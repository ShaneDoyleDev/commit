const messages = document.querySelectorAll(".toast-message");

setTimeout(function () {
  messages.forEach((message) => (message.style.display = "none"));
}, 6000);
