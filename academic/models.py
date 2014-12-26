from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name + " -- " + self.affiliation
    
class Paper(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=250)
    
    CONFERENCE = "CR"
    JOURNAL = "JL"
    MANUSCRIPT = "MA"
    publication_type_choices = (
        (CONFERENCE, "Conference"),
        (JOURNAL, 'Journal'),
        (MANUSCRIPT, 'Manuscript')
    )
    publication_type = models.CharField(max_length=20,
                                        choices=publication_type_choices
    )

    publication_venue = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    page_nums = models.CharField(max_length=25, blank=True)
    volume = models.SmallIntegerField(blank=True, null=True)
    number = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    course_code = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=250)
    length = models.CharField(max_length=25)

    def __str__(self):
        return self.course_code + ": " + self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course)
    
    TEACHING_ASSISTANT = "TA"
    COURSE_INSTRUCTOR = "CI"
    role_choices = (
        (TEACHING_ASSISTANT, "Teaching Assistant"),
        (COURSE_INSTRUCTOR, "Course Instructor")
    )
    role = models.CharField(max_length=20,
                            choices=role_choices
    )
    semester = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return str(self.course) + ", " + self.semester
    
