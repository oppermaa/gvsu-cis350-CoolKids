document.addEventListener("DOMContentLoaded", () => {
    const themeSwitch = document.getElementById("theme-switch");
    const fontDecrease = document.getElementById("font-decrease");
    const fontDefault = document.getElementById("font-default");
    const fontIncrease = document.getElementById("font-increase");

    // Load preferences from localStorage
    const savedTheme = localStorage.getItem("theme");
    const savedFontSize = localStorage.getItem("font-size");

    // Apply saved theme
    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
        if (themeSwitch) themeSwitch.checked = true;
    }

    // Apply saved font size
    if (savedFontSize === "small") {
        document.body.classList.add("font-small");
    } else if (savedFontSize === "large") {
        document.body.classList.add("font-large");
    }

    // Theme Toggle
    if (themeSwitch) {
        themeSwitch.addEventListener("change", () => {
            if (themeSwitch.checked) {
                document.body.classList.add("dark-mode");
                localStorage.setItem("theme", "dark");
            } else {
                document.body.classList.remove("dark-mode");
                localStorage.setItem("theme", "light");
            }
        });
    }

    // Font Size Adjustment
    if (fontDecrease) {
        fontDecrease.addEventListener("click", () => {
            document.body.classList.remove("font-large");
            document.body.classList.add("font-small");
            localStorage.setItem("font-size", "small");
        });
    }

    if (fontDefault) {
        fontDefault.addEventListener("click", () => {
            document.body.classList.remove("font-small", "font-large");
            localStorage.setItem("font-size", "default");
        });
    }

    if (fontIncrease) {
        fontIncrease.addEventListener("click", () => {
            document.body.classList.remove("font-small");
            document.body.classList.add("font-large");
            localStorage.setItem("font-size", "large");
        });
    }
});
