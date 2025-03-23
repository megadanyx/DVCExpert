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
        categories = CoursCategory.objects.all()
        template = loader.get_template('DCVExpert/products.html')
        context = {'courses': courses,'categories':categories}
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return HttpResponse(template.render(context, request))
  
  
def courses_list(request):
    category_id = request.GET.get('category_id')  # Preia categoria selectată
    search_query = request.GET.get('search_query', '')  # Preia termenul de căutare (dacă există)

    Toate = CoursCategory.objects.filter(pk=4).first()  # Pentru dropdown
    courses = Course.objects.filter(is_visibil=True)  # Inițial, luăm toate cursurile vizibile
    if category_id != Toate.Category_name:
        if category_id:  # Filtrăm după categorie dacă a fost selectată
            courses = courses.filter(category_id=category_id)

    if search_query:  # Filtrăm și după termenul de căutare dacă a fost introdus
        courses = courses.filter(name__icontains=search_query)

    categories = CoursCategory.objects.all()  # Pentru dropdown

    return render(request, 'DCVExpert/products.html', {'courses': courses, 'categories': categories})


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


def joinUs(request):
    if request.method == 'POST':
        # Preluăm datele din formular
        fullname = request.POST.get('Fullname')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')

        # Creăm și salvăm un nou obiect JoinUs
        join_us_entry = JoinUs(
            Fullname=fullname,
            Phone=phone,
            Email=email,
        )
        join_us_entry.save()  # Salvează obiectul în baza de date

        # Afișăm un mesaj de succes
        # messages.success(request, "Înscrierea a fost realizată cu succes!")

        return redirect('home')  # Redirecționăm utilizatorul către pagina home sau altă pagină

    return redirect('home')  # Redirecționează la pagina formularului
