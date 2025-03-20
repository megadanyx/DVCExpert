import os
from django.utils.text import slugify

def course_image_upload_path(instance, filename):
    """Generează un nume personalizat pentru imaginea cursului."""
    ext = filename.split('.')[-1]  # Obține extensia fișierului
    filename = f"{instance.name.replace(' ', '_').lower()}.{ext}"  # Transformă numele cursului într-un format sigur
    path = 'DCVExpert/DbPhotos/Courses/'+ instance.name
    return os.path.join(path, filename)


def teacher_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{slugify(instance.name)}.{ext}"
    path = 'DCVExpert/DbPhotos/teachers/'+ instance.name
    return os.path.join(path, filename)