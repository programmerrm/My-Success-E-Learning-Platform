const formItem = document.querySelectorAll(".user-profile-info-change-form div");

if (formItem.length > 0) {
    formItem[1].classList.add("image-change-div");
    const icon = document.createElement("i");
    icon.classList.add("ri-image-edit-fill");
    formItem[1].appendChild(icon);
}

const copyLinkUrl = document.querySelector(".copy-link-url p");
const copyLinkButton = document.querySelector(".copy-link-url button");

copyLinkButton.addEventListener("click", () => {
    const tempTextarea = document.createElement("textarea");
    tempTextarea.value = copyLinkUrl.textContent;
    document.body.appendChild(tempTextarea);
    tempTextarea.select();
    document.execCommand("copy");
    document.body.removeChild(tempTextarea);
    alert("Link successfully copied!");
});
