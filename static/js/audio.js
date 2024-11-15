// $(document).ready(function() {
//     // Update audio preview when a new audio is selected
//     $('#id_audio').change(function() {
//         var selectedAudioId = $(this).val();
//         var audioSrc = '';

//         // Map of audio IDs to their respective sources
//         var audioSources = {
//             '1': '/media/musics/audio1.mp3',
//             '2': '/media/musics/audio2.mp3',
//             '3': '/media/musics/audio3.mp3'
//         };

//         // Set the audio source based on the selected ID
//         if (audioSources[selectedAudioId]) {
//             audioSrc = audioSources[selectedAudioId];
//         }

//         // Update the audio player
//         updateAudioPlayer(audioSrc);
//     });

//     // Update audio preview when the audio link is entered
//     $('#id_audio_link').on('input', function() {
//         var audioLink = $(this).val();
//         updateAudioPlayer(audioLink);
//     });

//     // Function to update the audio player
//     function updateAudioPlayer(src) {
//         var audioPlayer = $('#music-player');
        
//         if (src) {
//             audioPlayer.find('source').attr('src', src);
//             audioPlayer[0].load(); // Reload the audio player to reflect changes
//             audioPlayer.show(); // Show the audio player
//         } else {
//             audioPlayer.hide(); // Hide the audio player if no source is provided
//             $('#audio-container').html('<p>No audio selected</p>'); // Optionally show a message
//         }
//     }
// });
