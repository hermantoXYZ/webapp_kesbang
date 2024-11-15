# skt/forms.py
from django import forms
from .models import Pemohon, Organisasi, Pengurus, Dokumen, Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['nama_organisasi', 'logo']
        widgets = {
            'nama_organisasi': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama organisasi Anda',
                'class': 'form-control',
                'required': True,
                'autofocus': True,
                
            }),
            'logo': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }


class PemohonForm(forms.ModelForm):
    jenis_kelamin = forms.ChoiceField(
        choices=[('', 'Pilih Jenis Kelamin')] + Pemohon.JENIS_KELAMIN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Jenis Kelamin'})
    )

    tanggal_lahir_pemohon = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:

        model = Pemohon
        fields = ['nama_lengkap', 'nik', 'jenis_kelamin', 'alamat', 'tempat_tanggal_lahir', 'tanggal_lahir_pemohon', 'pekerjaan', 'no_wa', 'email', 'surat_permohonan_skt', 'nomor_surat']
        widgets = {
            'surat_permohonan_skt': forms.FileInput(attrs={'accept': 'application/pdf'}),
            'nama_lengkap': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama lengkap Anda',
            }),
            'nik': forms.TextInput(attrs={
                'placeholder': 'Masukkan NIK Anda',
            }),
            'alamat': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat Anda',
            }),
            'tempat_tanggal_lahir': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat dan tanggal lahir Anda',
            }),
            
            'pekerjaan': forms.TextInput(attrs={
                'placeholder': 'Masukkan pekerjaan Anda',
            }),
            'no_wa': forms.TextInput(attrs={
                'placeholder': 'Masukkan nomor WhatsApp Anda',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Masukkan email Anda',
            }),
            'nomor_surat': forms.TextInput(attrs={
                'placeholder': 'Masukkan nomor surat Anda',
            })
        }

class OrganisasiForm(forms.ModelForm):

    tanggal_akta =  forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tanggal_pendirian =  forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = Organisasi
        fields = ['nama_notaris', 'nomor_akta', 'tanggal_akta', 'nama_organisasi', 'bidang_kegiatan', 'alamat_kantor', 'tempat_pendirian', 'tanggal_pendirian', 'asas_ciri_organisasi', 'tujuan_organisasi', 'masa_bakti_kepengurusan', 'keputusan_tertinggi_organisasi', 'unit_cabang', 'npwp', 'sumber_keuangan', 'lambang_logo', 'bendera']
        widgets = {
            'nama_notaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama notaris Anda',
            }),
            'nomor_akta': forms.TextInput(attrs={
                'placeholder': 'Masukkan nomor akta Anda',
            }),
            'nama_organisasi': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama organisasi Anda',
            }),
            'bidang_kegiatan': forms.TextInput(attrs={
                'placeholder': 'Masukkan bidang kegiatan Anda',
            }),
            'alamat_kantor': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat kantor Anda',
            }),
            'tempat_pendirian': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat pendirian Anda',
            }),
            'asas_ciri_organisasi': forms.Textarea(attrs={
                'placeholder': 'Masukkan asas ciri organisasi Anda',
            }),
            'tujuan_organisasi': forms.Textarea(attrs={
                'placeholder': 'Masukkan tujuan organisasi Anda',
            }),
            'masa_bakti_kepengurusan': forms.Textarea(attrs={
                'placeholder': 'Masukkan masa bakti kepengurusan Anda',
            }),
            'keputusan_tertinggi_organisasi': forms.Textarea(attrs={
                'placeholder': 'Masukkan keputusan tertinggi organisasi Anda',
            }),
            'unit_cabang': forms.Textarea(attrs={
                'placeholder': 'Masukkan unit cabang Anda',
            }),
            'npwp': forms.TextInput(attrs={
                'placeholder': 'Masukkan NPWP Anda',
            }),
            'sumber_keuangan': forms.TextInput(attrs={
                'placeholder': 'Masukkan sumber keuangan Anda',
            }),
            'lambang_logo': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
            'bendera': forms.FileInput(attrs={
                'accept': 'image/*',
            })
        }

class PengurusForm(forms.ModelForm):
    # Jenis Kelamin
    jenis_kelamin_pendiri = forms.ChoiceField(
        choices=[('', 'Pilih Jenis Kelamin')] + Pengurus.JENIS_KELAMIN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Jenis Kelamin'})
    )
    jenis_kelamin_ketua = forms.ChoiceField(
        choices=[('', 'Pilih Jenis Kelamin')] + Pengurus.JENIS_KELAMIN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Jenis Kelamin'})
    )
    jenis_kelamin_sekretaris = forms.ChoiceField(
        choices=[('', 'Pilih Jenis Kelamin')] + Pengurus.JENIS_KELAMIN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Jenis Kelamin'})
    )
    jenis_kelamin_bendahara = forms.ChoiceField(
        choices=[('', 'Pilih Jenis Kelamin')] + Pengurus.JENIS_KELAMIN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Jenis Kelamin'})
    )
    # Status Perkawinan
    status_perkawinan_pendiri = forms.ChoiceField(
        choices=[('', 'Pilih Status Perkawinan')] + Pengurus.STATUS_PERKAWINAN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Status Perkawinan'})
    )
    status_perkawinan_ketua = forms.ChoiceField(
        choices=[('', 'Pilih Status Perkawinan')] + Pengurus.STATUS_PERKAWINAN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Status Perkawinan'})
    )
    status_perkawinan_sekretaris = forms.ChoiceField(
        choices=[('', 'Pilih Status Perkawinan')] + Pengurus.STATUS_PERKAWINAN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Status Perkawinan'})
    )
    status_perkawinan_bendahara = forms.ChoiceField(
        choices=[('', 'Pilih Status Perkawinan')] + Pengurus.STATUS_PERKAWINAN_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Status Perkawinan'})
    )
    # Status Agama
    agama_pendiri = forms.ChoiceField(
        choices=[('', 'Pilih Agama')] + Pengurus.AGAMA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Agama'})
    )
    agama_ketua = forms.ChoiceField(
        choices=[('', 'Pilih Agama')] + Pengurus.AGAMA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Agama'})
    )
    agama_sekretaris = forms.ChoiceField(
        choices=[('', 'Pilih Agama')] + Pengurus.AGAMA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Agama'})
    )
    agama_bendahara = forms.ChoiceField(
        choices=[('', 'Pilih Agama')] + Pengurus.AGAMA_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Pilih Agama'})
    )
    tanggal_lahir_pendiri = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tanggal_lahir_ketua = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tanggal_lahir_sekretaris = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tanggal_lahir_bendahara = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    widgets = dict(
        tanggal_lahir_pendiri = forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'Masukkan tanggal lahir pendiri',
            }
        )
        )
    class Meta:
        model = Pengurus
        fields = ['nama_pembina', 'nama_penasehat', 'nama_pendiri', 'nik_pendiri', 'agama_pendiri', 'jenis_kelamin_pendiri', 'tempat_tanggal_lahir_pendiri', 'tanggal_lahir_pendiri', 'status_perkawinan_pendiri', 'alamat_pendiri', 'no_hp_pendiri', 'pekerjaan_pendiri', 'nama_ketua', 'nik_ketua', 'agama_ketua', 'jenis_kelamin_ketua', 'tempat_tanggal_lahir_ketua', 'tanggal_lahir_ketua','status_perkawinan_ketua', 'alamat_ketua', 'no_hp_ketua', 'pekerjaan_ketua', 'nama_sekretaris', 'nik_sekretaris', 'agama_sekretaris', 'jenis_kelamin_sekretaris','tempat_tanggal_lahir_sekretaris', 'tanggal_lahir_sekretaris', 'status_perkawinan_sekretaris', 'alamat_sekretaris', 'no_hp_sekretaris', 'pekerjaan_sekretaris', 'nama_bendahara', 'nik_bendahara', 'agama_bendahara', 'jenis_kelamin_bendahara', 'tempat_tanggal_lahir_bendahara', 'tanggal_lahir_bendahara', 'status_perkawinan_bendahara', 'alamat_bendahara', 'no_hp_bendahara', 'pekerjaan_bendahara']
        widgets = {
            'nama_pembina': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama pembina Anda',
            }),
            'nama_penasehat': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama penasehat Anda',
            }),            
            'nama_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama pendiri Anda',
            }),
            'nik_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan NIK pendiri Anda',
            }),
            'agama_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan agama pendiri Anda',
            }),
            'jenis_kelamin_pendiri': forms.Select(attrs={
                'placeholder': 'Masukkan jenis kelamin pendiri Anda',
            }),
            'tempat_tanggal_lahir_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat tanggal lahir pendiri Anda',
            }),
            'tanggal_lahir_pendiri': forms.DateInput(attrs={
                'placeholder': 'Masukkan tanggal lahir pendiri Anda',
            }),
            'status_perkawinan_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan status perkawinan pendiri Anda',
            }),
            'alamat_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat pendiri Anda',
            }),
            'no_hp_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan no hp pendiri Anda',
            }),
            'pekerjaan_pendiri': forms.TextInput(attrs={
                'placeholder': 'Masukkan pekerjaan pendiri Anda',
            }),
            'nama_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama ketua Anda',
            }),
            'nik_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan NIK ketua Anda',
            }),
            'agama_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan agama ketua Anda',
            }),
            'jenis_kelamin_ketua': forms.Select(attrs={
                'placeholder': 'Masukkan jenis kelamin ketua Anda',            
            }),            
            'tempat_tanggal_lahir_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat tanggal lahir ketua Anda',
            }),
            'tanggal_lahir_ketua': forms.DateInput(attrs={
                'placeholder': 'Masukkan tanggal lahir ketua Anda',
            }),
            'status_perkawinan_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan status perkawinan ketua Anda',
            }),
            'alamat_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat ketua Anda',
            }),
            'no_hp_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan no hp ketua Anda',
            }),
            'pekerjaan_ketua': forms.TextInput(attrs={
                'placeholder': 'Masukkan pekerjaan ketua Anda',
            }),
            'nama_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama sekretaris Anda',
            }),
            'nik_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan NIK sekretaris Anda',
            }),
            'agama_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan agama sekretaris Anda',
            }),
            'jenis_kelamin_sekretaris': forms.Select(attrs={
                'placeholder': 'Masukkan jenis kelamin sekretaris Anda',            
            }),            
            'tempat_tanggal_lahir_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat tanggal lahir sekretaris Anda',
            }),
            'status_perkawinan_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan status perkawinan sekretaris Anda',
            }),
            'alamat_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat sekretaris Anda',
            }),
            'no_hp_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan no hp sekretaris Anda',
            }),
            'pekerjaan_sekretaris': forms.TextInput(attrs={
                'placeholder': 'Masukkan pekerjaan sekretaris Anda',
            }),
            'nama_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan nama bendahara Anda',
            }),
            'nik_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan NIK bendahara Anda',
            }),
            'agama_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan agama bendahara Anda',
            }),
            'jenis_kelamin_bendahara': forms.Select(attrs={
                'placeholder': 'Masukkan jenis kelamin bendahara Anda',            
            }),            
            'tempat_tanggal_lahir_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan tempat tanggal lahir bendahara Anda',
            }),
            'tanggal_lahir_bendahara': forms.DateInput(attrs={
                'placeholder': 'Masukkan tanggal lahir bendahara Anda',
            }),
            'status_perkawinan_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan status perkawinan bendahara Anda',
            }),
            'alamat_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan alamat bendahara Anda',
            }),
            'no_hp_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan no hp bendahara Anda',
            }),
            'pekerjaan_bendahara': forms.TextInput(attrs={
                'placeholder': 'Masukkan pekerjaan bendahara Anda',
            }),
        }

class AktaNotarisForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['akta_notaris']

class AdArtForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['ad_art']

class ProgramKerjaForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['program_kerja']

class StrukturOrganisasiForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['struktur_organisasi']

class BiodataPengurusForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['biodata_pengurus']

class FotoPengurusForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['foto_pengurus']

class KtpPengurusForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['ktp_pengurus']

class NpwpPengurusForm(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['npwp_pengurus']

class SuratDomisiliForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_domisili']

class SuratKepemilikanGedungForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_kepemilikan_gedung']

class FotoKantorForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['foto_kantor']

class SuratTidakSengketaForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_tidak_sengketa']

class SuratPernyataanKesanggupanForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_pernyataan_kesanggupan']

class SuratTidakTerkaitPolitikForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_tidak_terkait_politik']

class SuratPernyataanHakPatenForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_pernyataan_hak_paten']

class SuratRekomendasiSatuForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_rekomendasi_satu']

class SuratRekomendasiDuaForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_rekomendasi_dua']



class SuratPernyataanPejabatForm(forms.ModelForm):    
    class Meta:
        model = Dokumen
        fields = ['surat_pernyataan_pejabat']
        
        

    