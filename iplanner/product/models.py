from __future__ import unicode_literals
# from iplanner.survey.models import Survey, DefaultSurvey, DefaultUserSurvey
from iplanner.project.models import Project, ProjectFile

from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from iplanner.profile.models import UserProfile

class Product(models.Model):
    PRODUCT_TYPES = [
        (1, "1. Product"),
        (2, "2. Service"),
        (3, "3. Information")
    ]

    project = models.ForeignKey(Project, related_name="products")
    image = models.ForeignKey(ProjectFile, null=True, blank=True)
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    product_type = models.IntegerField(choices=PRODUCT_TYPES, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.project.name)




# def create_default_product_surveys(sender, instance, created, **kwargs):
#     if created:
#
#         profile_obj = UserProfile.objects.get(user=instance.project.user.id)
#         language = profile_obj.interface_lang
#
#         if language:
#             create_surveys_for_product(instance, instance.project.user, language)
#         else:
#             create_surveys_for_product(instance, instance.project.user, 2)
#
#
# def create_surveys_for_product(product, user, language):
#     default_survey_set = DefaultSurvey.objects.filter(language=language, survey__system_tag__functionality_type=2)
#
#     for default_survey in default_survey_set:
#         user_default_survey_set = DefaultUserSurvey.objects.filter(user=user,
#                                                                    survey__system_tag=default_survey.survey.system_tag.id)
#         if user_default_survey_set:
#             new_survey = Survey.copy_survey_to_project(user_default_survey_set.survey.id, product.project, user)
#             # ProductSurvey.objects.create(product=product, survey=new_survey)
#         else:
#             new_survey = Survey.copy_survey_to_project(default_survey.survey.id, product.project, user)
#             # ProductSurvey.objects.create(product=product, survey=new_survey)





# post_save.connect(create_default_product_surveys, sender=Product)


#
# class ProductFile(models.Model):
#
#     product = models.ForeignKey(Product, related_name="files", null=False, blank=False)
#     project_file = models.ForeignKey(ProjectFile)
#
#     create_date = models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)
#
#
#     def __str__(self):
#         return "%s - %s" % (self.project_file.file.name, self.product.name)

# class ProductSurvey(models.Model):
#
#     product = models.ForeignKey(Product, null=False, blank=False)
#     survey = models.OneToOneField(Survey, null=False, blank=False)
#     create_date = models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)
#
#
#     def __str__(self):
#         return "%s - %s" % (self.product.name, self.survey.name)




class ProductCompetitor(models.Model):

    product = models.ForeignKey(Product, related_name="product_competitors", null=False, blank=False)
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=1000, blank=False)
    position = models.PositiveIntegerField(null=True, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["product", "position"]

    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.product.product_competitors.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super( ProductCompetitor, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = self.product.product_competitors.order_by("-position").filter(
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
            other_position = self.product.product_competitors.order_by("position").filter(
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

        return "%s  %s" % (self.name, self.product.name)