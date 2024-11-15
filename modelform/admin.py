from django.contrib import admin
from .models import Organisasi, Pemohon, Pengurus, Dokumen, Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['author', 'nama_organisasi', 'register', 'created_at', 'logo']

admin.site.register(Register, RegisterAdmin)

admin.site.register(Organisasi)
admin.site.register(Pemohon)
admin.site.register(Pengurus)
admin.site.register(Dokumen)

class PemohonInline(admin.TabularInline):
    model = Pemohon
    extra = 1

class OrganisasiInline(admin.TabularInline):
    model = Organisasi
    extra = 1

class PengurusInline(admin.TabularInline):
    model = Pengurus
    extra = 1

class DokumenInline(admin.TabularInline):
    model = Dokumen
    extra = 1


class RegisterAdmin(admin.ModelAdmin):
    inlines = [PemohonInline, OrganisasiInline, PengurusInline, DokumenInline]
    list_display = ('id', 'nama_organisasi', 'register', 'created_at')

# Register your models here.
