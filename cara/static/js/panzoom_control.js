const schemeElement = document.getElementById('scheme');

const panzoom = Panzoom(schemeElement, {
    maxScale: 3,
    minScale: 0.2,
    startScale: 0.55,
    startX: -600,
    startY: -600
});

schemeElement.style.transform = 'scale(0.35) translate(0, 45vh)';
schemeElement.addEventListener('wheel', panzoom.zoomWithWheel);

document.getElementById('to_home').addEventListener('click', () => {
    panzoom.reset({
        animate: true,
        duration: 200,
        easing: "easeInOut"
    });
    schemeElement.style.transformOrigin = '50% 50%';
    schemeElement.style.transition = 'transform 200ms ease-in-out';
    schemeElement.style.transform = 'scale(0.35) translate(0, 45vh)';
});