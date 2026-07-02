// Allow pressing Enter to send message
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendToFlask();
});

async function sendToFlask() {
    const inputElement = document.getElementById('userInput');
    const prompt = inputElement.value.trim();
    const chatbox = document.getElementById('chatbox');

    if (!prompt) return;

    // Add user message
    chatbox.innerHTML += `
        <div class="message-row user-row">
            <div class="bubble user-bubble">${prompt}</div>
        </div>
    `;

    inputElement.value = '';
    chatbox.scrollTop = chatbox.scrollHeight;

    // Thinking bubble
    const thinkingId = "thinking-" + Date.now();
    chatbox.innerHTML += `
        <div class="message-row bot-row" id="${thinkingId}">
            <div class="bubble bot-bubble"><i>Thinking...</i></div>
        </div>
    `;

    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();

        document.getElementById(thinkingId).remove();

        chatbox.innerHTML += `
            <div class="message-row bot-row">
                <div class="bubble bot-bubble">${data.response}</div>
            </div>
        `;
    } catch (error) {
        document.getElementById(thinkingId).remove();

        chatbox.innerHTML += `
            <div class="message-row bot-row">
                <div class="bubble bot-bubble" style="color:red;">
                    Error processing your request.
                </div>
            </div>
        `;
    }

    chatbox.scrollTop = chatbox.scrollHeight;
}

// Clear chat function (FIXED POSITION)
function clearChat() {
    fetch('/clear', { method: 'POST' })
    .then(() => {
        document.getElementById('chatbox').innerHTML = `
            <div class="message-row bot-row">
                <div class="bubble bot-bubble">
                    Chat cleared. Start again!
                </div>
            </div>
        `;
    });
}