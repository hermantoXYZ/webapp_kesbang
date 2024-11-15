function copyToClipboard(icon, text) {
    navigator.clipboard.writeText(text).then(() => {
        icon.classList.remove('fa-copy');
        icon.classList.add('fa-check', 'checked');

        // Set timeout to revert the icon back to copy icon after 2 seconds
        setTimeout(() => {
            icon.classList.remove('fa-check', 'checked');
            icon.classList.add('fa-copy');
        }, 2000); // 2000 milliseconds = 2 seconds

    }).catch(err => {
        console.error('Could not copy text: ', err);
    });
}