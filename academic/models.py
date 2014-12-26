from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=250)
    
class Paper(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=250)
    publication_type = models.CharField(max_length=20)
    publication_venue = models.CharField(max_length=50)
    year = models.DateField()
    page_nums = models.CharField(max_length=25)
    volume = models.SmallIntegerField()
    number = models.SmallIntegerField()

class Course(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=250)
    length = models.CharField(max_length=25)

class CourseInstance(models.Model):
    course = models.ForeignKey(Course)
    role = models.CharField(max_length=20)
    year = models.DateField()
    
    
