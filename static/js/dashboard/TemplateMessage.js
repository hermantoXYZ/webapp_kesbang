
    // Define templates
    const templates = {
        template1: `Kepada Yth.\nBapak/Ibu/Saudara/i\n{tamu_name}\ndi tempat\n\nTanpa mengurangi rasa hormat, perkenankan kami mengundang Bapak/Ibu/Saudara/i, untuk menghadiri acara Resepsi Pernikahan Kami\n\nMempelai Pria & Wanita\n\n* Hari/Tgl : \n* Pukul : \n* Tempat : \n\nInfo lebih lengkap klik link dibawah ini 👇👇👇\n{invitation_slug} \n\nMerupakan suatu kebahagiaan bagi kami apabila Bapak/Ibu/Saudara/i berkenan untuk hadir dan memberikan doa restu.\n\nKami yang berbahagia\nKeluarga Kedua Mempelai\n\nMohon maaf perihal undangan hanya dibagikan melalui pesan ini dikarenakan keterbatasan jarak dan juga waktu.`,
        template2: `Halo {tamu_name}\nJangan Lewatkan pesata kami yang akan diadakan pada \n\n* Hari/Tgl : \n* Pukul : \n* Tempat : \n\n Temukan semua detail dan konfirmasi kehadiran Anda melalui tautan berikut: [{invitation_slug}]\n\nKami sangat menantikan kehadiran Anda!\n\nSalam,`,
        // Tambahkan lebih banyak template jika diperlukan
    };

    function setTemplate(templateKey) {
        const templateMessage = templates[templateKey];
        if (templateMessage) {
            document.querySelector('textarea[name="template_message"]').value = templateMessage;
        }
    }

    // Function to close modal
    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }

