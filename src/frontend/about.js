// about.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("About Us page loaded");

    // Apply the saved theme mode
    const isDarkMode = localStorage.getItem("dark-mode") === "true";
    document.body.classList.toggle("dark-mode", isDarkMode);
    document.getElementById("theme-switch").checked = isDarkMode;

    // Apply the saved font size
    const fontSize = localStorage.getItem("font-size");
    if (fontSize) {
        document.body.classList.add(fontSize);
    }

    // Event listener for theme switch
    const themeSwitch = document.getElementById("theme-switch");
    themeSwitch.addEventListener("change", () => {
        const isChecked = themeSwitch.checked;
        document.body.classList.toggle("dark-mode", isChecked);
        localStorage.setItem("dark-mode", isChecked);
    });

    // Event listeners for font size buttons
    const fontDecrease = document.getElementById("font-decrease");
    const fontDefault = document.getElementById("font-default");
    const fontIncrease = document.getElementById("font-increase");

    fontDecrease.addEventListener("click", () => {
        document.body.classList.remove("font-large");
        document.body.classList.add("font-small");
        localStorage.setItem("font-size", "font-small");
    });

    fontDefault.addEventListener("click", () => {
        document.body.classList.remove("font-small", "font-large");
        localStorage.setItem("font-size", "");
    });

    fontIncrease.addEventListener("click", () => {
        document.body.classList.remove("font-small");
        document.body.classList.add("font-large");
        localStorage.setItem("font-size", "font-large");
    });
});
