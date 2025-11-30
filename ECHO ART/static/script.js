// Handle text-to-image generation
function generateImage() {
  const text = document.getElementById("textInput").value;
  if (!text) {
    alert("Please enter some text first.");
    return;
  }

  fetch("/generate-image", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text })
  })
  .then(response => response.json())
  .then(data => {
    if (data.message) {
      document.getElementById("output").innerText = data.message;
    } else {
      document.getElementById("output").innerText = "Error: " + data.error;
    }
  })
  .catch(error => {
    document.getElementById("output").innerText = "Error: " + error;
  });
}

// Handle voice-to-text conversion
function uploadVoice() {
  const fileInput = document.getElementById("voiceInput");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please select an audio file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  fetch("/voice-to-text", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.text) {
      document.getElementById("output").innerText = "Voice to Text: " + data.text;
    } else {
      document.getElementById("output").innerText = "Error: " + data.error;
    }
  })
  .catch(error => {
    document.getElementById("output").innerText = "Error: " + error;
  });
}
