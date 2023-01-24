// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["BIT", "BSIT", ],
        datasets: [{
            data: [65, 45],
            backgroundColor: ['#4e73df', '#17a673', '#36b9cc', ],
            hoverBackgroundColor: ['#CFF800', '#FC6238', '#FC6238', ],
            hoverBorderColor: "rgba(234, 236, 244, 254, 1,343)",
        }],
    },
    options: {
        maintainAspectRatio: false,
        tooltips: {
            backgroundColor: "rgb(255,255,255,)",
            bodyFontColor: "#FFFF ",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
        },
        legend: {
            display: false
        },
        cutoutPercentage: 60,
    },
});