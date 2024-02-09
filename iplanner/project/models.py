from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models import Max
from django.db.models.signals import post_save

PROJECT_TYPES = [
    (1, "Business Website"),
    (2, "Promotional Websites"),
    (3, "eCommerce Website"),
    (4, "Blog or Personal Website"),
    (5, "School or College Website"),
    (6, "Business Directory"),
    (7, "Online Communities"),
    (8, "Portfolio Websites"),
]

class Project(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    name = models.CharField(max_length=150, null=True, blank=True)
    url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(blank=True)
    mission = models.CharField(max_length=250, null=True, blank=True)
    vision = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def _get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

    image_url = property(_get_image_url)

    def __str__(self):
        return self.name


# class ProjectFileQuerySet(models.query.QuerySet):
#
#     def project(self, project):
#         return self.filter(project=project)
#
#     def object(self, object_type, object_id):
#         return self.filter(object_type=object_type, object_id=object_id)
#
#     def type(self, type):
#         return self.filter(
#            type__icontains = type)
#
#     def search(self, query):
#         return self.filter(
#                 Q(alt__icontains=query) |
#                 Q(name__icontains=query)
#             )
#
#
#
# class ProjectFileManager(models.Manager):
#
#     def get_queryset(self):
#         return ProjectFileQuerySet(self.model, using=self._db)
#
#     def all(self):
#         return self.get_queryset().all()
#
#     def project(self, project):
#         return self.get_queryset().project(project)
#
#     def search(self, project,query):
#         return self.get_queryset().project(project).search(query)
#
#     def type(self, project, type):
#         return self.get_queryset().project(project).type(type)
#
#     def object(self, project, object_type, object_id ):
#         return self.get_queryset().project(project).object(object_type, object_id)

class ProjectFile(models.Model):
    OBJECT_TYPES = [
        (1, "1. answer"),
        (2, "2. survey"),
        (3, "3. page"),
        (4, "4. page_section"),
        (5, "5. mockup")
    ]

    user = models.ForeignKey(User, null=True, blank=True)
    project = models.ForeignKey(Project, null=True, blank=True)
    object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)
    object_id = models.IntegerField(null=False, blank=False)
    project_file = models.FileField(null=True, blank=True, upload_to='%Y/%m/%d/')
    type = models.CharField(max_length=20, blank=False, null=True)
    name = models.CharField(max_length=250, blank=False, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def _get_file_url(self):
        if self.project_file:
            return self.project_file.url
        else:
            return None

    file_url = property(_get_file_url)

    # objects = ProjectFileManager()

    def __str__(self):
        return self.name


def get_project_files_qty(object_type, object_id):
    qty = ProjectFile.objects.filter(object_type=object_type, object_id=object_id).count()
    if qty:
        return qty
    else:
        return 0

class ProjectCompetitor(models.Model):
    project = models.ForeignKey(Project, related_name="competitors")
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=1000, blank=False)
    position = models.PositiveIntegerField(null=True, blank=True)
    # target = models.ForeignKey("self", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # unique_together = [
        #     ("project", "position")
        # ]
        ordering = ["project", "position"]

    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.project.competitors.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super(ProjectCompetitor, self).save(*args, **kwargs)

    def move_up(self):
        try:
            other_position = self.project.competitors.order_by("-position").filter(
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
            other_position = self.project.competitors.order_by("position").filter(
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

    # def next_page(self):
    #     target = self
    #
    #     try:
    #         target = self.project.projects.get(
    #             page_num=self.position + 1
    #         )
    #     except ProjectCompetitor.DoesNotExist:
    #             target = None
    #
    #     if self.target:
    #             target = self.target
    #
    #     if target:
    #         target = target.next_page()
    #
    #     return target
    #
    #
    #
    # def is_last_page(self):
    #     return self.next_page() is None

    def __str__(self):

        return self.name

class ProjectMockup(models.Model):

    project = models.ForeignKey(Project, related_name='mockup_versions')
    accepted_owner = models.ForeignKey(User, blank=True, null=True)
    accepted_client = models.ForeignKey(User, blank=True, null=True, related_name="+")
    version = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField (default=True)
    comment = models.TextField()

    class Meta:

        ordering = ["project", "-version"]
    def save(self, *args, **kwargs):
        if self.version is None:
            max_version = self.project.mockup_versions.aggregate(Max("version"))
            self.version = (max_version.get("version__max") or 0) + 1
        return super(ProjectMockup, self).save(*args, **kwargs)

    def __str__(self):
        return "%s  %s  | %s" % (self.id, self.version, self.comment)


class ProjectMockupFiles(models.Model):
    project_mockup = models.ForeignKey(ProjectMockup, null=False, blank=False)
    project_file = models.ForeignKey(ProjectFile)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return "%s| %s" % (self.id, self.comment)


class ProjectTeam(models.Model):
    PERMISSION_TYPES = [
        (1, "1. Admin"),
        (2, "2. Member"),
        (3, "3. Client")
    ]
    project = models.ForeignKey(Project, null=False, blank=False, related_name='user_project')
    user = models.ForeignKey(User, null=False, blank=False)
    permission = models.IntegerField(choices=PERMISSION_TYPES, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "%s| %s" % (self.id, self.user)

def create_default_team_member(sender, instance, created, **kwargs):
    if created:
        ProjectTeam.objects.create(project=instance, user = instance.user, permission = 1)



post_save.connect(create_default_team_member, sender=Project)