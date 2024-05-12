// Function to dynamically load fonts
function loadFonts() {
    // Create a new link element for the font stylesheet
    var fontLink = document.createElement('link');
    fontLink.href = 'https://fonts.googleapis.com/css?family=Inter';
    fontLink.rel = 'stylesheet';

    // Add the font stylesheet to the head of the document
    document.head.appendChild(fontLink);

    // Set the font style to use the loaded font
    var fontStyle = document.createElement('style');
    fontStyle.innerHTML = 'body { font-family: "Inter", sans-serif; }';
    document.head.appendChild(fontStyle);

}

// Call the loadFonts function after the page has loaded
window.addEventListener('load', loadFonts);
