
function new_chart(legenda, tc, hum, press) {



temp = {
        label: 'Temperatura',
            fill: true,
            lineTension: 0.1,
            backgroundColor: "rgba(255,38,38,0.05)",
            borderColor: "rgba(255,38,38,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(255,38,38,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(255,38,38,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data : tc,
            spanGaps: false
        }

var humid = {
        label: 'Umidade',
            fill: true,
            lineTension: 0.1,
            backgroundColor: "rgba(100,162,162,0.01)",
            borderColor: "rgba(100,162,162,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(100,162,162,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(100,162,162,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data : hum,
            spanGaps: false
        }
var par = {
        label: 'Luminosidade',
            fill: true,
            lineTension: 0.1,
            backgroundColor: "rgba(0,255,128,0.05)",
            borderColor: "rgba(0,255,128,1)",
            borderCapStyle: 'butt',
            borderDash: ['.','-'],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(0,255,128,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(0,255,128,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data : press,
            spanGaps: false
        }

var chartData = {
  labels : legenda,
        datasets : [temp, humid, par]
      }

      var ctx = document.getElementById("chart").getContext("2d");

      // create the chart using the chart canvas
      var myChart = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
          scales: {
              xAxes: [{
                  display: false
              }]
        }
    }
      });

    }