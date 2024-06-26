
async function fetchLocation() {
    try {
        const response = await fetch('http://ip-api.com/json/');
        const data = await response.json();
        document.getElementById('location').innerText = `Location: ${data.city}, ${data.regionName}, ${data.country}`;
    } catch (error) {
        console.error('Error fetching location:', error);
    }
}

// Event listener for webcam access
document.getElementById('webcamButton').addEventListener('click', () => {
    const video = document.querySelector('video');
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                video.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing webcam:', error);
            });
    }
});


document.getElementById('microphoneButton').addEventListener('click', () => {
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then((stream) => {
                const mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();
                mediaRecorder.ondataavailable = (e) => {
                    const audioChunks = [];
                    audioChunks.push(e.data);
                    if (mediaRecorder.state === 'inactive') {
                        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                        const audioUrl = URL.createObjectURL(audioBlob);
                        const audio = new Audio(audioUrl);
                        audio.play();
                    }
                };


document.getElementById('snapshotButton').addEventListener('click', () => {
    const video = document.querySelector('video');
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    const dataURL = canvas.toDataURL('image/png');
    
    fetch('save_snapshot.php', {
        method: 'POST',
        body: JSON.stringify({ image: dataURL }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.text())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
});

                setTimeout(() => {
                    mediaRecorder.stop();
                }, 5000); 
            })
            .catch((error) => {
                console.error('Error accessing microphone:', error);
            });
    }
});


window.onload = fetchLocation;
