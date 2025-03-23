from django.db import models
from DCVExpert.utils import teacher_image_upload_path, course_image_upload_path  # Import funcții personalizate

# Model pentru prețuri
class Price(models.Model):
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"New price: {self.new_price}"

# Model pentru descrierea cursurilor
class CourseDescription(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    duration = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    lesson_count = models.IntegerField()

    cours_descriprion_name = models.OneToOneField('Course', on_delete=models.CASCADE, related_name='description',null=True, blank=True)
    def __str__(self):
        return f"Descriprion for: {self.cours_descriprion_name}"  # Afișează primele 20 de caractere

# Model pentru profesori
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=1550)
    description = models.TextField()
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to=teacher_image_upload_path)

    def __str__(self):
        return self.name


# Model pentru cursuri
class Course(models.Model):
    name = models.CharField(max_length=510)
    photo = models.ImageField(upload_to=course_image_upload_path)
    price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True)
    about = models.ForeignKey('CourseDescription', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('CoursCategory', on_delete=models.SET_NULL, null=True)
    teachers = models.ManyToManyField('Teacher')
    is_visibil = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CoursCategory(models.Model):
    Category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Category_name

# Model pentru curriculum
class Curriculum(models.Model):
    course = models.OneToOneField('Course', on_delete=models.CASCADE, related_name='curriculum', null=True, blank=True)
    curriculum_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course.name if self.course else 'No Course'}. {self.curriculum_name}"

# Model pentru teme din curriculum
class CurriculumThems(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.curriculum.curriculum_name} - {self.title}"

# Model pentru obiectivele din curriculum
class CurriculumItem(models.Model):
    curriculum_thems = models.ForeignKey(CurriculumThems, on_delete=models.CASCADE, related_name='CurriculumThems', null=True, blank=True)
    curriculum_cours = models.ForeignKey(Curriculum, on_delete=models.CASCADE,null=True, blank=True)
    objective = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.curriculum_thems.title} - {self.objective}"

class JoinUs(models.Model):
    Fullname = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=255)
    coursName = models.CharField(max_length=255, blank=True, null=True, default=None)
    Checked = models.BooleanField(default=False)

    def __str__(self):
        return self.Fullname