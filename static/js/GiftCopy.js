
function toggleCashless() {
        var accountBank = document.querySelector('.account-bank');
        var kirimKado = document.querySelector('.kirim-kado');
        
        if (accountBank.style.display === 'none') {
            accountBank.style.display = 'block';
            kirimKado.style.display = 'none'; // Hide Kirim Kado section
        } else {
            accountBank.style.display = 'none';
        }
    }

    function toggleKirimKado() {
        var kirimKado = document.querySelector('.kirim-kado');
        var accountBank = document.querySelector('.account-bank');
        
        if (kirimKado.style.display === 'none') {
            kirimKado.style.display = 'block';
            accountBank.style.display = 'none'; // Hide Cashless section
        } else {
            kirimKado.style.display = 'none';
        }
    }

    function copyText(button, text) {
        navigator.clipboard.writeText(text).then(() => {
            button.innerText = 'Berhasil Disalin';
            setTimeout(() => {
                button.innerText = 'Salin';
            }, 10000); // Mengubah kembali ke "Salin" setelah 2 detik
        }).catch(err => {
            console.error('Gagal menyalin teks: ', err);
        });
    }
