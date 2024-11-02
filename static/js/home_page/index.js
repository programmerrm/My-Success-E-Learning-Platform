"use strict";

const bannerTitle = document.querySelector(".banner-title");
const titleText = bannerTitle.textContent;

const updatedTitleText = titleText
    .replace(/Earning/g, "<b>Earning</b>")
    .replace(/Learning/g, "");
    // .replace(/Learning/g, "<b>Learning</b>");

bannerTitle.innerHTML = updatedTitleText;

const menu = document.querySelector(".humbagar-menu");
const closeMenu = document.querySelector(".close-menu");
const nav = document.querySelector(".nav-bar-wrap");

menu.addEventListener("click", () => {
    nav.style.display = "flex";
});

closeMenu.addEventListener("click", () => {
    nav.style.display = "none";
});

