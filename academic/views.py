from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register

from academic.models import Paper
from academic.models import CourseInstance

def index(request):
    context = {'headline' : "Main"}
    return render(request, 'academic/index.html', context)

def format_authors(paper):
    """ Format the authors of the paper into a printable list. """
    author_list = [p.name for p in paper.author.all()]
    author_list = sorted(author_list, key=lambda x: x.split()[-1])
    return ", ".join(author_list)

def papers(request):
    ## Format the author list of each paper
    papers = Paper.objects.all()
    papers = [x for x in reversed(sorted(papers, key=lambda x: x.year))]
    papers = zip([format_authors(paper) for paper in papers], papers)
    context = {'headline' : 'Projects and Publications', 'papers' : papers}
    return render(request, 'academic/papers.html', context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def semester_compare(cmp1, cmp2):
    """ 
    Given two strings of the form "[Winter, Summer, Fall] [Year]" order
    them lexicographically (in the first coordinate) by Winter < Summer < Fall.
    Years are ordered as normal.
    """
    split1 = cmp1.split()
    split2 = cmp2.split()
    order_map = {u"Winter" : 0, u"Spring" : 1, u"Summer" : 2, u"Fall" : 3}
    if split1[1] < split2[1]:
        return -1
    elif split1[1] == split2[1]:
        if order_map[split1[0]] < order_map[split2[0]]:
            return -1
        elif order_map[split1[0]] == order_map[split2[0]]:
            return 0
        else:
            return 1
    else:
        return 1
        
def teaching(request):
    all_courses = CourseInstance.objects.all()
    ## plop all the courses into a semester map
    course_semester_map = {}
    for course in all_courses:
        if course.semester in course_semester_map:
            course_semester_map[course.semester].append(course)
        else:
            course_semester_map[course.semester] = [course]
    all_semesters = reversed(sorted(course_semester_map.keys(), cmp=semester_compare))
    context = {'headline' : "Teaching", 'course_semester_map' : course_semester_map, 'all_semesters' : all_semesters}
    return render(request, 'academic/teaching.html', context)
