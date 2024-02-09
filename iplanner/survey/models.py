from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from iplanner.general.models import Language, SystemTag
from iplanner.project.models import Project, get_project_files_qty, PROJECT_TYPES
from iplanner.page.models import PageType
from django.db.models import Max
from django.db.models.signals import post_save
from iplanner.profile.models import UserProfile
from iplanner.task.models import get_open_tasks_qty, get_tasks_qty
from iplanner.comments.models import get_coments_qty
from iplanner.link.models import get_links_qty
# from django.db.models import Sum

OBJECT_TYPES = [
        (1, "1. project"),
        (2, "2. product"),
        (3, "3. page"),
    ]

class Survey(models.Model):

    object_type = models.IntegerField(choices=OBJECT_TYPES, null=True, blank=False, default=None)
    object_id = models.IntegerField(null=True, blank=False, default=None)
    page_type = models.ForeignKey(PageType, blank=True, null=True, default=None)
    user = models.ForeignKey(User)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, related_name="surveys", null=True)
    language = models.ForeignKey(Language, blank=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    html_title = models.CharField(max_length=60, null=True, blank=True)
    html_description = models.CharField(max_length=100, null=True, blank=True)
    system = models.BooleanField(default=False)
    template = models.BooleanField(default=False)
    is_publick = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def _get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None


    def _get_questions_qty(self):
        qty = SurveyField.objects.filter(page__survey=self.id).count()
        if qty:
            return qty
        else:
            return 0


    def _get_completed_questions_qty(self):
        qty = SurveyField.objects.filter(page__survey=self.id, completed=True).count()
        if qty:
            return qty
        else:
            return 0

    def _get_open_tasks_qty(self):
        fileds = SurveyField.objects.filter(page__survey=self.id, completed=False)

        qty=0
        for filed in fileds:
            qty=qty+get_open_tasks_qty(1, filed.id)

        if qty:
            return qty
        else:
            return 0



    image_url = property(_get_image_url)
    fields_qty = property(_get_questions_qty)
    completed_fields_qty = property(_get_completed_questions_qty)
    open_tasks_qty = property(_get_open_tasks_qty)


    def copy_survey_to_project(pk, project, user):
        new_obj = Survey.objects.get(pk=pk)
        new_obj.pk = None
        new_obj.id = None
        new_obj.project = project
        new_obj.user = user
        new_obj.template = False
        new_obj.is_publick = False
        new_obj.system = False
        print(new_obj)
        new_obj.save()

        page_set = SurveyPage.objects.filter(survey=pk)

        for page in page_set:
            page.copy_to_survey(new_obj)

        return new_obj

    def __str__(self):
        return "%s  %s" % (self.name, self.id)


def create_surveys_for_project(project, user, language):
    default_survey_set = DefaultSurvey.objects.filter(language=language, survey__system_tag__functionality_type=1)

    for default_survey in default_survey_set:
        user_default_survey_set = DefaultUserSurvey.objects.filter(user=user,
                                                                   survey__system_tag=default_survey.survey.system_tag.id)
        if user_default_survey_set:
            Survey.copy_survey_to_project(user_default_survey_set.survey.id, project, user)
        else:
            Survey.copy_survey_to_project(default_survey.survey.id, project, user)


def create_default_surveys(sender, instance, created, **kwargs):
    if created:

        prodile_obj = UserProfile.objects.get(user=instance.user.id)
        language = prodile_obj.interface_lang

        if language:
            create_surveys_for_project(instance, instance.user, language)
        else:
            create_surveys_for_project(instance, instance.user, 2)


post_save.connect(create_default_surveys, sender=Project)


class SurveyPage(models.Model):
    survey = models.ForeignKey(Survey, blank=False, related_name="pages")
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = [ "position"]

    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.survey.pages.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super(SurveyPage, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = self.survey.pages.order_by("-position").filter(
                position__lt=self.position
            )[0]
            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return

    def move_down(self):
        try:
            other_position = self.survey.pages.order_by("position").filter(
                position__gt=self.position
            )[0]

            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return

    def copy_to_survey(self, new_survey):
        pk = self.id
        new_obj = self
        new_obj.pk = None
        new_obj.id = None
        new_obj.survey = new_survey
        new_obj.save()

        field_set = SurveyField.objects.filter(page=pk)

        for field in field_set:
            field.copy_to_page(new_obj)

    def __str__(self):
        return "%s  %s  %s" % (self.name, self.id, self.survey.name)


class SurveyField(models.Model):
    # survey = models.ForeignKey(Survey, blank=False, related_name="fields")
    page = models.ForeignKey(SurveyPage, blank=False, related_name="page_fields")
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(blank=True)
    answer = models.TextField(blank=True, null=True)

    # TODO field_type, maximum_choices, required
    completed = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def _get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

    def _get_comments_qty(self):
        qty = get_coments_qty(1, self.id)
        if qty:
            return qty
        else:
            return 0

    def _get_links_qty(self):
        qty = get_links_qty(1, self.id)
        if qty:
            return qty
        else:
            return 0

    def _get_tasks_qty(self):
        qty = get_tasks_qty(1, self.id)
        if qty:
            return qty
        else:
            return 0

    def _get_open_tasks_qty(self):
        qty = get_open_tasks_qty(1, self.id)
        if qty:
            return qty
        else:
            return 0

    def _get_project_files_qty(self):
        qty = get_project_files_qty(1, self.id)
        if qty:
            return qty
        else:
            return 0

    image_url = property(_get_image_url)

    comments_qty = property(_get_comments_qty)
    links_qty = property(_get_links_qty)
    tasks_qty = property(_get_tasks_qty)
    open_tasks_qty = property(_get_open_tasks_qty)
    project_files_qty = property(_get_project_files_qty)

    class Meta:

        ordering = [ "position"]


    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.page.page_fields.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super(SurveyField, self).save(*args, **kwargs)


    def move_up(self):
        try:
            other_position = self.page.page_fields.order_by("-position").filter(
                position__lt=self.position
            )[0]
            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return


    def move_down(self):
        try:
            other_position = self.page.page_fields.order_by("position").filter(
                position__gt=self.position
            )[0]

            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return


    def copy_to_page(self, new_page):
        pk = self.id
        new_obj = self
        new_obj.pk = None
        new_obj.id = None
        new_obj.page = new_page
        new_obj.save()



    def __str__(self):
        return "%s  %s  | %s" % (self.name, self.id, self.page.survey.name)





class DefaultSurvey(models.Model):
    survey = models.ForeignKey(Survey, blank=False, null=False)
    language = models.ForeignKey(Language, blank=False, null=False)
    position = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        # unique_together = [
        #     ("survey", "language")
        # ]
        ordering = ["language", "position"]

    def __str__(self):
        return "%s  %s" % (self.survey.name, self.language.code)


class DefaultUserSurvey(models.Model):
    survey = models.ForeignKey(Survey, blank=False, null=False)
    user = models.ForeignKey(User, blank=False, null=False)

    def __str__(self):
        return "%s  %s" % (self.survey.name, self.user)


class SurveysSet (models.Model):

    project_type = models.IntegerField(choices=PROJECT_TYPES, null=False, blank=False)
    user = models.ForeignKey(User, blank=False, null=False)
    language = models.ForeignKey(Language, blank=False, null=False, default=2)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=True, null=True)

    system = models.BooleanField(default=False)
    is_publick = models.BooleanField(default=False)

    def __str__(self):
        return "%s  %s" % (self.name, self.user)


class SurveysInSet (models.Model):


    # object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)

    survey = models.ForeignKey(Survey, blank=False, null=False)
    set = models.ForeignKey(SurveysSet, blank=False, null=False)

    def __str__(self):
        return "%s  %s" % (self.survey, self.set)