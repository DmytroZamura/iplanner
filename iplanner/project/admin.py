from __future__ import absolute_import
from django.contrib import admin
from .models import *



class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectFile._meta.fields]

    class Meta:
        model = ProjectFile

admin.site.register(ProjectFile, ProjectFileAdmin)


class ProjectCompetitorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectCompetitor._meta.fields]

    class Meta:
        model = ProjectCompetitor

admin.site.register(ProjectCompetitor, ProjectCompetitorAdmin)

class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProjectTeam._meta.fields]

    class Meta:
        model = ProjectTeam

admin.site.register(ProjectTeam, ProjectTeamAdmin)