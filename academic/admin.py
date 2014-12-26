from django.contrib import admin

from academic.models import Author
from academic.models import Paper
from academic.models import Course
from academic.models import CourseInstance

class MyAdminSite(admin.AdminSite):
    site_header = 'Site Administration'

admin.site = MyAdminSite(name='myadmin')
admin.site.register(Author)
admin.site.register(Paper)
admin.site.register(Course)
admin.site.register(CourseInstance)


