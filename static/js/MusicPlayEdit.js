
    document.addEventListener('DOMContentLoaded', function() {
        var audioSelect = document.getElementById('id_audio');
        var audioPreview = document.getElementById('audio-preview');
        var audioPlayer = document.getElementById('audio-player');
        var audioSource = document.getElementById('audio-source');
    
        audioSelect.addEventListener('change', function() {
            var selectedOption = this.options[this.selectedIndex];
            var musicFileUrl = selectedOption.getAttribute('data-music-url');
    
            if (musicFileUrl) {
                audioSource.src = musicFileUrl;
                audioPlayer.load();
                audioPreview.style.display = 'block';
            } else {
                audioPreview.style.display = 'none';
            }
        });
    });
