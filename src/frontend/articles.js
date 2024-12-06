// articles.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("Articles page loaded");

    // Preserve the dark mode and font size settings across pages
    const themeSwitch = document.getElementById("theme-switch");
    const applyTheme = (isDark) => {
        document.body.classList.toggle("dark-mode", isDark);
    };

    // Check and apply saved settings from localStorage
    const savedTheme = localStorage.getItem("dark-mode") === "true";
    applyTheme(savedTheme);

    const savedFontSize = localStorage.getItem("font-size");
    if (savedFontSize) {
        document.body.classList.remove("font-small", "font-large");
        if (savedFontSize === "small") {
            document.body.classList.add("font-small");
        } else if (savedFontSize === "large") {
            document.body.classList.add("font-large");
        }
    }

    // Listen for theme toggle switch changes
    if (themeSwitch) {
        themeSwitch.checked = savedTheme;
        themeSwitch.addEventListener("change", () => {
            const isDark = themeSwitch.checked;
            localStorage.setItem("dark-mode", isDark);
            applyTheme(isDark);
        });
    }
});
