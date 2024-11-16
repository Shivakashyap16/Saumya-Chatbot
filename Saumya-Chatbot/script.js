document.getElementById('chatForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let message = document.getElementById('message').value;

    fetch('http://127.0.0.1:5000/chat', {  // Use the correct URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        let messagesDiv = document.getElementById('messages');
        messagesDiv.innerHTML += `<div class="user-message">${message}</div>`;
        if (data.reply) {
            messagesDiv.innerHTML += `<div class="chatbot-reply">${data.reply}</div>`;
        } else if (data.error) {
            messagesDiv.innerHTML += `<div class="error-message">${data.error}</div>`;
        }
        document.getElementById('message').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
        let messagesDiv = document.getElementById('messages');
        messagesDiv.innerHTML += `<div class="error-message">Error: ${error.message}</div>`;
    });
});
