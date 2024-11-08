"use strict"

const subAdminImage = document.querySelector(".profile-image img");
const profileSubMenu = document.querySelector(".profile-sub-menu");

let currentStep = false;

subAdminImage.addEventListener("click", () => {
    if(currentStep) {
        profileSubMenu.style.display = "none";
        return currentStep = false;
    } else {
        profileSubMenu.style.display = "block";
        return currentStep = true;
    }
});

const subMenuItem = document.querySelectorAll(".sub-menu-item");

subMenuItem.forEach((item) => {
    let currentStep = false;
    item.addEventListener("click", () => {
        const thisItem = item.closest(".sub-menu-item");
        let arrowIcon = thisItem.querySelector(".sub-menu-item .right-arrow");
        let menuItem = thisItem.querySelector(".menu-item");
        if (!currentStep) {
            arrowIcon.style.transform = "rotate(90deg)";
            menuItem.style.display = "flex";
            return currentStep = true;
        } else {
            arrowIcon.style.transform = "rotate(0deg)";
            menuItem.style.display = "none";
            return currentStep = false;
        }        
    });
});

const closeSidebar = document.querySelector(".close-side-bar");
const openSideBar = document.querySelector(".open-side-bar");
const sideBar = document.querySelector(".side-bar-sub-admin");

const handleSideBar = () => {

    openSideBar.addEventListener("click", () => {
    });

    closeSidebar.addEventListener("click", () => {

    });
}

handleSideBar();


console.log("sub admin page");