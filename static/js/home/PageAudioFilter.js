
    document.addEventListener("DOMContentLoaded", function() {
        const playButtons = document.querySelectorAll(".play-button");

        playButtons.forEach(button => {
            const audioId = button.getAttribute("data-audio-id");
            const audioElement = document.getElementById(audioId);
            const durationElement = document.getElementById(`duration-${audioId.split('-')[1]}`);

            // Update duration once metadata is loaded
            audioElement.addEventListener("loadedmetadata", function() {
                const minutes = Math.floor(audioElement.duration / 60);
                const seconds = Math.floor(audioElement.duration % 60).toString().padStart(2, '0');
                durationElement.textContent = `${minutes}:${seconds}`;
            });

            // Toggle play/pause on button click
            button.addEventListener("click", function() {
                if (audioElement.paused) {
                    audioElement.play();
                    button.innerHTML = "&#10074;&#10074;"; // Pause icon
                } else {
                    audioElement.pause();
                    button.innerHTML = "&#9654;"; // Play icon
                }
            });

            // Update button text when audio ends
            audioElement.addEventListener("ended", function() {
                button.innerHTML = "&#9654;"; // Play icon
            });
        });
    });

    function copyLink(url) {
        navigator.clipboard.writeText(url).then(() => {
            alert('Link copied to clipboard');
        }).catch(err => {
            console.error('Error copying link: ', err);
        });
    }

