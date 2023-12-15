document.addEventListener('DOMContentLoaded', function() {
    const circleCursor = document.querySelector('.circle-cursor');
    circleCursor.style.transform = 'scale(0)';
    const hoverElement = document.querySelector('.ucat-selection');
    const hoverElement2 = document.querySelector('.interview-selection');

    hoverElement.addEventListener('mouseover', function() {
        circleCursor.style.transform = 'scale(1)';
    });

    hoverElement.addEventListener('mouseout', function() {
        circleCursor.style.transform = 'scale(0)';
    });

    hoverElement2.addEventListener('mouseover', function() {
        circleCursor.style.transform = 'scale(1)';
    });

    hoverElement2.addEventListener('mouseout', function() {
        circleCursor.style.transform = 'scale(0)';
    });

    document.addEventListener('mousemove', function(e) {
        const { clientX, clientY } = e;
        circleCursor.style.left = `${clientX}px`;
        circleCursor.style.top = `${clientY}px`;
    });
});
