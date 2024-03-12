// ---------------------
// DOM Selectors
// ---------------------
const navbarDropdown = document.querySelector(".navbar-dropdown");
const navbarHamburgerBtn = document.querySelector(".navbar-hamburger-btn");
const navbarCloseBtn = document.querySelector(".navbar-close-btn");

// ---------------------
// Event Listeners
// ---------------------
navbarHamburgerBtn.addEventListener("click", function () {
  navbarDropdown.classList.add("show-navbar-dropdown");
});

navbarCloseBtn.addEventListener("click", function () {
  navbarDropdown.classList.remove("show-navbar-dropdown");
});

