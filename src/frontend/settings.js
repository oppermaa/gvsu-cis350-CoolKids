document.addEventListener("DOMContentLoaded", () => {
    const themeSwitch = document.getElementById("theme-switch");
    const fontDecrease = document.getElementById("font-decrease");
    const fontDefault = document.getElementById("font-default");
    const fontIncrease = document.getElementById("font-increase");

    // Theme Toggle
    themeSwitch.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode", themeSwitch.checked);
    });

    // Font Size Adjustment
    fontDecrease.addEventListener("click", () => {
        document.body.classList.remove("font-large");
        document.body.classList.add("font-small");
    });

    fontDefault.addEventListener("click", () => {
        document.body.classList.remove("font-small", "font-large");
    });

    fontIncrease.addEventListener("click", () => {
        document.body.classList.remove("font-small");
        document.body.classList.add("font-large");
    });
});
