function sendEmotionData() {
    var textToAnalyze = document.getElementById("textToAnalyze").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("result").style.display = "block";
            document.getElementById("result").innerHTML = xhttp.responseText;
        } else if (this.readyState == 4 && this.status == 400) {
            document.getElementById("result").style.display = "block";
            document.getElementById("result").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
