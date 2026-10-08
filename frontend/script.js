const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const temperature = Number(document.getElementById("temperature").value);
    const humidity = Number(document.getElementById("humidity").value);
    const windSpeed = Number(document.getElementById("wind_speed").value);
    const isWeekend = Number(document.getElementById("is_weekend").value);

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            temperature: temperature,
            humidity: humidity,
            wind_speed: windSpeed,
            is_weekend: isWeekend
        })
    });

    const data = await response.json();

    result.textContent =
        "Expected Hot Chocolate Sales: " + data.prediction.toFixed(2);
});