// Handle Image Preview
    document.addEventListener('DOMContentLoaded', function () {
        var imageInputs = document.querySelectorAll('.image-input');

        imageInputs.forEach(function(input) {
            input.addEventListener('change', function(event) {
                var previewId = event.target.getAttribute('data-preview-id');
                var preview = document.getElementById(previewId);
                var currentImage = preview.querySelector('.current-image');

                if (event.target.files && event.target.files[0]) {
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        if (currentImage) {
                            currentImage.src = e.target.result;
                        } else {
                            var img = document.createElement('img');
                            img.className = 'current-image';
                            img.src = e.target.result;
                            preview.innerHTML = ''; // Clear existing content
                            preview.appendChild(img);
                        }
                    }
                    reader.readAsDataURL(event.target.files[0]);
                }
            });
        });
    });
