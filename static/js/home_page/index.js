"use strict";

const bannerTitle = document.querySelector(".banner-title");
const titleText = bannerTitle.textContent;

const updatedTitleText = titleText
    .replace(/Earning/g, "<b>Earning</b>")
    .replace(/Learning/g, "");
    // .replace(/Learning/g, "<b>Learning</b>");

bannerTitle.innerHTML = updatedTitleText;
