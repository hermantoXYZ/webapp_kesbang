
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from . forms import PemohonForm, RegisterForm, OrganisasiForm, PengurusForm, AktaNotarisForm, AdArtForm, ProgramKerjaForm, StrukturOrganisasiForm, BiodataPengurusForm, FotoPengurusForm, KtpPengurusForm, NpwpPengurusForm, SuratDomisiliForm, SuratKepemilikanGedungForm, FotoKantorForm, SuratTidakSengketaForm, SuratPernyataanKesanggupanForm, SuratTidakTerkaitPolitikForm, SuratPernyataanHakPatenForm, SuratRekomendasiSatuForm, SuratRekomendasiDuaForm, SuratPernyataanPejabatForm
from .models import Dokumen, Organisasi, Pemohon, Pengurus, Register
from accounts.forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from uuid import UUID
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q 


def is_pelanggan(user):
    return user.is_authenticated and user.is_pelanggan

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'dashboard/profile.html', {'form': form})


@user_passes_test(is_pelanggan)
def dashboard_profile(request):
    user = request.user
    return render(request, 'dashboard/profile.html', {'user': user})


@user_passes_test(is_pelanggan)
def pelanggan(request):
    user = request.user

    context = {
        'user': user,
        'register': Register.objects.all(),
    }
    return render(request, 'dashboard/pelanggan.html', context)


@user_passes_test(is_pelanggan)
def pemohon(request):
    if request.method == 'POST':
        form = PemohonForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the Pemohon instance with a link to the logged-in user
            pemohon = form.save(commit=False)
            pemohon.user = request.user  # Assign the user field
            pemohon.save()  # Save the instance to the database
            
            # Return a JSON response with relevant fields from the Pemohon instance
            return JsonResponse({
                'message': 'Pemohon submitted successfully.',
                'status': 'success',
                'id': pemohon.id,   
                'register': pemohon.register.id,
                'name': pemohon.nama_lengkap,
                'nik': pemohon.nik,
                'jenis_kelamin': pemohon.jenis_kelamin,
                'alamat': pemohon.alamat,
                'tempat_tanggal_lahir': pemohon.tempat_tanggal_lahir,
                'pekerjaan': pemohon.pekerjaan,
                'no_wa': pemohon.no_wa,
                'email': pemohon.email,
                'surat_permohonan_skt': pemohon.surat_permohonan_skt.url,
                'nomor_surat': pemohon.nomor_surat,
            })
        else:
            # Return form errors if the form is invalid
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    else:
        form = PemohonForm()
    
    return render(request, 'dashboard/pemohon.html', {'form': form})


@user_passes_test(is_pelanggan)
def create_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            register = form.save(commit=False)  # Save the form without committing to the database yet
            register.author = request.user  # Set the author to the current logged-in user
            register.save()  # Now save the form data to the database
            return redirect('register_list')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register_skt.html', {'form': form})


@user_passes_test(is_pelanggan)
def register_list(request):
    query = request.GET.get('q', '')
    results = Register.objects.filter(author=request.user)

    try:
        register_id = request.GET.get('register_id')
        if register_id:
            register_id = UUID(register_id)  # Verifikasi jika register_id adalah UUID yang valid
        registers = Register.objects.all()  # Ambil data yang sesuai

    except ValueError:
        # Jika register_id tidak valid UUID, bisa mengarahkan ke halaman error
        return redirect('error_page')
    

    if query:
        results = results.filter(
            Q(nama_organisasi__icontains=query) | Q(register__icontains=query)
        )



    return render(request, 'dashboard/register_list.html', {'registers': registers, 'results': results, 'query': query})


def dashboard_terverifikasi (request):
    results = Register.objects.filter(is_verified=True)
    total_pengajuan = Register.objects.all().count()
    total_verified = results.count()
    unverified_completed_count = Register.objects.filter(is_completed=True, is_verified=False).count()
    query = request.GET.get('q', '')

    try:
        register_id = request.GET.get('register_id')
        if register_id:
            register_id = UUID(register_id)  # Verifikasi jika register_id adalah UUID yang valid
        registers = Register.objects.all()  # Ambil data yang sesuai

    except ValueError:
        # Jika register_id tidak valid UUID, bisa mengarahkan ke halaman error
        return redirect('error_page')

    if query:
        results = results.filter(
            Q(nama_organisasi__icontains=query) | Q(register__icontains=query)
        )

    context = {
        'results': results,
        'total_verified': total_verified,
        'unverified_completed_count': unverified_completed_count,
        'query': query,
        'registers': registers,
        'total_pengajuan': total_pengajuan
    }

    
    return render(request, 'dashboard/dashboard_terverifikasi.html', context)

# modelform/views.py

def dashboard_unverified(request):
    results = Register.objects.filter(is_verified=False, is_completed=True)
    results_verified = Register.objects.filter(is_verified=True)
    total_pengajuan = Register.objects.all().count()
    total_verified = results_verified.count()
    unverified_completed_count = Register.objects.filter(is_completed=True, is_verified=False).count()
    query = request.GET.get('q', '')

    try:
        register_id = request.GET.get('register_id')
        if register_id:
            register_id = UUID(register_id)  # Verifikasi jika register_id adalah UUID yang valid
        registers = Register.objects.all()  # Ambil data yang sesuai

    except ValueError:
        # Jika register_id tidak valid UUID, bisa mengarahkan ke halaman error
        return redirect('error_page')

    if query:
        results = results.filter(
            Q(nama_organisasi__icontains=query) | Q(register__icontains=query)
        )


    context = {
        'results': results,
        'total_verified': total_verified,
        'total_pengajuan': total_pengajuan,
        'unverified_completed_count': unverified_completed_count,
        'query': query,
        'registers': registers
    }

    return render(request, 'dashboard/dashboard_unverified.html', context)

def resume_page(request, register_id):
    register = get_object_or_404(Register, id=register_id)

    try:
        pengurus = register.pengurus.get()
    except Pengurus.DoesNotExist:
        messages.warning(request, "Silakan lengkapi data terlebih dahulu.")
        return redirect('edit_pengurus', register_id=register_id)

    is_editable = not register.is_completed

    pemohon = register.pemohon.first() if register.pemohon.exists() else None
    organisasi = register.organisasi.first() if register.organisasi.exists() else None
    pengurus = register.pengurus.first() if register.pengurus.exists() else None
    dokumen = register.dokumen.first() if register.dokumen.exists() else None

    surat_permohonan_skt = pemohon.surat_permohonan_skt if pemohon else None
    bendera = organisasi.bendera if organisasi else None
    lambang_logo = organisasi.lambang_logo if organisasi else None
    

    akta_notaris = dokumen.akta_notaris if dokumen else None
    ad_art = dokumen.ad_art if dokumen else None
    program_kerja = dokumen.program_kerja if dokumen else None
    struktur_organisasi = dokumen.struktur_organisasi if dokumen else None
    biodata_pengurus = dokumen.biodata_pengurus if dokumen else None
    foto_pengurus = dokumen.foto_pengurus if dokumen else None
    ktp_pengurus = dokumen.ktp_pengurus if dokumen else None
    npwp_pengurus = dokumen.npwp_pengurus if dokumen else None
    surat_domisili = dokumen.surat_domisili if dokumen else None
    surat_kepemilikan_gedung = dokumen.surat_kepemilikan_gedung if dokumen else None
    foto_kantor = dokumen.foto_kantor if dokumen else None
    surat_tidak_sengketa = dokumen.surat_tidak_sengketa if dokumen else None
    surat_pernyataan_kesanggupan = dokumen.surat_pernyataan_kesanggupan if dokumen else None
    surat_tidak_terkait_politik = dokumen.surat_tidak_terkait_politik if dokumen else None
    surat_pernyataan_hak_paten = dokumen.surat_pernyataan_hak_paten if dokumen else None
    surat_rekomendasi_satu = dokumen.surat_rekomendasi_satu if dokumen else None
    surat_rekomendasi_dua = dokumen.surat_rekomendasi_dua if dokumen else None
    surat_pernyataan_pejabat = dokumen.surat_pernyataan_pejabat if dokumen else None


    # Display the message if the register is not verified
    if register.is_verified:
        messages.success(request, "Permohonan anda berhasil, silahkan menunggu konfirmasi selanjutnya.")
   

    if request.method == 'POST':
        if not register.is_completed:
            # Ubah status is_completed menjadi True
            register.is_completed = True
            register.save()
            messages.success(request, "Pendaftaran telah berhasil diakhiri.")
        else:
            messages.error(request, "Pendaftaran sudah diakhiri sebelumnya dan tidak dapat diubah lagi.")

        # Redirect ke halaman resume setelah pengakhiran pendaftaran
        return redirect('resume_page', register_id=register.id)

    context = {
        
        'surat_permohonan_skt' : surat_permohonan_skt,
        'bendera' : bendera,
        'lambang_logo': lambang_logo,

        'register': register,
        'pemohon': pemohon,
        'organisasi': organisasi,
        'pengurus': pengurus,
        'dokumen': dokumen,
        'register_id': register_id,
        'akta_notaris': akta_notaris,
        'ad_art': ad_art,
        'program_kerja': program_kerja,
        'struktur_organisasi': struktur_organisasi,
        'biodata_pengurus': biodata_pengurus,
        'foto_pengurus': foto_pengurus,
        'ktp_pengurus': ktp_pengurus,
        'npwp_pengurus': npwp_pengurus,
        'surat_domisili': surat_domisili,
        'surat_kepemilikan_gedung': surat_kepemilikan_gedung,
        'foto_kantor': foto_kantor,
        'surat_tidak_sengketa': surat_tidak_sengketa,
        'surat_pernyataan_kesanggupan': surat_pernyataan_kesanggupan,
        'surat_tidak_terkait_politik': surat_tidak_terkait_politik,
        'surat_pernyataan_hak_paten': surat_pernyataan_hak_paten,
        'surat_rekomendasi_satu': surat_rekomendasi_satu,
        'surat_rekomendasi_dua': surat_rekomendasi_dua,
        'surat_pernyataan_pejabat': surat_pernyataan_pejabat,

        'is_editable': is_editable
    }

    return render(request, 'dashboard/resume_page.html', context)


# PAGE FORMULIR PEMOHON
@user_passes_test(is_pelanggan)
def edit_pemohon(request, register_id):  # register_id is now a UUID
    register = get_object_or_404(Register, id=register_id)

    if register.is_completed:
        messages.warning(request, "Pendaftaran sudah diakhiri, Anda tidak dapat mengedit data lagi.")
        return redirect(reverse('resume_page', args=[register_id])) # Redirect ke halaman lain jika diperlukan

    if request.method == 'POST':
        pemohon_instance = register.pemohon.first() if register.pemohon.exists() else None
        pemohon_form = PemohonForm(request.POST, request.FILES, instance=pemohon_instance)
        
        
        if pemohon_form.is_valid():
            pemohon = pemohon_form.save(commit=False)
            pemohon.register = register  # Set the related Register instance
            pemohon.save()
            return redirect(reverse('edit_organisasi', args=[register_id]))
    else:
        pemohon_instance = register.pemohon.first() if register.pemohon.exists() else None
        pemohon_form = PemohonForm(instance=pemohon_instance)
        print(pemohon_form.errors)

    return render(request, 'dashboard/edit_pemohon.html', {
        'pemohon_form': pemohon_form,
        'register_id': register_id,
    })

# PAGE FORMULIR ORGANISASI
@user_passes_test(is_pelanggan)
def edit_organisasi(request, register_id):  # register_id is now a UUID
    register = get_object_or_404(Register, id=register_id)

    if register.is_completed:
        messages.warning(request, "Pendaftaran sudah diakhiri, Anda tidak dapat mengedit data lagi.")
        return redirect(reverse('resume_page', args=[register_id])) # Redirect ke halaman lain jika diperlukan


# CARA USER TIDAK BISA LANJUT SEBELUM ISI FORM PEMOHON
    try:
        pemohon = register.pemohon.get()  
    except Pemohon.DoesNotExist:
        messages.warning(request, "Silakan lengkapi data Pemohon terlebih dahulu.")
        return redirect('edit_pemohon', register_id=register_id)
# CARA USER TIDAK BISA LANJUT SEBELUM ISI FORM PEMOHON


    if request.method == 'POST':
        organisasi_instance = register.organisasi.first() if register.organisasi.exists() else None
        organisasi_form = OrganisasiForm(request.POST, request.FILES, instance=organisasi_instance)
        
        if organisasi_form.is_valid():
            organisasi = organisasi_form.save(commit=False)
            organisasi.register = register  # Set the related Register instance
            organisasi.save()
            return redirect(reverse('edit_pengurus', args=[register_id]))
    else:
        organisasi_instance = register.organisasi.first() if register.organisasi.exists() else None
        organisasi_form = OrganisasiForm(instance=organisasi_instance)

    return render(request, 'dashboard/edit_organisasi.html', {
        'organisasi_form': organisasi_form,
        'register_id': register_id,
    })

# PAGE FORMULIR PENGURUS
@user_passes_test(is_pelanggan)
def edit_pengurus(request, register_id):  # register_id is now a UUID
    register = get_object_or_404(Register, id=register_id)

    if register.is_completed:
        messages.warning(request, "Pendaftaran sudah diakhiri, Anda tidak dapat mengedit data lagi.")
        return redirect(reverse('resume_page', args=[register_id])) # Redirect ke halaman lain jika diperlukan

    try:
        organisasi = register.organisasi.get()  
    except Organisasi.DoesNotExist:
        messages.warning(request, "Silakan lengkapi data Organisasi terlebih dahulu.")
        return redirect('edit_organisasi', register_id=register_id)
    
    

    if request.method == 'POST':
        pengurus_instance = register.pengurus.first() if register.pengurus.exists() else None
        pengurus_form = PengurusForm(request.POST, instance=pengurus_instance)
        
        if pengurus_form.is_valid():
            pengurus = pengurus_form.save(commit=False)
            pengurus.register = register  # Set the related Register instance
            pengurus.save()
            return redirect(reverse('edit_dokumen', args=[register_id]))
        else:
            messages.error(request, 'Form is not valid')
    else:
        pengurus_instance = register.pengurus.first() if register.pengurus.exists() else None
        pengurus_form = PengurusForm(instance=pengurus_instance)

    return render(request, 'dashboard/edit_pengurus.html', {
        'pengurus_form': pengurus_form,
        'register_id': register_id,
    })


# # PAGE FORMULIR DOKUMEN
# @user_passes_test(is_pelanggan)
# def edit_dokumen(request, register_id):
#     register = get_object_or_404(Register, id=register_id)
#     dokumen_instance = register.dokumen.first() if register.dokumen.exists() else Dokumen.objects.create(register=register)

#     if request.method == 'POST':
#         akta_notaris_form = AktaNotarisForm(request.POST, request.FILES, instance=dokumen_instance)


#         if akta_notaris_form.is_valid():
#             instance = akta_notaris_form.save(commit=False)
#             instance.register = dokumen_instance.register
#             instance.save()
#             return JsonResponse({
#                 'message': 'Akta Notaris updated successfully.',
#                 'akta_notaris_url': instance.akta_notaris.url if instance.akta_notaris else None,
#             })
#         else:
#             return JsonResponse({'errors': akta_notaris_form.errors.as_json()}, status=400)
        
#     else:

#         akta_notaris_form = AktaNotarisForm(instance=dokumen_instance)

#     return render(request, 'dashboard/edit_dokumen.html', {
#         'akta_notaris_form': akta_notaris_form,
#     })


@user_passes_test(is_pelanggan)
def edit_dokumen(request, register_id):
    register = get_object_or_404(Register, id=register_id)
    dokumen_instance = register.dokumen.first() if register.dokumen.exists() else Dokumen.objects.create(register=register)
   
    if register.is_completed:
        messages.warning(request, "Pendaftaran sudah diakhiri, Anda tidak dapat mengedit data lagi.")
        return redirect(reverse('resume_page', args=[register_id])) # Redirect ke halaman lain jika diperlukan
    

    try :
        pengurus = register.pengurus.get()  
    except Pengurus.DoesNotExist:
        messages.warning(request, "Silakan lengkapi data Pengurus terlebih dahulu.")
        return redirect('edit_pengurus', register_id=register_id)

    if request.method == 'POST':
        # Initialize both forms with POST data and files
        akta_notaris_form = AktaNotarisForm(request.POST, request.FILES, instance=dokumen_instance)
        ad_art_form = AdArtForm(request.POST, request.FILES, instance=dokumen_instance)
        program_kerja_form = ProgramKerjaForm(request.POST, request.FILES, instance=dokumen_instance)
        struktur_organisasi_form = StrukturOrganisasiForm(request.POST, request.FILES, instance=dokumen_instance)
        biodata_pengurus_form = BiodataPengurusForm(request.POST, request.FILES, instance=dokumen_instance)
        foto_pengurus_form = FotoPengurusForm(request.POST, request.FILES, instance=dokumen_instance)
        ktp_pengurus_form = KtpPengurusForm(request.POST, request.FILES, instance=dokumen_instance)
        npwp_pengurus_form = NpwpPengurusForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_domisili_form = SuratDomisiliForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_kepemilikan_gedung_form = SuratKepemilikanGedungForm(request.POST, request.FILES, instance=dokumen_instance)
        foto_kantor_form = FotoKantorForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_tidak_sengketa_form = SuratTidakSengketaForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_pernyataan_kesanggupan_form = SuratPernyataanKesanggupanForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_tidak_terkait_politik_form = SuratTidakTerkaitPolitikForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_pernyataan_hak_paten_form = SuratPernyataanHakPatenForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_rekomendasi_satu_form = SuratRekomendasiSatuForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_rekomendasi_dua_form = SuratRekomendasiDuaForm(request.POST, request.FILES, instance=dokumen_instance)
        surat_pernyataan_pejabat_form = SuratPernyataanPejabatForm(request.POST, request.FILES, instance=dokumen_instance)


        if akta_notaris_form.is_valid() and ad_art_form.is_valid():
            # Save AktaNotarisForm
            akta_notaris_instance = akta_notaris_form.save(commit=False)
            akta_notaris_instance.register = dokumen_instance.register
            akta_notaris_instance.save()

            # Save AdArtForm
            ad_art_instance = ad_art_form.save(commit=False)
            ad_art_instance.register = dokumen_instance.register
            ad_art_instance.save()

            # Save ProgramKerjaForm
            program_kerja_instance = program_kerja_form.save(commit=False)
            program_kerja_instance.register = dokumen_instance.register
            program_kerja_instance.save()

            # Save the StrukturOrganisasiForm
            struktur_organisasi_instance = struktur_organisasi_form.save(commit=False)
            struktur_organisasi_instance.register = dokumen_instance.register
            struktur_organisasi_instance.save()

            # Save the BiodataForm
            biodata_pengurus_instance = biodata_pengurus_form.save(commit=False)
            biodata_pengurus_instance.register = dokumen_instance.register
            biodata_pengurus_instance.save()

            # Save the FotoPengurusForm
            foto_pengurus_instance = foto_pengurus_form.save(commit=False)
            foto_pengurus_instance.register = dokumen_instance.register
            foto_pengurus_instance.save()

            # Save the KtpPengurusForm
            ktp_pengurus_instance = ktp_pengurus_form.save(commit=False)
            ktp_pengurus_instance.register = dokumen_instance.register
            ktp_pengurus_instance.save()

            # Save the NpwpForm
            npwp_pengurus_instance = npwp_pengurus_form.save(commit=False)
            npwp_pengurus_instance.register = dokumen_instance.register
            npwp_pengurus_instance.save()


            # Save the SuratDomisiliForm
            surat_domisili_instance = surat_domisili_form.save(commit=False)
            surat_domisili_instance.register = dokumen_instance.register
            surat_domisili_instance.save()

            # Save the SuratKepemilikanGedungForm
            surat_kepemilikan_gedung_instance = surat_kepemilikan_gedung_form.save(commit=False)
            surat_kepemilikan_gedung_instance.register = dokumen_instance.register
            surat_kepemilikan_gedung_instance.save()

            # Save the FotoKantorForm
            foto_kantor_instance = foto_kantor_form.save(commit=False)
            foto_kantor_instance.register = dokumen_instance.register
            foto_kantor_instance.save()

            # Save the SuratTidakSengketaForm
            surat_tidak_sengketa_instance = surat_tidak_sengketa_form.save(commit=False)
            surat_tidak_sengketa_instance.register = dokumen_instance.register
            surat_tidak_sengketa_instance.save()

            # Save the SuratPernyataanKesanggupanForm
            surat_pernyataan_kesanggupan_instance = surat_pernyataan_kesanggupan_form.save(commit=False)
            surat_pernyataan_kesanggupan_instance.register = dokumen_instance.register
            surat_pernyataan_kesanggupan_instance.save()

            # Save the SuratTidakTerkaitPolitikForm
            surat_tidak_terkait_politik_instance = surat_tidak_terkait_politik_form.save(commit=False)
            surat_tidak_terkait_politik_instance.register = dokumen_instance.register
            surat_tidak_terkait_politik_instance.save()

            # Save the SuratPernyataanHakPatenForm
            surat_pernyataan_hak_paten_instance = surat_pernyataan_hak_paten_form.save(commit=False)
            surat_pernyataan_hak_paten_instance.register = dokumen_instance.register
            surat_pernyataan_hak_paten_instance.save()

            # Save the SuratRekomendasiSatuForm
            surat_rekomendasi_satu_instance = surat_rekomendasi_satu_form.save(commit=False)
            surat_rekomendasi_satu_instance.register = dokumen_instance.register
            surat_rekomendasi_satu_instance.save()

            # Save the SuratRekomendasiDuaForm
            surat_rekomendasi_dua_instance = surat_rekomendasi_dua_form.save(commit=False)
            surat_rekomendasi_dua_instance.register = dokumen_instance.register
            surat_rekomendasi_dua_instance.save()

            # Save the SuratPernyataanPejabat
            surat_pernyataan_pejabat_instance = surat_pernyataan_pejabat_form.save(commit=False)
            surat_pernyataan_pejabat_instance.register = dokumen_instance.register
            surat_pernyataan_pejabat_instance.save()

            messages.success(request, "Documents updated successfully.")

            # return JsonResponse({
            #     'message': 'Documents updated successfully.',
            #     'akta_notaris_url': akta_notaris_instance.akta_notaris.url if akta_notaris_instance.akta_notaris else None,
            #     'ad_art_url': ad_art_instance.ad_art.url if ad_art_instance.ad_art else None,
            #     'program_kerja_url': program_kerja_instance.program_kerja.url if program_kerja_instance.program_kerja else None,
            #     'struktur_organisasi_url': struktur_organisasi_instance.struktur_organisasi.url if struktur_organisasi_instance.struktur_organisasi else None,
            #     'biodata_pengurus_url': biodata_pengurus_instance.biodata_pengurus.url if biodata_pengurus_instance.biodata_pengurus else None,
            #     'foto_pengurus_url': foto_pengurus_instance.foto_pengurus.url if foto_pengurus_instance.foto_pengurus else None,
            #     'ktp_pengurus_url': ktp_pengurus_instance.ktp_pengurus.url if ktp_pengurus_instance.ktp_pengurus else None,
            #     'npwp_pengurus_url': npwp_pengurus_instance.npwp_pengurus.url if npwp_pengurus_instance.npwp_pengurus else None,
            #     'surat_domisili_url': surat_domisili_instance.surat_domisili.url if surat_domisili_instance.surat_domisili else None,
            #     'surat_kepemilikan_gedung_url': surat_kepemilikan_gedung_instance.surat_kepemilikan_gedung.url if surat_kepemilikan_gedung_instance.surat_kepemilikan_gedung else None,
            #     'fotos_kantor_url': foto_kantor_instance.foto_kantor.url if foto_kantor_instance.foto_kantor else None,
            #     'surat_tidak_sengketa_url': surat_tidak_sengketa_instance.surat_tidak_sengketa.url if surat_tidak_sengketa_instance.surat_tidak_sengketa else None,
            #     'surat_pernyataan_kesanggupan_url': surat_pernyataan_kesanggupan_instance.surat_pernyataan_kesanggupan.url if surat_pernyataan_kesanggupan_instance.surat_pernyataan_kesanggupan else None,
            #     'surat_tidak_terkait_politik_url': surat_tidak_terkait_politik_instance.surat_tidak_terkait_politik.url if surat_tidak_terkait_politik_instance.surat_tidak_terkait_politik else None,
            #     'surat_pernyataan_hak_paten_url': surat_pernyataan_hak_paten_instance.surat_pernyataan_hak_paten.url if surat_pernyataan_hak_paten_instance.surat_pernyataan_hak_paten else None,
            #     'surat_rekomendasi_satu_url': surat_rekomendasi_satu_instance.surat_rekomendasi_satu.url if surat_rekomendasi_satu_instance.surat_rekomendasi_satu else None,
            #     'surat_rekomendasi_dua_url': surat_rekomendasi_dua_instance.surat_rekomendasi_dua.url if surat_rekomendasi_dua_instance.surat_rekomendasi_dua else None,
            #     'surat_pernyataan_pejabat_url': surat_pernyataan_pejabat_instance.surat_pernyataan_pejabat.url if surat_pernyataan_pejabat_instance.surat_pernyataan_pejabat else None



            # })
        else:
            # Handle form errors
            # messages.error(request, "There was an error in the form submission. Please check the fields and try again.")
            messages.error(request, "There was an error in the form submission. Please check the fields and try again.")
            # Combine errors from both forms
            # errors = {
            #     'akta_notaris_errors': akta_notaris_form.errors.as_json(),
            #     'ad_art_errors': ad_art_form.errors.as_json(),
            #     'program_kerja_errors': program_kerja_form.errors.as_json(),
            #     'struktur_organisasi_errors': struktur_organisasi_form.errors.as_json(),
            #     'biodata_pengurus_errors': biodata_pengurus_form.errors.as_json(),
            #     'foto_pengurus_errors': foto_pengurus_form.errors.as_json(),
            #     'ktp_pengurus_errors': ktp_pengurus_form.errors.as_json(),
            #     'npwp_pengurus_errors': npwp_pengurus_form.errors.as_json(),
            #     'surat_domisili_errors': surat_domisili_form.errors.as_json(),
            #     'surat_kepemilikan_gedung_errors': surat_kepemilikan_gedung_form.errors.as_json(),
            #     'fotos_kantor_errors': foto_kantor_form.errors.as_json(),
            #     'surat_tidak_sengketa_errors': surat_tidak_sengketa_form.errors.as_json(),
            #     'surat_pernyataan_kesanggupan_errors': surat_pernyataan_kesanggupan_form.errors.as_json(),
            #     'surat_tidak_terkait_politik_errors': surat_tidak_terkait_politik_form.errors.as_json(),
            #     'surat_pernyataan_hak_paten_errors': surat_pernyataan_hak_paten_form.errors.as_json(),
            #     'surat_rekomendasi_satu_errors': surat_rekomendasi_satu_form.errors.as_json(),
            #     'surat_rekomendasi_dua_errors': surat_rekomendasi_dua_form.errors.as_json(),
            #     'surat_pernyataan_pejabat_errors': surat_pernyataan_pejabat_form.errors.as_json(),
            # }
            # return JsonResponse({'errors': errors}, status=400)
    else:
        # Initialize forms with existing instances for a GET request
        akta_notaris_form = AktaNotarisForm(instance=dokumen_instance)
        ad_art_form = AdArtForm(instance=dokumen_instance)
        program_kerja_form = ProgramKerjaForm(instance=dokumen_instance)
        struktur_organisasi_form = StrukturOrganisasiForm(instance=dokumen_instance)
        biodata_pengurus_form = BiodataPengurusForm(instance=dokumen_instance)
        foto_pengurus_form = FotoPengurusForm(instance=dokumen_instance)
        ktp_pengurus_form = KtpPengurusForm(instance=dokumen_instance)
        npwp_pengurus_form = NpwpPengurusForm(instance=dokumen_instance)
        surat_domisili_form = SuratDomisiliForm(instance=dokumen_instance)
        surat_kepemilikan_gedung_form = SuratKepemilikanGedungForm(instance=dokumen_instance)
        foto_kantor_form = FotoKantorForm(instance=dokumen_instance)
        surat_tidak_sengketa_form = SuratTidakSengketaForm(instance=dokumen_instance)
        surat_pernyataan_kesanggupan_form = SuratPernyataanKesanggupanForm(instance=dokumen_instance)
        surat_tidak_terkait_politik_form = SuratTidakTerkaitPolitikForm(instance=dokumen_instance)
        surat_pernyataan_hak_paten_form = SuratPernyataanHakPatenForm(instance=dokumen_instance)
        surat_rekomendasi_satu_form = SuratRekomendasiSatuForm(instance=dokumen_instance)
        surat_rekomendasi_dua_form = SuratRekomendasiDuaForm(instance=dokumen_instance)
        surat_pernyataan_pejabat_form = SuratPernyataanPejabatForm(instance=dokumen_instance)


    return render(request, 'dashboard/edit_dokumen.html', {
        'akta_notaris_form': akta_notaris_form,
        'ad_art_form': ad_art_form,
        'program_kerja_form': program_kerja_form,
        'struktur_organisasi_form': struktur_organisasi_form,
        'biodata_pengurus_form': biodata_pengurus_form,
        'foto_pengurus_form': foto_pengurus_form,
        'ktp_pengurus_form': ktp_pengurus_form,
        'npwp_pengurus_form': npwp_pengurus_form,
        'surat_domisili_form': surat_domisili_form,
        'surat_kepemilikan_gedung_form': surat_kepemilikan_gedung_form,
        'foto_kantor_form': foto_kantor_form,
        'surat_tidak_sengketa_form': surat_tidak_sengketa_form,
        'surat_pernyataan_kesanggupan_form': surat_pernyataan_kesanggupan_form,
        'surat_tidak_terkait_politik_form': surat_tidak_terkait_politik_form,
        'surat_pernyataan_hak_paten_form': surat_pernyataan_hak_paten_form,
        'surat_rekomendasi_satu_form': surat_rekomendasi_satu_form,
        'surat_rekomendasi_dua_form': surat_rekomendasi_dua_form,
        'surat_pernyataan_pejabat_form': surat_pernyataan_pejabat_form,
        'register_id': register_id,
    })



# def akhiri_pendaftaran(request, register_id):
#     register = get_object_or_404(Register, id=register_id)
#     if register.is_completed:
#         messages.error(request, "Pendaftaran sudah diakhiri. Anda tidak dapat mengedit data lagi.")
#         return redirect(reverse('resume_page', args=[register_id]))
    
#     register.is_completed = True
#     register.save()
#     messages.success(request, "Pendaftaran telah berhasil diakhiri.")
#     return redirect(reverse('resume_page', args=[register_id]))


def akhiri_pendaftaran(request, register_id):
    # Ambil object Register berdasarkan ID
    register = get_object_or_404(Register, id=register_id)

    if request.method == 'POST':
        # Cek jika pendaftaran sudah selesai
        if register.is_completed:
            messages.error(request, "Pendaftaran sudah diakhiri, Anda tidak dapat mengedit data lagi.")
        else:
            # Ubah status is_completed menjadi True
            register.is_completed = True
            register.save()
            messages.success(request, "Pendaftaran telah berhasil diakhiri.")

        # Redirect ke halaman resume_page setelah update
        return redirect('resume_page', register_id=register.id)

    # Jika bukan POST, kembali ke halaman resume_page
    return redirect('resume_page', register_id=register.id)