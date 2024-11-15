// static/js/dashboard/ChartStatistik.js
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('myChart').getContext('2d');
    var chartData = window.chartData; // Mengambil data dari objek global
    var myChart = new Chart(ctx, {
        type: 'bar', // Jenis grafik: bar, line, pie, dll.
        data: {
            labels: ['Total Undanganku', 'Total Tamu', 'Ucapan & Do\'a', 'Sisa Kuota Undangan'],
            datasets: [{
                label: 'Statistics',
                data: [chartData.invitationsCount, chartData.tamuUndanganCount, chartData.rsvpCount, chartData.kuotaUndanganSisa],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
