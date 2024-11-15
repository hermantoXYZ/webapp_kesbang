# skt/models.py
from django.utils import timezone
import uuid
from django.db import models
from accounts.models import User
from .image_utils import logo, surat_permohonan, dokumen, validate_file_size


STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('completed', 'Completed'),
    ]

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nama_organisasi = models.CharField(max_length=255)
    register = models.CharField(max_length=10, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to=logo, blank=False, null=True, validators=[validate_file_size])
    is_completed = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)  # Field untuk status verifikasi
    verified_at = models.DateTimeField(null=True, blank=True)  # Tanggal dan waktu verifikasi
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        if not self.register:
            self.register = timezone.now().strftime("%Y%m%d") + uuid.uuid4().hex[:4].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.register

    def verify(self):
        """Metode untuk memverifikasi formulir."""
        self.is_verified = True
        self.verified_at = timezone.now()  # Menyimpan waktu verifikasi
        self.save()
class Pemohon(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register=models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True, related_name='pemohon')
    nama_lengkap = models.CharField(max_length=255)
    nik = models.CharField(max_length=16, unique=True)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    alamat = models.TextField()
    tempat_tanggal_lahir = models.CharField(max_length=255)
    tanggal_lahir_pemohon = models.DateField()
    pekerjaan = models.CharField(max_length=255)
    no_wa = models.CharField(max_length=15)
    email = models.EmailField()
    surat_permohonan_skt = models.FileField(upload_to=surat_permohonan, blank=False, null=False)
    nomor_surat = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nama_lengkap

class Organisasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register = models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True, related_name='organisasi')
    nama_notaris = models.CharField(max_length=255)
    nomor_akta = models.CharField(max_length=50)
    tanggal_akta = models.DateField()
    nama_organisasi = models.CharField(max_length=255)
    bidang_kegiatan = models.CharField(max_length=255)
    alamat_kantor = models.TextField()
    tempat_pendirian = models.CharField(max_length=255)
    tanggal_pendirian = models.DateField()
    asas_ciri_organisasi = models.CharField(max_length=255)
    tujuan_organisasi = models.TextField()
    masa_bakti_kepengurusan = models.CharField(max_length=50)
    keputusan_tertinggi_organisasi = models.CharField(max_length=255)
    unit_cabang = models.CharField(max_length=255)
    npwp = models.CharField(max_length=15)
    sumber_keuangan = models.TextField()
    lambang_logo = models.ImageField(upload_to=logo, blank=True, null=True)
    bendera = models.ImageField(upload_to=logo, blank=True, null=True)

    def __str__(self):
        return self.nama_organisasi



class Pengurus(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    
    STATUS_PERKAWINAN_CHOICES = [
        ('Belum Kawin', 'Belum Kawin'),
        ('Kawin', 'Kawin'),
        ('Cerai Hidup', 'Cerai Hidup'),
        ('Cerai Mati', 'Cerai Mati'),
    ]

    AGAMA_CHOICES = [
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Konghucu', 'Konghucu'),
    ]
    
    # Pembina dan Penasehat
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register = models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True, related_name='pengurus')
    nama_pembina = models.CharField(max_length=255)
    nama_penasehat = models.CharField(max_length=255)
    
    # Data Pendiri
    nama_pendiri = models.CharField(max_length=255)
    nik_pendiri = models.CharField(max_length=16, unique=True)
    agama_pendiri = models.CharField(max_length=50, choices=AGAMA_CHOICES)
    jenis_kelamin_pendiri = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_tanggal_lahir_pendiri = models.CharField(max_length=255)
    tanggal_lahir_pendiri = models.DateField(null=True, blank=True)
    status_perkawinan_pendiri = models.CharField(max_length=50, choices=STATUS_PERKAWINAN_CHOICES)
    alamat_pendiri = models.TextField()
    no_hp_pendiri = models.CharField(max_length=15)
    pekerjaan_pendiri = models.CharField(max_length=255)
    
    # Data Ketua
    nama_ketua = models.CharField(max_length=255)
    nik_ketua = models.CharField(max_length=16, unique=True)
    agama_ketua = models.CharField(max_length=50, choices=AGAMA_CHOICES)
    jenis_kelamin_ketua = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_tanggal_lahir_ketua = models.CharField(max_length=255)
    tanggal_lahir_ketua = models.DateField(default=timezone.now, null=True, blank=True)
    status_perkawinan_ketua = models.CharField(max_length=50, choices=STATUS_PERKAWINAN_CHOICES)
    alamat_ketua = models.TextField()
    no_hp_ketua = models.CharField(max_length=15)
    pekerjaan_ketua = models.CharField(max_length=255)

    # Data Sekretaris
    nama_sekretaris = models.CharField(max_length=255)
    nik_sekretaris = models.CharField(max_length=16, unique=True)
    agama_sekretaris = models.CharField(max_length=50, choices=AGAMA_CHOICES)
    jenis_kelamin_sekretaris = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_tanggal_lahir_sekretaris = models.CharField(max_length=255)
    tanggal_lahir_sekretaris = models.DateField(default=timezone.now, null=True, blank=True)
    status_perkawinan_sekretaris = models.CharField(max_length=50, choices=STATUS_PERKAWINAN_CHOICES)
    alamat_sekretaris = models.TextField()
    no_hp_sekretaris = models.CharField(max_length=15)
    pekerjaan_sekretaris = models.CharField(max_length=255)

    # Data Bendahara
    nama_bendahara = models.CharField(max_length=255)
    nik_bendahara = models.CharField(max_length=16, unique=True)
    agama_bendahara = models.CharField(max_length=50, choices=AGAMA_CHOICES)
    jenis_kelamin_bendahara = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES)
    tempat_tanggal_lahir_bendahara = models.CharField(max_length=255)
    tanggal_lahir_bendahara = models.DateField(default=timezone.now, null=True, blank=True)
    status_perkawinan_bendahara = models.CharField(max_length=50, choices=STATUS_PERKAWINAN_CHOICES)
    alamat_bendahara = models.TextField()
    no_hp_bendahara = models.CharField(max_length=15)
    pekerjaan_bendahara = models.CharField(max_length=255)

    def __str__(self):
        return f"Pengurus - {self.nama_pendiri}"
    


class Dokumen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register = models.ForeignKey(Register, on_delete=models.CASCADE, blank=True, null=True, related_name='dokumen')
    akta_notaris = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Akta Notaris")
    ad_art = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="AD/ART")
    program_kerja = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Program Kerja")
    struktur_organisasi = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Struktur Organisasi")
    biodata_pengurus = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Biodata Pengurus")
    foto_pengurus = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Foto Pengurus")
    ktp_pengurus = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="KTP Pengurus")
    npwp_pengurus = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="NPWP")
    surat_domisili = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Keterangan Domisili Ormas")
    surat_kepemilikan_gedung = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Kepemilikan/Kontrak Gedung")
    foto_kantor = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Foto Kantor/Sekretariat")
    surat_tidak_sengketa = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Keterangan Tidak Dalam Sengketa")
    surat_pernyataan_kesanggupan = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Pernyataan Kesanggupan Melaporkan Kegiatan")
    surat_tidak_terkait_politik = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Pernyataan Tidak Terkait Partai Politik")
    surat_pernyataan_hak_paten = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Pernyataan Hak Paten")
    surat_rekomendasi_satu = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Rekomendasi Satu")
    surat_rekomendasi_dua = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Rekomendasi Dua")
    surat_pernyataan_pejabat = models.FileField(upload_to=dokumen, blank=True, null=True, verbose_name="Surat Pernyataan Pejabat")

    def __str__(self):
        return f"Dokumen ID: {self.id}"