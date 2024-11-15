
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from . forms import  ProfileUpdateForm   
from django.contrib.auth.decorators import login_required
from modelform.models import Register
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
    query = request.GET.get('q', '')  # Mengambil nilai dari parameter 'q' di URL
    results = Register.objects.filter(author=request.user)
    jumlah_pengajuan_skt = Register.objects.filter(is_completed=True).filter(author=request.user).count()

    if query:
        results = results.filter(
            Q(nama_organisasi__icontains=query) | Q(register__icontains=query)
        )

    user = request.user
    return render(request, 'dashboard/pelanggan.html', {'user': user, 'results': results, 'query': query, 'jumlah_pengajuan_skt': jumlah_pengajuan_skt})