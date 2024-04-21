// popupHandler.js
function showPopup() {
    var popup = document.querySelector('.popupblock');
    if (popup) {
        popup.style.display = 'block'; // Make the popup visible
        popup.style.opacity = 1; // Ensure it is fully visible
    }
}

function closePopup() {
    var popup = document.querySelector('.popupblock');
    if (popup) {
        popup.style.opacity = 0; // Start fade out
        setTimeout(function () {
            popup.style.display = 'none'; // Hide the popup after the fade effect
        }, 500); // Adjust time to match CSS transition
    }
}
