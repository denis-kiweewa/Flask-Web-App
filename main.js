<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coffee Quality Monitoring</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Coffee Quality Monitoring Interface</h1>
        <div class="data-section">
            <div class="image-container">
                <img id="captured-image" src="#" alt="Captured Image">
            </div>
            <div class="sensor-data">
                <h2>Sensor Data</h2>
                <p id="temperature">Temperature: --</p>
                <p id="humidity">Humidity: --</p>
            </div>
        </div>
        <div class="user-input">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="profession">Profession:</label>
            <input type="text" id="profession" name="profession" required>
        </div>
        <div class="buttons">
            <button id="detect-button">Detect</button>
            <button id="prediction-button">Make Prediction</button>
        </div>
    </div>
    <script src="main.js"></script>
</body>
</html>
