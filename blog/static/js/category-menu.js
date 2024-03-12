// ---------------------
// DOM Selectors
// ---------------------
const categoryMenuItem = document.querySelectorAll(".category-menu-item");
const categoryMenuSelector = document.querySelectorAll(
  ".category-menu-selector"
);
const categoryMenuLine = document.querySelector(".category-menu-line");

// ---------------------
// Functions
// ---------------------
/**
 * Handles the mouseover event on a menu item.
 * Changes the border color of the menu selector and the background color of the menu line
 * based on the category of the current menu item.
 *
 * @param {Event} event - The mouseover event
 */
function handleMouseOver(event) {
  const category = event.currentTarget.dataset.category;
  if (category === "all-posts") return;

  categoryMenuSelector.forEach((item) => {
    item.style.setProperty(
      "border",
      `var(--clr-${category}-category) 3px solid`
    );
  });

  categoryMenuLine.style.setProperty(
    "background-color",
    `var(--clr-${category}-category)`
  );
}

/**
 * Handles the mouseout event on a menu item.
 * Resets the border color of the menu selector and the background color of the menu line to primary color.
 *
 * @param {Event} event - The mouseout event
 */
function handleMouseOut(event) {
  categoryMenuSelector.forEach((item) => {
    item.style.setProperty("border", "var(--clr-primary) 3px solid");
  });
  categoryMenuLine.style.setProperty("background-color", "var(--clr-primary)");
}

// ---------------------
// Event Listeners
// ---------------------
categoryMenuItem.forEach((item) => {
  item.addEventListener("mouseover", handleMouseOver);
  item.addEventListener("mouseout", handleMouseOut);
});
