from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
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
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'DCVExpert/products.html',{'courses':courses})


# def go_home(request):
#     return redirect('home')  # Redirecționează către pagina principală