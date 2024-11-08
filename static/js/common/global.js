"use strict";

const headerSection = document.querySelector(".header-section");

function handleHeaderSection() {
    if (window.scrollY > 50) {
        headerSection.classList.add("sticky");
    } else {
        headerSection.classList.remove("sticky");
    }
}

window.onscroll = function () { handleHeaderSection() }
