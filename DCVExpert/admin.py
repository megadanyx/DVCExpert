from django.contrib import admin
from .models import *

# Register your models here.


# Inline pentru 'CurriculumThems'
class CurriculumThemsInline(admin.TabularInline):  
    model = CurriculumThems
    extra = 1  # Numărul de rânduri goale de adăugat implicit

# Inline pentru 'CurriculumItem' (legătura este acum cu CurriculumThems)
class CurriculumItemInline(admin.TabularInline):
    model = CurriculumItem
    extra = 3  # Numărul de rânduri goale de adăugat implicit

# # Admin personalizat pentru modelul 'Curriculum'
# @admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    inlines = [CurriculumThemsInline, CurriculumItemInline]  # Legăm doar CurriculumThems la Curriculum
    # list_display = ('curriculum_name', 'course')  # Afișează numele curriculumului și cursul asociat

# # Admin pentru 'CurriculumThems', adăugăm inline pentru 'CurriculumItem'
# @admin.register(CurriculumThems)
# class CurriculumThemsAdmin(admin.ModelAdmin):
#     inlines = [CurriculumItemInline] 


admin.site.register(Price)
admin.site.register(CourseDescription)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Curriculum,CurriculumAdmin)
# admin.site.register(CurriculumThems)
# admin.site.register(CurriculumItem)
# admin.site.register(Curriculum)
# admin.site.register(CurriculumThems)
# admin.site.register([Curriculum,CurriculumThems,CurriculumItem])
# admin.site.register(CurriculumItem)
# admin.site.register(CurriculumThems)
# admin.site.register(Curriculum, CurriculumAdmin)


