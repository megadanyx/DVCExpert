from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import *

# Create your views here.

def home(request):
    try:
        courses = Course.objects.filter(is_visibil=True).order_by('-created_at')[:3]
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
    # Obține cursul pe baza ID-ului
    course = get_object_or_404(Course, id=id)

    # Obține curriculum-ul asociat cursului
    curriculum = Curriculum.objects.filter(course=course).first()

    if curriculum:
        # Dacă există curriculum, caută temele și obiectivele
        curriculum_themes = CurriculumThems.objects.filter(curriculum=curriculum)
        curriculum_items = CurriculumItem.objects.filter(curriculum_thems__curriculum=curriculum)
    else:
        # Dacă nu există curriculum, setează listele ca fiind goale
        curriculum_themes = []
        curriculum_items = []

    # Obține profesorii cursului
    teachers = course.teachers.all()

    # Creează un dicționar de context pentru template
    context = {'cours': course, 'teachers': teachers}
    
    # Adaugă variabilele doar dacă există
    if curriculum:
        context['curriculum'] = curriculum
        context['curriculum_themes'] = curriculum_themes
        context['curriculum_items'] = curriculum_items
    

    # Răspunde cu datele obținute
    return render(request, 'DCVExpert/product.html', context)

# def go_home(request):
#     return redirect('home')  # Redirecționează către pagina principală