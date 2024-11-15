
    function previewImage(event) {
        var input = event.target;
        var reader = new FileReader();
        reader.onload = function () {
            var imgElement = input.parentNode.querySelector('img');
            imgElement.src = reader.result;
            imgElement.style.display = 'block'; // Tampilkan gambar setelah dipilih
        }
        if (input.files && input.files[0]) {
            reader.readAsDataURL(input.files[0]);
        } else {
            var imgElement = input.parentNode.querySelector('img');
            imgElement.src = '';
            imgElement.style.display = 'none'; // Sembunyikan gambar jika tidak ada file yang dipilih
        }
    }
