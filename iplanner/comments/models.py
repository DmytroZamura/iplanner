from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# class Conversation(models.Model):
#     OBJECT_TYPES = [
#         (1, "1. answer"),
#         (2, "2. page"),
#         (3, "3. mockup")
#     ]
#
#     object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)
#     object_id = models.IntegerField(null=False, blank=False)
#     create_date = models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         unique_together = ("object_type", "object_id")
#
#     def __str__(self):
#         return "%s| %s" % (self.object_type, self.object_type)


class Comment(models.Model):
    OBJECT_TYPES = [
        (1, "1. answer"),
        (2, "2. page"),
        (3, "3. mockup")
    ]
    object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)
    object_id = models.IntegerField(null=False, blank=False)

    user = models.ForeignKey(User, null=False, blank=False)
    comment = models.CharField(max_length=1000, null=True, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        # unique_together = ("object_type", "object_id")
        ordering = ["object_type", "object_id", "create_date"]


    def __str__(self):
        return "%s| %s" % (self.id, self.comment)


def get_coments_qty(object_type, object_id):
    qty = Comment.objects.filter(object_type=object_type, object_id=object_id).count()
    if qty:
        return qty
    else:
        return 0
