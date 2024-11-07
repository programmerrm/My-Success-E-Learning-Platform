const formItem = document.querySelectorAll(".user-profile-info-change-form div");

if (formItem.length > 0) {
    formItem[1].classList.add("image-change-div");
    const icon = document.createElement("i");
    icon.classList.add("ri-image-edit-fill");
    formItem[1].appendChild(icon);
}
