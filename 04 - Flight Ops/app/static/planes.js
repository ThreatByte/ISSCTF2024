const planeImages = [
    '/static/airplane.png',
    '/static/airplane2.png',
    '/static/airplane3.png',
    '/static/airplane4.png',
    // Add more image paths as needed
];

function generateRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generatePlanes() {
    const maxPlanes = generateRandomNumber(4, 7); // Generate 2 to 5 planes
    const body = document.querySelector('body');
    const existingPlanes = document.querySelectorAll('.plane');

    for (let i = 0; i < maxPlanes; i++) {
        if (existingPlanes.length >= maxPlanes) {
            // If the maximum number of planes is reached, remove the oldest plane
            body.removeChild(existingPlanes[i]);
        }

        const plane = document.createElement('img');
        const randomImage = planeImages[Math.floor(Math.random() * planeImages.length)];
        plane.src = randomImage;
        plane.classList.add('plane');

        // Random position on the screen
        plane.style.top = Math.random() * window.innerHeight + 'px';
        plane.style.left = Math.random() * window.innerWidth + 'px';

        // Random durations for fade-in, display, and fade-out
        const fadeInDuration = Math.random() * 2000 + 1000; // in milliseconds
        const displayDuration = Math.random() * 9000 + 4000; // in milliseconds
        const fadeOutDuration = Math.random() * 2000 + 1000; // in milliseconds

        // Fade-in effect after a random delay
        setTimeout(() => {
            plane.style.opacity = '1';
        }, fadeInDuration);

        // Fade-out effect after the display duration
        setTimeout(() => {
            plane.style.opacity = '0';
        }, fadeInDuration + displayDuration);

        // Remove the plane after fade-out
        setTimeout(() => {
            body.removeChild(plane);
        }, fadeInDuration + displayDuration + fadeOutDuration);

        body.appendChild(plane);
    }
}

generatePlanes()