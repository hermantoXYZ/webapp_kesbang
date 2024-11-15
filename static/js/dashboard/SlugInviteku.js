document.addEventListener('DOMContentLoaded', function() {
    // Access the template message from the global object
    const templateMessage = window.templateMessage;
    const invitationSlug = window.invitationSlug; 
    window.updateInvitationLink = function() {
        var nameInput = document.getElementById('id_name');
        var invitationLink = document.getElementById('invitation-link');

        var name = nameInput.value;
        var encodedName = encodeURIComponent(name);
        var baseUrl = `https://inviteku.com/${invitationSlug}`;
        var newLink = `${baseUrl}?to=${encodedName}`;

        invitationLink.href = newLink;
        invitationLink.textContent = newLink;
    };
    window.copyInvitationLink = function() {
        var name = document.getElementById('id_name').value;
        var invitationSlugUrl = `https://inviteku.com/${invitationSlug}?to=${encodeURIComponent(name)}`;

        var formattedMessage = templateMessage
            .replace(/{tamu_name}/g, name)
            .replace(/{invitation_slug}/g, invitationSlugUrl);

        var tempTextarea = document.createElement('textarea');
        tempTextarea.value = formattedMessage;
        document.body.appendChild(tempTextarea);
        tempTextarea.select();
        document.execCommand('copy');
        document.body.removeChild(tempTextarea);

        var copyButtonText = document.querySelector('#copy-button span');
        copyButtonText.textContent = 'Success Copy';

        setTimeout(function() {
            copyButtonText.textContent = 'Copy Link';
        }, 2000);
    };

    document.getElementById('id_name').addEventListener('input', updateInvitationLink);
    document.getElementById('copy-button').addEventListener('click', copyInvitationLink);
});
