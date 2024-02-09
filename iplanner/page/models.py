from __future__ import unicode_literals
#
# import null
from django.db import models
from iplanner.general.models import SystemTag, Language
# from iplanner.survey.models import Survey, DefaultSurvey
from iplanner.project.models import ProjectFile, Project
from iplanner.product.models import Product
from iplanner.profile.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Max
from django.db.models.signals import post_save

class TemplateSection(models.Model):
    user = models.ForeignKey(User, blank=False, null=True)
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=80, blank=False)

    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    system = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.id)


class PageTemplate(models.Model):
    user = models.ForeignKey(User, blank=False, null=True)
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    system = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.id)

class PageTemplateSection(models.Model):
    page_template = models.ForeignKey(PageTemplate, blank=False, null=False)
    template_section = models.ForeignKey(TemplateSection, blank=False, null=False)
    position = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["page_template", "position"]

    def save(self, *args, **kwargs):
      if self.position is None:
            max_position = PageTemplateSection.objects.filter(page_template=self.page_template).aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
            return super(PageTemplateSection, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = PageTemplateSection.objects.filter(page_template=self.page_template).order_by("-position").filter(
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

    def move_down(self):
        try:
            other_position = PageTemplateSection.objects.filter(page_template=self.page_template).order_by("position").filter(
                position__gt=self.position)[0]
            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return

    def __str__(self):
        return "%s - %s" % (self.page_template.name, self.template_section.name)

class PageType(models.Model):
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    language = models.ForeignKey(Language, blank=False, null=False, default=2)
    # template_survey = models.ForeignKey(Survey, blank=True, null=True)
    page_template = models.ForeignKey(PageTemplate, blank=True, null=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position",]

    def __str__(self):
        return "%s - %s" % (self.id, self.name)


class PageTypeUserTemplates(models.Model):
    user = models.ForeignKey(User, blank=False, null=True)
    page_type = models.ForeignKey(PageType, blank=False, null=False)
    # template_survey = models.ForeignKey(Survey, blank=False, null=False)
    page_template = models.ForeignKey(PageTemplate, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.user)



class Page(models.Model):

    parent = models.ForeignKey('self', related_name='child_set', null=True, blank=True, default=None)
    project = models.ForeignKey(Project, null=False, blank=False, related_name='project_pages')
    product = models.ForeignKey(Product, null=True
                                , blank=True, related_name='product_pages')
    og_imgage = models.ForeignKey(ProjectFile, null=True, blank=True)
    page_type = models.ForeignKey(PageType, blank=True, null=True)
    name = models.CharField(max_length=80, blank=False)
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=True)
    key_word = models.CharField(max_length=80, null=True, blank=True)
    additional_key_word = models.CharField(max_length=80, null=True, blank=True)
    page_body = models.TextField(blank=True)
    # version = models.PositiveIntegerField(null=True, blank=True)
    # todo - vesion control

    active = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    accepted_owner = models.ForeignKey(User, blank=True, null=True)
    accepted_client = models.ForeignKey(User, blank=True, null=True, related_name="+")
    url = models.URLField(blank=True, null=True)

    position = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position",]



    def save(self, *args, **kwargs):
        # if self.version is None:
        #     max_version = self.project.mockup_versions.aggregate(Max("version"))
        #     self.version = (max_version.get("version__max") or 0) + 1

        if self.position is None:
            if self.parent:
                max_position = self.parent.child_set.aggregate(Max("position"))
                self.position = (max_position.get("position__max") or 0) + 1

            else:
                max_position = Page.objects.filter(parent=None).aggregate(Max("position"))
                self.position = (max_position.get("position__max") or 0) + 1


        return super(Page, self).save(*args, **kwargs)

    def move_up(self):
        try:
            if self.parent:
                other_position = self.parent.child_set.order_by("-position").filter(
                    position__lt=self.position
                )[0]
            else:
                other_position = Page.objects.filter(parent=None).order_by("-position").filter(
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

    def move_down(self):
        try:
            if self.parent:
                other_position = self.parent.child_set.order_by("position").filter(
                    position__gt=self.position
                )[0]
            else:
                other_position = Page.objects.filter(parent=None).order_by("position").filter(
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

    def __str__(self):
        return "%s  %s" % (self.name, self.id)

def create_default_page_objects(sender, instance, created, **kwargs):
    if created:

        profile_obj = UserProfile.objects.get(user=instance.project.user.id)
        language = profile_obj.interface_lang

        if language:
            create_objects_for_page(instance, instance.project.user, language)
        else:
            create_objects_for_page(instance, instance.project.user, 2)




def create_objects_for_page(page, user, language):
    try:
        user_page_type_template = PageTypeUserTemplates.objects.get(page_type=page.page_type, user=user)
    except:
        user_page_type_template = None


    # template_survey = null
    if not user_page_type_template and page.page_type:
        page_type = PageType.objects.get(id=page.page_type.id, system_tag__language=language)
        template_survey = page_type.template_survey.id
    else:
        template_survey = user_page_type_template.template_survey.id

    # if template_survey:
    #     new_survey = Survey.copy_survey_to_project(template_survey, page.project, user)
    #     PageSurvey.objects.create(page=page, survey=new_survey)






post_save.connect(create_default_page_objects, sender=Page)


# class PageSurvey(models.Model):
#     page = models.ForeignKey(Page, blank=False, null=True, related_name='page_surveys')
#     survey = models.ForeignKey(Survey, blank=False, null=False)
#
#     create_date = models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return "%s - %s" % (self.page.name, self.survey.name)



class PageSection(models.Model):
    page = models.ForeignKey(Page, blank=False, null=True, related_name='sections')
    system_tag = models.ForeignKey(SystemTag, blank=True, null=True)
    name = models.CharField(max_length=80, blank=False)

    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    accepted_owner = models.ForeignKey(User, blank=True, null=True)
    accepted_client = models.ForeignKey(User, blank=True, null=True, related_name="+")
    # version = models.PositiveIntegerField(null=True, blank=True)
    # todo - vesion control
    active = models.BooleanField(default=True)
    system = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # if self.version is None:
        #     max_version = self.page.sections.aggregate(Max("version"))
        #     self.version = (max_version.get("version__max") or 0) + 1

        if self.position is None:
            max_position = PageSection.objects.filter(page=self.page).aggregate(
                Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
            return super(PageSection, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = \
            PageSection.objects.filter(page_template=self.page).order_by("-position").filter(
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

    def move_down(self):
        try:
            other_position = \
            PageTemplateSection.objects.filter(page_template=self.page).order_by("position").filter(
                position__gt=self.position)[0]
            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return


    def __str__(self):
        return "%s - %s" % (self.page.name, self.name)

class PageMockup(models.Model):

    page = models.ForeignKey(Page, related_name='mockup_versions')
    accepted_owner = models.ForeignKey(User, blank=True, null=True)
    accepted_client = models.ForeignKey(User, blank=True, null=True, related_name="+")
    version = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField (default=True)
    comment = models.TextField()

    class Meta:

        ordering = ["page", "-version"]
    def save(self, *args, **kwargs):
        if self.version is None:
            max_version = self.page.mockup_versions.aggregate(Max("version"))
            self.version = (max_version.get("version__max") or 0) + 1
        return super(PageMockup, self).save(*args, **kwargs)

    def __str__(self):
        return "%s  %s  | %s" % (self.id, self.version, self.comment)


class PageMockupFiles(models.Model):
    page_mockup = models.ForeignKey(PageMockup, null=False, blank=False, related_name='mockup_files')
    page_file = models.ForeignKey(ProjectFile)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return "%s| %s" % (self.id, self.comment)


class PageCompetitor(models.Model):
    page = models.ForeignKey(Page, related_name="competitors")
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=1000, blank=False)
    position = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # unique_together = [
        #     ("project", "position")
        # ]
        ordering = ["page", "position"]

    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.page.competitors.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super(PageCompetitor, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = self.page.competitors.order_by("-position").filter(
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
            other_position = self.page.competitors.order_by("position").filter(
                position__gt=self.position
            )[0]
            print(other_position)
            existing = self.position
            other = other_position.position
            self.position = other
            other_position.position = existing
            other_position.save()
            self.save()
        except IndexError:
            return



    def __str__(self):

        return self.name
