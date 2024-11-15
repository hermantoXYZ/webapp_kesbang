document.addEventListener("DOMContentLoaded", function() {
    // Fungsi untuk menampilkan countdown
    function displayCountdown(element) {
        var dateTime = element.dataset.datetime;
        if (!dateTime) {
            // Set ke "00" jika data-datetime tidak ada
            setToZero(element);
            return;
        }

        var endTime = new Date(dateTime).getTime();
        if (isNaN(endTime)) {
            // Set ke "00" jika endTime tidak valid
            setToZero(element);
            return;
        }

        var daysElement = element.querySelector(".countdown-timer .day");
        var hoursElement = element.querySelector(".countdown-timer .hour");
        var minutesElement = element.querySelector(".countdown-timer .minute");
        var secondsElement = element.querySelector(".countdown-timer .second");

        function updateCountdown() {
            var now = new Date().getTime();
            var timeRemaining = endTime - now;

            if (timeRemaining <= 0) {
                clearInterval(interval);
                setToZero(element);
                return;
            }

            var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            var hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

            daysElement.textContent = days.toString().padStart(2, '0');
            hoursElement.textContent = hours.toString().padStart(2, '0');
            minutesElement.textContent = minutes.toString().padStart(2, '0');
            secondsElement.textContent = seconds.toString().padStart(2, '0');
        }

        var interval = setInterval(updateCountdown, 1000);
        updateCountdown();
    }

    // Fungsi untuk mengatur elemen countdown ke "00"
    function setToZero(element) {
        var daysElement = element.querySelector(".countdown-timer .day");
        var hoursElement = element.querySelector(".countdown-timer .hour");
        var minutesElement = element.querySelector(".countdown-timer .minute");
        var secondsElement = element.querySelector(".countdown-timer .second");

        daysElement.textContent = "00";
        hoursElement.textContent = "00";
        minutesElement.textContent = "00";
        secondsElement.textContent = "00";
    }

    // Memulai countdown untuk setiap elemen dengan kelas 'agenda-wrapper'
    var countdownElements = document.querySelectorAll(".agenda-wrapper");
    countdownElements.forEach(function(element) {
        displayCountdown(element);
    });
});
