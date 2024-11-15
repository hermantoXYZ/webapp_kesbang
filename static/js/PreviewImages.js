// Get the modal
var modal = document.getElementById("modal-preview-photo");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var images = document.getElementsByClassName("images-preview");
var modalImg = document.getElementById("modal-img");
var currentImageIndex;

for (let i = 0; i < images.length; i++) {
    images[i].onclick = function () {
        modal.style.display = "block";
        modalImg.src = this.src;
        currentImageIndex = i;
    };
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
};

// Handle next/previous functionality
document.querySelector('.prev').onclick = function() {
    currentImageIndex = (currentImageIndex > 0) ? currentImageIndex - 1 : images.length - 1;
    modalImg.src = images[currentImageIndex].src;
};

document.querySelector('.next').onclick = function() {
    currentImageIndex = (currentImageIndex < images.length - 1) ? currentImageIndex + 1 : 0;
    modalImg.src = images[currentImageIndex].src;
};
