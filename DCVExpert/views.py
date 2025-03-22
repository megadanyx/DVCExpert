from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Price, CourseDescription, Teacher, Curriculum, CurriculumItem, Course

# Create your views here.

def home(request):
    try:
        courses = Course.objects.filter(is_visibil=True)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'DCVExpert/index.html',{'courses':courses})

def courses(request):
    try:
        courses = Course.objects.filter(is_visibil=True)
        template = loader.get_template('DCVExpert/products.html')
        context = {'courses': courses, }
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return HttpResponse(template.render(context, request))
    # return render(request, 'DCVExpert/products.html',{'courses':courses})

# def course(request, id):
#     try:
#         course = Course.objects.get(id=id) # get the course with the id num
#         teachers = course.teachers.all()  # Obține toți profesorii asociați cursului
#         # course_description = CourseDescription.objects.get(course=course) # get the course description for the course
#         # print(teachers)
#         template = loader.get_template('DCVExpert/product.html')
#         context = {'cours': course, 'teachers': teachers }
#     except Poll.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return HttpResponse(template.render(context, request))
def course(request, id):
    course = get_object_or_404(Course, id=id)
    teacher = course.teachers.all()  # Obține profesorii asociați cursului

    return render(request, 'DCVExpert/product.html', {'cours': course, 'teachers': teacher})

# def go_home(request):
#     return redirect('home')  # Redirecționează către pagina principală