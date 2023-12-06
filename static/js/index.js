// index.js
document.addEventListener("DOMContentLoaded", function() {
  // Function to show Django messages as alerts
  function showMessagesAsAlerts() {
      var messagesContainer = document.getElementById('django-messages');
      if (messagesContainer) {
          var messages = messagesContainer.dataset.messages;
          if (messages) {
              // Split messages by newline and show alerts
              messages.split('\n').forEach(function(message) {
                  if (message.trim() !== "") {
                      alert(message);
                  }
              });
          }
      }
  }

  // Call the function to show messages as alerts
  showMessagesAsAlerts();
});
