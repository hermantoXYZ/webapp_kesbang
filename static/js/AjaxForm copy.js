$(document).ready(function() {
    $('#invitationForm button[type=submit]').click(function(event) {
        event.preventDefault(); // Prevent default form submission

        var submitButton = $(this); // Get the clicked button
        var buttonName = submitButton.attr('name'); // Get the name of the clicked button
        var form = $('#invitationForm')[0];
        var formData = new FormData(form);

        // Append the clicked button's name to formData
        formData.append(buttonName, true);

        // Show loading animation on the button
        submitButton.html('<i class="fa fa-spinner fa-spin"></i> Updating...');
        submitButton.prop('disabled', true); // Disable the button to prevent multiple clicks

        $.ajax({
            type: $(form).attr('method'),
            url: $(form).attr('action'),
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('Response from server:', response); // Log the response


                // Handle successful form submission for invitation
                if (buttonName === 'submit_invitation' && response.status === 'success') {

                    var baseURL = 'https://inviteku.com/';
                    var fullURL = baseURL + (response.slug || 'default-slug');
                    // Update HTML elements with the new data
                    $('#invitationName').text(response.name || 'Default Name');
                    $('#invitationSlug').text(fullURL || 'default-slug');
                    $('#invitationTheme').text(response.theme || 'Default Theme');
                    $('#invitationCategory').text(response.category || 'Default Category');
                      // Update the audio element if available
                    var audioContainer = $('#audio-container');
                    var musicPlayer = $('#music-player');
                    var audioSource = $('#audio-source');
                    var noAudio = $('#no-audio');

                    if (response.audio_link) {
                        if (audioSource.length === 0) {
                            // Create and append the audio element if it doesn't exist
                            audioContainer.html('<audio id="music-player" controls loop><source id="audio-source" src="' + response.audio_link + '" type="audio/mp3">Your browser does not support the audio element.</audio>');
                        } else {
                            // Update the existing audio element's source
                            audioSource.attr('src', response.audio_link);
                            musicPlayer[0].load();  // Reload the audio element to play the new source
                        }
                        musicPlayer.show();
                        noAudio.hide();
                    } else {
                        // Show no audio message if no audio link is provided
                        audioContainer.html('<p id="no-audio">No audio available</p>');
                    }

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="nama_undangan"]').val(response.name);
                    $('#invitationForm').find('input[name="slug"]').val(response.slug);
                    $('#invitationForm').find('input[name="theme"]').val(response.theme);
                    $('#invitationForm').find('input[name="category"]').val(response.category);
                    $('#invitationForm').find('input[name="audio_link"]').val(response.audio_link);
                }

                // Handle successful form submission
                // Handle successful form submission for opening
                if (buttonName === 'submit_opening' && response) {
                    // Update HTML elements with the new data
                    $('#openingText1').text(response.opening_text_1 || 'The Wedding of');
                    $('#openingText2').text(response.opening_text_2 || 'Andy');
                    $('#openingText3').text(response.opening_text_3 || 'Dan');
                    $('#openingText4').text(response.opening_text_4 || 'Ifa');
                    $('#openingText5').html(response.opening_text_5 || 'Kepada Yth;<br>Bapak/Ibu/Saudara/i');
                    $('#openingText6').text(response.opening_text_6 || 'Buka Undangan');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="opening_text_1"]').val(response.opening_text_1);
                    $('#invitationForm').find('input[name="opening_text_2"]').val(response.opening_text_2);
                    $('#invitationForm').find('input[name="opening_text_3"]').val(response.opening_text_3);
                    $('#invitationForm').find('input[name="opening_text_4"]').val(response.opening_text_4);
                    $('#invitationForm').find('input[name="opening_text_5"]').val(response.opening_text_5);
                    $('#invitationForm').find('input[name="opening_text_6"]').val(response.opening_text_6);

                    if (response.opening_images) {
                        $('#invitationForm').find('#opening_images_preview').attr('src', response.opening_images);
                    } else {
                        $('#invitationForm').find('#opening_images_preview').removeAttr('src');
                    }
                }

                 // Handle successful form submission for greeting
                if (buttonName === 'submit_greeting' && response) {
                    // Update HTML elements with the new data
                    $('#greetingText1').text(response.greeting_text_1 || 'Assalamu"alaikum Wr.Wb');
                    $('#greetingText2').text(response.greeting_text_2 || 'Tanpa mengurangi rasa hormat, kami bermaksud mengundang Bapak/Ibu/Saudara/i pada acara resepsi pernikahan anak kami');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="greeting_text_1"]').val(response.greeting_text_1);
                    $('#invitationForm').find('input[name="greeting_text_2"]').val(response.greeting_text_2);
                }

                 // Handle successful form submission for quote
                if (buttonName === 'submit_quote' && response) {
                    // Update HTML elements with the new data
                    $('#quotesText1').text(response.quotes_text_1 || 'Kutipan');
                    $('#quotesText2').text(response.quotes_text_2 || '"Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan pasangan-pasangan untukmu dari jenismu sendiri, agar kamu cenderung dan merasa tenteram kepadanya, dan Dia menjadikan di antaramu rasa kasih dan sayang. Sungguh, pada yang demikian itu benar-benar terdapat tanda-tanda (kebesaran Allah) bagi kaum yang berpikir"');
                    $('#quotesText3').text(response.quotes_text_3 || 'Surah Ar Ruum : 21');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="quotes_text_1"]').val(response.quotes_text_1);
                    $('#invitationForm').find('input[name="quotes_text_2"]').val(response.quotes_text_2);
                    $('#invitationForm').find('input[name="quotes_text_3"]').val(response.quotes_text_3);

                    if (response.quotes_images) {
                        $('#invitationForm').find('#quotes_images_preview').attr('src', response.quotes_images);
                    } else {
                        $('#invitationForm').find('#quotes_images_preview').removeAttr('src');
                    }
                }

                 // Handle successful form submission for mempelai
                if (buttonName === 'submit_mempelai' && response) {
                    // Update HTML elements with the new data
                    $('#mempelaiPria').text(response.mempelai_pria || 'Default Mempelai Pria');
                    $('#mempelaiText1Pria').text(response.mempelai_text_1_pria || 'Default Text 1 Pria');
                    $('#mempelaiText2Pria').text(response.mempelai_text_2_pria || 'Default Text 2 Pria');
                    $('#mempelaiText3Pria').text(response.mempelai_text_3_pria || 'Default Text 3 Pria');
                    $('#mempelaiText4Pria').text(response.mempelai_text_4_pria || 'Default Text 4 Pria');
                    $('#mempelaiText5Pria').text(response.mempelai_text_5_pria || 'Default Text 5 Pria');
                    $('#mempelaiText6Pria').text(response.mempelai_text_6_pria || 'Default Text 6 Pria');
                    $('#mempelaiWanita').text(response.mempelai_wanita || 'Default Mempelai Wanita');
                    $('#mempelaiText1Wanita').text(response.mempelai_text_1_wanita || 'Default Text 1 Wanita');
                    $('#mempelaiText2Wanita').text(response.mempelai_text_2_wanita || 'Default Text 2 Wanita');
                    $('#mempelaiText3Wanita').text(response.mempelai_text_3_wanita || 'Default Text 3 Wanita');
                    $('#mempelaiText4Wanita').text(response.mempelai_text_4_wanita || 'Default Text 4 Wanita');
                    $('#mempelaiText5Wanita').text(response.mempelai_text_5_wanita || 'Default Text 5 Wanita');
                    $('#mempelaiText6Wanita').text(response.mempelai_text_6_wanita || 'Default Text 6 Wanita');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="mempelai_pria"]').val(response.mempelai_pria);
                    $('#invitationForm').find('input[name="mempelai_text_1_pria"]').val(response.mempelai_text_1_pria);
                    $('#invitationForm').find('input[name="mempelai_text_2_pria"]').val(response.mempelai_text_2_pria);
                    $('#invitationForm').find('input[name="mempelai_text_3_pria"]').val(response.mempelai_text_3_pria);
                    $('#invitationForm').find('input[name="mempelai_text_4_pria"]').val(response.mempelai_text_4_pria);
                    $('#invitationForm').find('input[name="mempelai_text_5_pria"]').val(response.mempelai_text_5_pria);
                    $('#invitationForm').find('input[name="mempelai_text_6_pria"]').val(response.mempelai_text_6_pria);
                    $('#invitationForm').find('input[name="mempelai_wanita"]').val(response.mempelai_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_1_wanita"]').val(response.mempelai_text_1_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_2_wanita"]').val(response.mempelai_text_2_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_3_wanita"]').val(response.mempelai_text_3_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_4_wanita"]').val(response.mempelai_text_4_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_5_wanita"]').val(response.mempelai_text_5_wanita);
                    $('#invitationForm').find('input[name="mempelai_text_6_wanita"]').val(response.mempelai_text_6_wanita);

                    if (response.mempelai_images_pria) {
                        $('#invitationForm').find('#mempelai_images_pria_preview').attr('src', response.mempelai_images_pria);
                    } else {
                        $('#invitationForm').find('#mempelai_images_pria_preview').removeAttr('src');
                    }

                    if (response.mempelai_images_wanita) {
                        $('#invitationForm').find('#mempelai_images_wanita_preview').attr('src', response.mempelai_images_wanita);
                    } else {
                        $('#invitationForm').find('#mempelai_images_wanita_preview').removeAttr('src');
                    }
                }


                 // Handle successful form submission for akad
                if (buttonName === 'submit_akad' && response) {

                    function formatDate(dateString) {
                        const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
                        const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
                    
                        const date = new Date(dateString);
                        const dayName = days[date.getDay()];
                        const day = date.getDate();
                        const month = months[date.getMonth()];
                        const year = date.getFullYear();
                    
                        return `${dayName}, ${day} ${month} ${year}`;
                    }
                    
                    function formatTime(timeString) {
                        if (!timeString) return '18:00'; // Default time
                
                        // Extract the hours and minutes from timeString
                        const timeParts = timeString.split(':');
                        if (timeParts.length >= 2) {
                            return timeParts[0] + ':' + timeParts[1];
                        }
                        return '18:00'; // Fallback to default time
                    }

                    // Update HTML elements with the new data for akad
                    $('#akad').text(response.akad || 'Default Akad');
                    $('#akadText1').text(response.akad_text_1 || 'Default Akad Text 1');
                    $('#eventDetailsAkad').html(
                        (response.tanggal_akad ? formatDate(response.tanggal_akad) : 'Minggu, 31 Desember 2022') + '<br>' +
                        'Pukul ' + (response.waktu_akad ? formatTime(response.waktu_akad)  :  '18:00')+ ' '   +
                        (response.zona_waktu_akad || 'WIB') + '<br>' +
                        (response.alamat_akad || 'Inviteku.com') + '<br>' +
                        (response.lokasi_akad || 'Luwu Raya, Sulawesi Selatan, Indonesia')
                    );

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="akad"]').val(response.akad);
                    $('#invitationForm').find('input[name="akad_text_1"]').val(response.akad_text_1);
                    $('#invitationForm').find('input[name="tanggal_akad"]').val(response.tanggal_akad);
                    $('#invitationForm').find('input[name="waktu_akad"]').val(response.waktu_akad);
                    $('#invitationForm').find('input[name="zona_waktu_akad"]').val(response.zona_waktu_akad);
                    $('#invitationForm').find('input[name="alamat_akad"]').val(response.alamat_akad);
                    $('#invitationForm').find('input[name="lokasi_akad"]').val(response.lokasi_akad);
                }


                if (buttonName === 'submit_resepsi' && response) {

                    function formatDate(dateString) {
                        const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
                        const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
                    
                        const date = new Date(dateString);
                        const dayName = days[date.getDay()];
                        const day = date.getDate();
                        const month = months[date.getMonth()];
                        const year = date.getFullYear();
                    
                        return `${dayName}, ${day} ${month} ${year}`;
                    }
                    
                    function formatTime(timeString) {
                        if (!timeString) return '18:00'; // Default time
                
                        // Extract the hours and minutes from timeString
                        const timeParts = timeString.split(':');
                        if (timeParts.length >= 2) {
                            return timeParts[0] + ':' + timeParts[1];
                        }
                        return '18:00'; // Fallback to default time
                    }

                    // Update HTML elements with the new data for resepsi
                    $('#resepsi').text(response.resepsi || 'Default Resepsi');
                    $('#resepsiText1').text(response.resepsi_text_1 || 'Default Resepsi Text 1');
                    $('#eventDetailsResepsi').html(
                        (response.tanggal_resepsi ? formatDate(response.tanggal_resepsi) : 'Minggu, 31 Desember 2022') + '<br>' +
                        'Pukul ' + (response.waktu_resepsi ? formatTime(response.waktu_resepsi)  :  '18:00')+ ' '   +
                        (response.zona_waktu_resepsi || 'WIB') + '<br>' +
                        (response.alamat_resepsi || 'Inviteku.com') + '<br>' +
                        (response.lokasi_resepsi || 'Luwu Raya, Sulawesi Selatan, Indonesia')
                    );

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="resepsi"]').val(response.resepsi);
                    $('#invitationForm').find('input[name="resepsi_text_1"]').val(response.resepsi_text_1);
                    $('#invitationForm').find('input[name="tanggal_resepsi"]').val(response.tanggal_resepsi);
                    $('#invitationForm').find('input[name="waktu_resepsi"]').val(response.waktu_resepsi);
                    $('#invitationForm').find('input[name="zona_waktu_resepsi"]').val(response.zona_waktu_resepsi);
                    $('#invitationForm').find('input[name="alamat_resepsi"]').val(response.alamat_resepsi);
                    $('#invitationForm').find('input[name="lokasi_resepsi"]').val(response.lokasi_resepsi);
                }

                  // Handle successful form submission for maps
                if (buttonName === 'submit_maps' && response) {
                    // Update HTML elements with the new data for maps
                    $('#mapsText1').text(response.maps_text_1 || 'Default Maps Text 1');
                    $('#mapsText2').text(response.maps_text_2 || 'Default Maps Text 2');
                    $('#mapsText3').text(response.maps_text_3 || 'Default Maps Text 3');
                    $('#mapsText4').text(response.maps_text_4 || 'Default Maps Text 4');
                    $('#mapsIframe').attr('src', response.maps_link_1 || 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.047451007307!2d144.9559273153199!3d-37.81720997975195!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf5778d1c9e6e7e9a!2sFederation+Square!5e0!3m2!1sen!2sau!4v1494489989637');
                }

                if (buttonName === 'submit_gallery' && response) {
                    // Update HTML elements with the new data
                    $('#galleryText1').text(response.gallery_text_1 || 'Default Gallery Text 1');

                    // Update gallery images
                    if (response.gallery_images_1) {
                        $('#galleryImages1').attr('src', response.gallery_images_1);
                    } else {
                        $('#galleryImages1').removeAttr('src');
                    }
                    

                    if (response.gallery_images_2) {
                        $('#galleryImages2').attr('src', response.gallery_images_2);
                    } else {
                        $('#galleryImages2').removeAttr('src');
                    }

                    if (response.gallery_images_3) {
                        $('#galleryImages3').attr('src', response.gallery_images_3);
                    } else {
                        $('#galleryImages3').removeAttr('src');
                    }

                    if (response.gallery_images_4) {
                        $('#galleryImages4').attr('src', response.gallery_images_4);
                    } else {
                        $('#galleryImages4').removeAttr('src');
                    }

                    if (response.gallery_images_5) {
                        $('#galleryImages5').attr('src', response.gallery_images_5);
                    } else {
                        $('#galleryImages5').removeAttr('src');
                    }

                    if (response.gallery_images_6) {
                        $('#galleryImages6').attr('src', response.gallery_images_6);
                    } else {
                        $('#galleryImages6').removeAttr('src');
                    }

                    if (response.gallery_images_7) {
                        $('#galleryImages7').attr('src', response.gallery_images_7);
                    } else {
                        $('#galleryImages7').removeAttr('src');
                    }

                    if (response.gallery_images_8) {
                        $('#galleryImages8').attr('src', response.gallery_images_8);
                    } else {
                        $('#galleryImages8').removeAttr('src');
                    }

                    if (response.gallery_images_9) {
                        $('#galleryImages9').attr('src', response.gallery_images_9);
                    } else {
                        $('#galleryImages9').removeAttr('src');
                    }

                    if (response.gallery_images_10) {
                        $('#galleryImages10').attr('src', response.gallery_images_10);
                    } else {
                        $('#galleryImages10').removeAttr('src');
                    }
                }


                  // Handle successful form submission for RSVP
                if (buttonName === 'submit_rsvp' && response) {
                    $('#rsvpText1').text(response.rsvp_text_1 || 'Default RSVP Text 1');
                    $('#rsvpText2').text(response.rsvp_text_2 || 'Default RSVP Text 2');
                    $('#rsvpText3').text(response.rsvp_text_3 || 'Default RSVP Text 3');
                    $('#rsvpText4').text(response.rsvp_text_4 || 'Default RSVP Text 4');

                    $('#invitationForm').find('input[name="rsvp_text_1"]').val(response.rsvp_text_1);
                    $('#invitationForm').find('input[name="rsvp_text_2"]').val(response.rsvp_text_2);
                    $('#invitationForm').find('input[name="rsvp_text_3"]').val(response.rsvp_text_3);
                    $('#invitationForm').find('input[name="rsvp_text_4"]').val(response.rsvp_text_4);

                    if (response.rsvp_images) {
                        $('#invitationForm').find('#rsvp_images_preview').attr('src', response.rsvp_images);
                    } else {
                        $('#invitationForm').find('#rsvp_images_preview').removeAttr('src');
                    }
                }

                // Handle successful form submission for gift
                if (buttonName === 'submit_gift' && response) {
                    // Update HTML elements with the new data
                    $('#gift').text(response.gift || 'Default Gift');
                    $('#giftText1').text(response.gift_text_1 || 'Default Gift Text 1');
                    $('#giftText2').text(response.gift_text_2 || 'Default Gift Text 2');
                    $('#giftText3').text(response.gift_text_3 || 'Default Gift Text 3');
                    $('#paymentMethod1').text(response.payment_method_1 || 'Default Payment Method 1');
                    $('#nomorRekening1').text(response.nomor_rekening_1 || 'Default No Rekening 1');
                    $('#namaPemilikRekening1').text(response.nama_pemilik_rekening_1 || 'Default Pemilik Rekening 1');
                    $('#paymentMethod2').text(response.payment_method_2 || 'Default Payment Method 2');
                    $('#nomorRekening2').text(response.nomor_rekening_2 || 'Default No Rekening 2');
                    $('#namaPemilikRekening2').text(response.nama_pemilik_rekening_2 || 'Default Pemilik Rekening 2');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="gift"]').val(response.gift);
                    $('#invitationForm').find('input[name="gift_text_1"]').val(response.gift_text_1);
                    $('#invitationForm').find('input[name="gift_text_2"]').val(response.gift_text_2);
                    $('#invitationForm').find('input[name="gift_text_3"]').val(response.gift_text_3);
                    $('#invitationForm').find('input[name="payment_method_1"]').val(response.payment_method_1);
                    $('#invitationForm').find('input[name="nomor_rekening_1"]').val(response.nomor_rekening_1);
                    $('#invitationForm').find('input[name="nama_pemilik_rekening_1"]').val(response.nama_pemilik_rekening_1);
                    $('#invitationForm').find('input[name="payment_method_2"]').val(response.payment_method_2);
                    $('#invitationForm').find('input[name="nomor_rekening_2"]').val(response.nomor_rekening_2);
                    $('#invitationForm').find('input[name="nama_pemilik_rekening_2"]').val(response.nama_pemilik_rekening_2);

                    if (response.gift_images) {
                        $('#invitationForm').find('#gift_images_preview').attr('src', response.gift_images);
                    } else {
                        $('#invitationForm').find('#gift_images_preview').removeAttr('src');
                    }
                }

                if (buttonName === 'submit_thanks' && response) {
                    // Update HTML elements with the new data
                    $('#thanksText1').text(response.thanks_text_1 || 'Default Thanks Text 1');
                    $('#thanksText2').text(response.thanks_text_2 || 'Default Thanks Text 2');
                    $('#thanksText3').text(response.thanks_text_3 || 'Default Thanks Text 3');
                    $('#thanksText4').text(response.thanks_text_4 || 'Default Thanks Text 4');

                    // Update form inputs with the new data
                    $('#invitationForm').find('input[name="thanks_text_1"]').val(response.thanks_text_1);
                    $('#invitationForm').find('input[name="thanks_text_2"]').val(response.thanks_text_2);
                    $('#invitationForm').find('input[name="thanks_text_3"]').val(response.thanks_text_3);
                    $('#invitationForm').find('input[name="thanks_text_4"]').val(response.thanks_text_4);

                    if (response.thanks_images) {
                        $('#invitationForm').find('#thanks_images_preview').attr('src', response.thanks_images);
                    } else {
                        $('#invitationForm').find('#thanks_images_preview').removeAttr('src');
                    }
                }


                // Show success notification
                $('#notification-message').text(response.message);
                $('#notification').addClass('show');

                // Hide the notification after 3 seconds
                setTimeout(function() {
                    $('#notification').removeClass('show');
                }, 3000);
            },
            error: function(response) {
                // Handle errors
                console.log('Error:', response); // Log the error
                var errors = JSON.parse(response.responseText).errors;
                alert(errors);
            },
            complete: function() {
                // Revert the button back to its original state
                submitButton.html('Save'); // Change this to the original button text
                submitButton.prop('disabled', false); // Enable the button again
            }
        });
    });
});
