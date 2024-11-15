import os
import uuid
import random
from datetime import datetime
from django.core.exceptions import ValidationError



def logo(instance, filename):
    upload_to = 'logo/'
    ext = filename.split('.')[-1]
    
    # current_date = datetime.now().strftime('%Y_%m_%d')
    
    filename = f"{uuid.uuid4()}.{ext}"
    
    return os.path.join(upload_to, filename)



def surat_permohonan(instance, filename):
    upload_to = 'surat_permohonan/'
    ext = filename.split('.')[-1]
    
    # current_date = datetime.now().strftime('%Y_%m_%d')
    
    filename = f"{uuid.uuid4()}.{ext}"
    
    return os.path.join(upload_to, filename)


def dokumen(instance, filename):
    upload_to = 'dokumen/'
    ext = filename.split('.')[-1]
    
    # current_date = datetime.now().strftime('%Y_%m_%d')
    
    filename = f"{uuid.uuid4()}.{ext}"
    
    return os.path.join(upload_to, filename)



def validate_file_size(file):
    max_size_kb = 2048  # Maksimum ukuran file dalam KB (2 MB)
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Ukuran file tidak boleh lebih dari {max_size_kb} KB.")