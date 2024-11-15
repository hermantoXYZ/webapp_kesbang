
  $(document).ready(function() {
    // Handle form submission via AJAX
    $('form').submit(function(event) {
        event.preventDefault(); // Prevent normal form submission
        
        var formData = $(this).serialize(); // Serialize form data
        var submitButton = $(this).find(':submit');
        submitButton.prop('disabled', true); // Disable submit button to prevent multiple submissions

        // Include CSRF token if necessary
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        
        // AJAX POST request
        $.ajax({
            type: 'POST',
            url: '', // URL untuk endpoint form submission
            data: formData,
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken); // Add CSRF token to request header if needed
            },
            success: function(response) {
                // Handle successful form submission
                $('form')[0].reset(); // Clear form fields
                
                // Update comments section with new comment
                var newCommentHtml = '<li><div class="comment-avatar">' + response.name.slice(0, 1) + '</div>' +
                                    '<div class="comment-content"><strong>' + response.name + '</strong> ' +
                                    '<span class="badge">' + response.attend + '</span>' +
                                    '<p>' + response.message + '</p>' +
                                    '<small>' + response.created_at + '</small></div></li>';
                $('#commentList').prepend(newCommentHtml); // Add new comment to the top
                submitButton.prop('disabled', false); // Re-enable submit button
                
                // Show success message below the submit button
                $('#success-message').text('Data berhasil terkirim!').fadeIn();

                // Automatically close success message after a few seconds
                setTimeout(function() {
                    $('#success-message').fadeOut('slow');
                }, 3000); // 3000 milliseconds (3 seconds) - adjust as needed
                
                // Remove the call to closeModal() to keep the modal open
                // closeModal();
            },
            error: function(error) {
                console.log('Error:', error);
                alert('There was an error submitting the form. Please try again.');
                submitButton.prop('disabled', false); // Re-enable submit button
            }
        });
    });
});

