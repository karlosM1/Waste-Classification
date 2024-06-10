document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel');
    let isDown = false;
    let startX;
    let scrollLeft;

    carousel.addEventListener('mousedown', (e) => {
        isDown = true;
        carousel.classList.add('active');
        startX = e.pageX - carousel.offsetLeft;
        scrollLeft = carousel.scrollLeft;
        carousel.style.cursor = 'grabbing';
    });

    carousel.addEventListener('mouseleave', () => {
        isDown = false;
        carousel.classList.remove('active');
        carousel.style.cursor = 'grab';
    });

    carousel.addEventListener('mouseup', () => {
        isDown = false;
        carousel.classList.remove('active');
        carousel.style.cursor = 'grab';
    });

    carousel.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - carousel.offsetLeft;
        const walk = (x - startX) * 1;
        carousel.scrollLeft = scrollLeft - walk;
    });


    const cards = document.querySelectorAll('.card');
    const middleIndex = Math.floor(cards.length / 2);
    const cardWidth = cards[0].offsetWidth;
    const containerWidth = document.querySelector('.container').offsetWidth;
    const offset = (containerWidth / 2) - (cardWidth / 2);

    carousel.scrollLeft = middleIndex * cardWidth - offset;
});
