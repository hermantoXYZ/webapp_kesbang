function copyLink(audioUrl, counter) {
    const fullUrl = `${audioUrl}`; // Menambahkan URL domain.com
    // Salin link ke clipboard
    navigator.clipboard.writeText(fullUrl).then(() => {
        // Dapatkan tombol berdasarkan ID
        const button = document.getElementById(`copy-link-button-${counter}`);
        // Ubah ikon tombol
        button.innerHTML = '✅'; // Contoh mengubah ke ikon centang
        // Anda bisa menambahkan logika untuk mengubah kembali ikon setelah beberapa detik, jika diinginkan
        setTimeout(() => {
            button.innerHTML = '🔗'; // Kembali ke ikon salin
        }, 2000); // Ubah kembali setelah 2 detik
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}