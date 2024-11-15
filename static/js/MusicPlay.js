
    var musicBtn = document.getElementById("btnMusic");
    var h = document.getElementById("music");
    var icon = document.getElementById("buttonIcon");
    var w = false;

    function playMusic() {
        if (h.paused) {
            h.play();
            icon.classList.remove('ri-disc-fill');
            icon.classList.add('ri-customer-service-fill');
        } else {
            h.pause();
            icon.classList.remove('ri-customer-service-fill');
            icon.classList.add('ri-disc-fill');
        }
    }

    h.onplaying = function() { 
        w = true; 
        icon.classList.remove('ri-disc-fill');
        icon.classList.add('ri-customer-service-fill');
    };

    h.onpause = function() { 
        w = false; 
        icon.classList.remove('ri-customer-service-fill');
        icon.classList.add('ri-disc-fill');
    };

    function openFullScreen() {
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        } else if (document.documentElement.webkitRequestFullscreen) {
            document.documentElement.webkitRequestFullscreen();
        } else if (document.documentElement.msRequestFullscreen) {
            document.documentElement.msRequestFullscreen();
        }
    }

    function openInvitation() {
        playMusic(true);
        openFullScreen();
    }
