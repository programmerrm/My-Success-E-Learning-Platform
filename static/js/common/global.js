"use strict";

setTimeout(() => {
    const messages = document.querySelectorAll('.messages li');
    messages.forEach(function (message) {
        message.style.display = 'none';
    });
}, 4000);