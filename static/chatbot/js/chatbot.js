const messagesList = document.querySelector('.messages-list');
const messageForm = document.querySelector('.message-form');
const messageInput = document.querySelector('.message-input');

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (message.length === 0) {
        return;
    }

    const messageItem = document.createElement('li');
    messageItem.classList.add('message', 'sent');
    messageItem.innerHTML = `
    <div class="message-text">
        <div class="message-sender">
            <b>You</b>
        </div>
        <div class="message-content">
            ${message}
        </div>
    </div>`;
    messagesList.appendChild(messageItem);

    messageInput.value = '';

    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'message': message
        })
    })
        .then(response => response.json())
        .then(data => {
            const response = data.response;

            var parts = response.split("```");
            var regularText = parts[0];
            var jsonData = parts[1];

            console.log(response);
            console.log("---------------");
            console.log(parts);
            console.log("---------------");
            console.log(regularText);
            console.log("---------------");
            console.log(jsonData);

            const messageItem = document.createElement('li');
            messageItem.classList.add('message', 'received');
            messageItem.innerHTML = `
                <div class="message-text">
                    <div class="message-sender">
                    <b>AI Chatbot</b>
                    </div>
                    <div>
                        <pre class="message-content">
                            ${response}
                        </pre>
                    </div>
                </div>
                `;
            messagesList.appendChild(messageItem);
        });
});