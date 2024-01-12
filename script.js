function sendPublicMessage() {
    sendMessage('public-discussion-display', 'public-message-input', 'sent-message');
}

function sendMessage(displayId, inputId, messageClass) {
    var messageInput = document.getElementById(inputId);
    var message = messageInput.value.trim();

    if (message !== '') {
        var discussionDisplay = document.getElementById(displayId);

        var messageContainer = document.createElement('div');
        messageContainer.className = 'message ' + messageClass;

        var messageText = document.createElement('p');
        var textNode = document.createTextNode('You: ' + message);
        messageText.appendChild(textNode);

        var replyButton = document.createElement('button');
        replyButton.className = 'reply-button';
        replyButton.innerHTML = 'Reply';
        replyButton.onclick = function() {
            replyToMessage(this);
        };

        messageContainer.appendChild(messageText);
        messageContainer.appendChild(replyButton);

        discussionDisplay.appendChild(messageContainer);

        messageInput.value = '';
        messageInput.focus();

        discussionDisplay.scrollTop = discussionDisplay.scrollHeight;

        var replyButtons = document.querySelectorAll('.reply-button');
        replyButtons.forEach(function(button) {
            button.style.display = 'inline-block';
        });
    }
}

function replyToMessage(button) {
    var parentMessage = button.parentElement;
    var originalMessage = parentMessage.querySelector('p').innerText;
    var replyInput = document.getElementById('public-message-input');

    // تجنب تنفيذ HTML غير آمن
    replyInput.value += '\n@' + originalMessage.split(':')[1].trim() + ' ';
    replyInput.focus();

    var replyButtons = document.querySelectorAll('.reply-button');
    replyButtons.forEach(function(button) {
        button.style.display = 'none';
    });
}
