from django.db import models
from DCVExpert.utils import teacher_image_upload_path, course_image_upload_path  # Import funcții personalizate

# Model pentru prețuri
class Price(models.Model):
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.new_price} RON"

# Model pentru descrierea cursurilor
class CourseDescription(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    duration = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    lesson_count = models.IntegerField()

    def __str__(self):
        return self.short_description[:50]  # Afișează primele 50 de caractere

# Model pentru profesori
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to=teacher_image_upload_path)

    def __str__(self):
        return self.name

# Model pentru curriculum
class Curriculum(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.number}. {self.title}"

# Model pentru elemente din curriculum
class CurriculumItem(models.Model):
    curriculumId = models.ForeignKey('Curriculum', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.curriculum.title} - {self.name}"

# Model pentru cursuri
class Course(models.Model):
    name = models.CharField(max_length=510)
    photo = models.ImageField(upload_to=course_image_upload_path)
    price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True)
    about = models.ForeignKey('CourseDescription', on_delete=models.SET_NULL, null=True)
    curriculum = models.ForeignKey('Curriculum', on_delete=models.SET_NULL, null=True)
    teachers = models.ManyToManyField('Teacher')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
