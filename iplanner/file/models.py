from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models



# class File(models.Model):
#
#
#     user = models.ForeignKey(User)
#     file = models.FileField(null=True, blank=True, upload_to='%Y/%m/%d/')
#
#
#
#     name = models.CharField(max_length=250, blank=False)
#     type = models.CharField(max_length=12, blank=False)
#     create_date = models.DateTimeField(auto_now_add=True)
#
#     def _get_file_url(self):
#         if self.file:
#             return self.file.url
#         else:
#             return None
#
#     file_url = property(_get_file_url)
#     def __str__(self):
#         return self.name





