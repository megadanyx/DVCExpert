import os
from django.utils.text import slugify

def course_image_upload_path(instance, filename):
    """Generează un nume personalizat pentru imaginea cursului."""
    ext = filename.split('.')[-1]  # Obține extensia fișierului
    filename = f"{instance.Name.replace(' ', '_').lower()}.{ext}"  # Transformă numele cursului într-un format sigur
    return os.path.join('photos/', filename)


def teacher_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{slugify(instance.name)}.{ext}"
    return os.path.join('teachers/', filename)