function toggleModal(modalId) {
  // Get the requested modal element
  var modal = document.getElementById(modalId);

  // Check if the modal is already open
  var isModalOpen = modal.style.display === 'block';
  
  // Get all modal elements
  var modals = document.getElementsByClassName('modal');
  
  // Iterate through all modals and close them
  for (var i = 0; i < modals.length; i++) {
    modals[i].style.display = 'none';
  }
  
  // Open the requested modal only if it was not already open
  if (!isModalOpen) {
    modal.style.display = 'block';
  }
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
  if (event.target.classList.contains('modal')) {
    event.target.style.display = 'none';
  }
};

// Optional: Close the modal when pressing the 'Escape' key
window.onkeydown = function(event) {
  if (event.key === 'Escape') {
    var modals = document.getElementsByClassName('modal');
    for (var i = 0; i < modals.length; i++) {
      modals[i].style.display = 'none';
    }
  }
};


