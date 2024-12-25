function toggleModelOptions() {
    const manualRadio = document.getElementById("manual");
    const modelOptionsDiv = document.getElementById("model-options");

    if (manualRadio.checked) {
        modelOptionsDiv.style.display = "block";
    } else {
        modelOptionsDiv.style.display = "none";
    }
}
