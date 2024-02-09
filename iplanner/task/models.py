from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models



class Task(models.Model):
    OBJECT_TYPES = [
        (1, "1. answer"),
        (2, "2. page"),
        (3, "3. mockup")
    ]
    STATUSES = [
        (1, "1. open"),
        (2, "2. paused"),
        (3, "3. finished"),
        (4, "4. closed")

    ]

    object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)
    object_id = models.IntegerField(null=False, blank=False)
    created_user = models.ForeignKey(User, null=False, blank=False, related_name='my_tasks')
    assigned_user = models.ForeignKey(User, blank=True, null=True, related_name='assigned_tasks')
    dead_line = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=250, null=True, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, null=False, blank=False, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # unique_together = ("object_type", "object_id")
        ordering = ["object_type","object_id", "status","dead_line"]



    def __str__(self):
        return "%s| %s" % (self.id, self.name)


def get_tasks_qty(object_type, object_id):
    qty = Task.objects.filter(object_type=object_type, object_id=object_id).count()
    if qty:
        return qty
    else:
        return 0


def get_open_tasks_qty(object_type, object_id):
    qty = Task.objects.filter(object_type=object_type, object_id=object_id, status=1).count()
    if qty:
        return qty
    else:
        return 0
