const socket1 = new WebSocket("ws://localhost:8765/weather");
const socket = new WebSocket("ws://localhost:8765/forescast");

let temperatureChart
let temperatureChart1
const forescast =(weatherData) =>{
  const day8Data = weatherData.list;
  const day8Forecast = document.getElementById("8-day-forecast");
  day8Forecast.innerHTML = ""; // Xóa nội dung cũ
  currentday = new Date("2023-11-03");
  
  day8Data.forEach((dayData) => {
    const date = new Date(dayData.dt * 1000);
    const temperature = dayData.main.temp;
    const description = dayData.weather[0].description;
    const humidity = dayData.main.humidity;
    const windspeed = dayData.wind.speed;
    const pop= dayData.pop*100;
    const day2 = date.getDate();
    // Tạo một biến để lưu đường dẫn hình ảnh
    let weatherIconSrc = "";
    const keywordsToCheckrain = ["light rain"];
    const keywordsToCheckclouds = ["broken clouds", "overcast clouds", "scattered clouds","few clouds" ];
    const containsKeywordsrain = keywordsToCheckrain.some(keyword => description.toLowerCase().includes(keyword));
    const containsKeywordsclouds = keywordsToCheckclouds.some(keyword => description.toLowerCase().includes(keyword));
    if (containsKeywordsrain) {
      weatherIconSrc = "muanho.png";
    } else if (containsKeywordsclouds) {
      weatherIconSrc = "maytrang.png";
    }else{
      weatherIconSrc = "nangnong.png";
    }
    if (day2 != currentday.getDate()) {
      const dayCard = document.createElement("div");
      dayCard.classList.add("day-card");
      dayCard.innerHTML = `
                          <p>thời tiết:${description}</p>
                          <p>nhiệt độ: ${temperature}°C</p>
                          <p>độ ẩm: ${humidity}%</p>
                          <p>tốc độ gió: ${windspeed}m/s</p>
                          <p>xác xuất mưa: ${Math.floor(pop)}%</p>
                          <img src="${weatherIconSrc}" alt="${description}"> <!-- Thêm hình ảnh thời tiết -->
                      `;
      day8Forecast.appendChild(dayCard);
      currentday = date;
    }
  });
}
const forescastchart= (weatherData)=>{
  // Lấy thẻ canvas và dữ liệu nhiệt độ và thời gian
  const day8Data = weatherData.list;
  const temperatureCanvas = document.getElementById("temperature-chart");
  const temperatureCanvas1 = document.getElementById("temperature-chart1");
  const temperatureData = [];
  const timeLabels = [];
  const windata = [];
  let currentDate1 = null;


  day8Data.forEach((dayData) => {
    const date = new Date(dayData.dt * 1000);
    const day = date.getDate();
    const day2 = date.toLocaleDateString();

    if (currentDate1 === null || day !== currentDate1) {
      temperatureData.push(dayData.main.temp);
      windata.push(dayData.wind.speed);
      timeLabels.push(day2);
      currentDate1 = day;
    }
  });
  updateTemperatureChart(temperatureChart, temperatureCanvas, timeLabels, temperatureData,"Nhiệt độ (°C)","rgba(211, 84, 0,1.0)","rgba(255, 190, 118,1.0)")
  updateTemperatureChart(temperatureChart1, temperatureCanvas1, timeLabels, windata,"Tốc độ gió(m/s","rgba(9, 132, 227,1.0)","rgba(129, 236, 236,1.0)")
}
const updateTemperatureChart=(temperatureChart, temperatureCanvas, timeLabels, temperatureData,labels,color1,color2)=> {
  if (temperatureChart) {
    temperatureChart.data.labels = timeLabels;
    temperatureChart.data.datasets[0].data = temperatureData;
    temperatureChart.update();
  } else {
    temperatureChart = new Chart(temperatureCanvas, {
      type: "line",
      data: {
        labels: timeLabels,
        datasets: [
          {
            label: labels,
            data: temperatureData,
            borderColor: color1,
            borderWidth: 2,
            tension: 0.4,
            fill: true,
            backgroundColor: color2,
          },
        ],
      },
      options: {
        scales: {
          x: {
            position: 'top',
            title: {
              display: true,
            },
          },
          y: {
            title: {
              display: true,
              text: labels,
            },
          },
        },
      },
    });
  }
}

const info=(weatherData)=>{
  
  let weatherIconSrc1 = "";
  const action= document.getElementById("action");
  const description=weatherData.weather[0].description;
  action.innerHTML="";
  const keywordsToCheckrain = ["light rain"];
    const keywordsToCheckclouds = ["broken clouds", "overcast clouds", "scattered clouds","few clouds" ];
    const containsKeywordsrain = keywordsToCheckrain.some(keyword => description.toLowerCase().includes(keyword));
    const containsKeywordsclouds = keywordsToCheckclouds.some(keyword => description.toLowerCase().includes(keyword));
    if (containsKeywordsrain) {
      weatherIconSrc1 = "muanho.png";
    } else if (containsKeywordsclouds) {
      weatherIconSrc1 = "maytrang.png";
    }else{
      weatherIconSrc1 = "nangnong.png";
    }
  const weatherInfo = document.createElement("div");
  if(weatherData.main.temp>=30)
  {
    var tam= "Quá nóng";
    var tam1= "Dự kiến khu vực nóng gay gắt";
  }
  else if(weatherData.main.temp<30 && weatherData.main.temp>24)
  {
    var tam= "Mát mẻ";
    var tam1="Dự kiến khu vực sẽ rất mát mẻ thích hợp cho các hoạt động ngoài trời";
  }
  else{
    var tam= "Thời tiết lạnh";
    var tam1="Dự kiến khu vực bắt đầu se lạnh nhớ mặc áo ấm";
  }
  weatherInfo.classList.add("weather-info");
  weatherInfo.innerHTML =
  `
  <center><div class="pill_1"><p>Thời tiết ở : ${weatherData.name}, ${weatherData.sys.country}</p>
  </div></center>
  <img height="100"  src="${weatherIconSrc1}" ><br> <!-- Thêm hình ảnh thời tiết -->
  <p>Nhiệt độ: ${weatherData.main.temp}°C</p>
  <p>Thời tiết: ${description}</p>
  <p>Độ ẩm: ${weatherData.main.humidity}%</p>
  <p>Tốc độ gió: ${weatherData.wind.speed} m/s</p>
  <div class = "conclude"><div class="pill_2"><p>${tam}</p></div>
  <div class="pill_2_p">${tam1}</div></div>
`;
action.appendChild(weatherInfo);
}

socket.onmessage = function (event) {
  const weatherData = JSON.parse(event.data);
  forescast(weatherData);
  forescastchart(weatherData);
};

socket1.onmessage = function (event) {
  const weatherData = JSON.parse(event.data);
  info(weatherData);
};

document.addEventListener("DOMContentLoaded", function () {
  const temperatureChart = document.getElementById("temperature-chart");
  const temperatureChart1 = document.getElementById("temperature-chart1");
  const temperatureBtn = document.getElementById("temperature-btn");
  const windBtn = document.getElementById("wind-btn");
  const btnsearch = document.getElementById("btnsearch");
  const chart1 = document.getElementById("chart1");
  const btn8day=document.getElementById("btn8day");
  temperatureChart1.style.display = "none";
  chart1.style.display = "none";
  btn8day.style.display = "none";
  btnsearch.addEventListener("click", function () {
    const city = document.getElementById("city").value;
    socket.send(city);
    socket1.send(city);
    chart1.style.display = "block";
    btn8day.style.display = "block";
  });
  temperatureBtn.addEventListener("click", function () {
    temperatureChart1.style.display = "none";
    temperatureChart.style.display = "block";
  });

  windBtn.addEventListener("click", function () {
    temperatureChart.style.display = "none";
    temperatureChart1.style.display = "block";
  });
});




