import os
from django.utils.text import slugify

def course_image_upload_path(instance, filename):
    """Generează un nume personalizat pentru imaginea cursului."""
    ext = filename.split('.')[-1]  # Obține extensia fișierului
    filename = f"{slugify(instance.name)}.{ext}"  # Transformă numele cursului într-un format sigur

    # Salvează imaginile în MEDIA_ROOT/courses/{numele_cursului}/imagine.jpg
    path = os.path.join('photos/courses', slugify(instance.name))
    return os.path.join(path, filename)


def teacher_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]  # Obține extensia fișierului
    filename = f"{slugify(instance.name)}.{ext}"  # Transformă numele cursului într-un format sigur

    # Salvează imaginile în MEDIA_ROOT/courses/{numele_cursului}/imagine.jpg
    path = os.path.join('photos/teachers', slugify(instance.name))
    return os.path.join(path, filename)