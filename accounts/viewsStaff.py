from uuid import UUID
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from modelform.models import Register, Pemohon, Pengurus, Organisasi, Dokumen
from django.db.models import Q 
from django.contrib import messages

def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff)
def staff(request):
    query = request.GET.get('q', '')  # Mengambil nilai dari parameter 'q' di URL
    results = Register.objects.filter()
    results_verified = Register.objects.filter(is_verified=True)
    total_pengajuan = results.count()
    total_verified = results_verified.count()
    unverified_completed_count = Register.objects.filter(is_completed=True, is_verified=False).count()

    if query:
        results = results.filter(
            Q(nama_organisasi__icontains=query) | Q(register__icontains=query)
        )

    context = {
        'results': results,
        'query': query,
        'total_pengajuan': total_pengajuan,
        'total_verified': total_verified,
        'unverified_completed_count': unverified_completed_count,
    }

    return render(request, 'dashboard/staff.html', context)

@user_passes_test(is_staff)
def dashboard_profile_staff(request):
    user = request.user
    return render(request, 'dashboard/profile.html', {'user': user})




@user_passes_test(is_staff)
def list_pengajuan(request):
    query = request.GET.get('q', '')
    results = Register.objects.filter()
    results_verified = Register.objects.filter(is_verified=True)
    total_pengajuan = results.count()
    total_verified = results_verified.count()
    unverified_completed_count = Register.objects.filter(is_completed=True, is_verified=False).count()

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
        'query': query,
        'registers': registers,
        'total_pengajuan': total_pengajuan,
        'total_verified': total_verified,
        'unverified_completed_count': unverified_completed_count,
    }



    return render(request, 'dashboard/list_pengajuan.html', context)


@user_passes_test(is_staff)
def view_pengajuan(request, register_id):
    register = get_object_or_404(Register, id=register_id)
    pemohon = Pemohon.objects.filter(register=register).first()
    pengurus = Pengurus.objects.filter(register=register).first()
    organisasi = Organisasi.objects.filter(register=register).first()
    dokumen = Dokumen.objects.filter(register=register).first()
    surat_permohonan_skt = pemohon.surat_permohonan_skt if pemohon else None

    if request.method == "POST":
        if not register.is_verified:
            # Verifikasi Register
            register.verify()
            messages.success(request, "Dokumen telah berhasil diverifikasi.")
        else:
            messages.error(request, "Dokumen telah diverifikasi sebelumnya.")


    context = {
        'register': register,    
        'pemohon': pemohon,
        'pengurus': pengurus,
        'organisasi': organisasi,
        'dokumen': dokumen,
        'surat_permohonan_skt': surat_permohonan_skt
    }

    return render(request, 'dashboard/view_pengajuan.html', context)

