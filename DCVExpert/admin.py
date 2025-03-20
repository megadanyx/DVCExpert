from django.contrib import admin
from .models import Price, CourseDescription, Teacher, Curriculum, CurriculumItem, Course

# Register your models here.


admin.site.register(Price)
admin.site.register(CourseDescription)
admin.site.register(Teacher)
admin.site.register(Curriculum)
admin.site.register(CurriculumItem)
admin.site.register(Course)


