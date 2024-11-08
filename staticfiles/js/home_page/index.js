"use strict";

const texts = ["Learning", "Earning"];
const animationContainer = document.querySelector(".banner-text-animation");

function generateText(text) {
    animationContainer.innerHTML = '';
    const arr = text.split("");

    arr.forEach((char) => {
        const span = document.createElement("span");
        span.classList.add("char");
        span.innerHTML = char;
        animationContainer.appendChild(span);
    });
}

function animateText(text) {
    generateText(text);

    const tl = gsap.timeline({
        onComplete: () => {
            const nextIndex = (texts.indexOf(text) + 1) % texts.length;
            animateText(texts[nextIndex]);
        }
    });
    tl.from(".char", {
        y: -50,
        opacity: 0,
        stagger: 0.05,
        delay: 0.2,
        ease: "back.out",
        duration: 1,
    });
}

animateText(texts[0]);

const openMenu = document.querySelector(".menu-open-btn");
const closeMenu = document.querySelector(".menu-close-btn");
const menuItem = document.querySelector(".nav-wrap");

const handleMenuAnimation = () => {
    const tl = gsap.timeline({ paused: true });

    tl.to(menuItem, {
        right: 0,
    }).from(".nav-wrap ul li", {
        opacity: 0,
        x: 150,
        stagger: 0.2,
        duration: 0.6,
    });

    openMenu.addEventListener("click", () => {
        tl.play();
        console.log("Open menu");
    });

    closeMenu.addEventListener("click", () => {
        tl.reverse();
        console.log("Close menu");
    });
}

const checkViewportSize = () => {
    if (window.innerWidth <= 767) {
        handleMenuAnimation();
    }
}

checkViewportSize();
window.addEventListener('resize', checkViewportSize);