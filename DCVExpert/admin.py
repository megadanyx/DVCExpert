from django.contrib import admin
from .models import *
from .forms import CurriculumItemForm, CurriculumThemsForm, CurriculumForm

# Inline pentru 'CurriculumThems'
class CurriculumThemsInline(admin.TabularInline):  
    model = CurriculumThems
    extra = 1  # Numărul de rânduri goale de adăugat implicit
    form = CurriculumThemsForm  # Formularul personalizat pentru 'CurriculumThems'
# Inline pentru 'CurriculumItem' (legătura este acum cu CurriculumThems)
class CurriculumItemInline(admin.TabularInline):
    model = CurriculumItem
    extra = 3  # Numărul de rânduri goale de adăugat implicit
    form = CurriculumItemForm
class CurriculumAdmin(admin.ModelAdmin):
    inlines = [CurriculumThemsInline, CurriculumItemInline]  # Legăm doar CurriculumThems la Curriculum
    list_display = ('curriculum_name', 'course')  # Afișează numele curriculumului și cursul asociat
    form = CurriculumForm  # Formularul personalizat pentru 'Curriculum'
    can_delete = True  # Nu permitem ștergerea curriculum-ului

class JoinUsAdmin(admin.ModelAdmin):
    # Afișează câmpurile dorite în lista de obiecte
    list_display = ('Fullname', 'Email', 'Phone', 'Checked', 'coursName')  # Adăugăm 'Checked' în listă

    # Permite modificarea câmpului 'Checked' direct din listă
    list_editable = ('Checked',)





admin.site.register(Price)
admin.site.register(CourseDescription)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Curriculum,CurriculumAdmin)
admin.site.register(CoursCategory)
admin.site.register(JoinUs, JoinUsAdmin)


