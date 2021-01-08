const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-list');

    burger.addEventListener('click', () => {
        console.log('clicked');
        nav.classList.toggle('nav-active');
    });
}

navSlide();