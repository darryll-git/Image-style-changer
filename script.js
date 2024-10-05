function applyStyle() {
    const imageInput = document.getElementById('imageInput');
    const styleSelect = document.getElementById('styleSelect');
    const resultContainer = document.getElementById('resultContainer');

    const file = imageInput.files[0];
    const style = styleSelect.value;

    if (file) {
        const formData = new FormData();
        formData.append('image', file);
        formData.append('style', style);

        // Make a request to your backend API for style transfer
        fetch('your_backend_api_url', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Display the styled image in the result container
            resultContainer.innerHTML = `<img src="${data.styledImage}" alt="Styled Image">`;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please select an image');
    }
}
