// Define an object containing each country with its associated measurement system
const countryMeasurementData = {
    "United States": "US Customary",
    "Liberia": "Imperial",
    "Myanmar": "Imperial",
    "Canada": "Metric",
    "United Kingdom": "Imperial",
    "France": "Metric",
    "Germany": "Metric",
    "Japan": "Metric",
    "Russia": "Metric",
    "India": "Metric",
    "Australia": "Metric",
    "Brazil": "Metric",
    "South Africa": "Metric",
    "China": "Metric",
    "Mexico": "Metric",
    "Argentina": "Metric",
    "Egypt": "Metric",
    "Italy": "Metric",
    "Saudi Arabia": "Metric",
    "Turkey": "Metric",
    // Add more countries as needed
};

// Function to get the measurement system based on selected country
function getMeasurementSystem(country) {
    return countryMeasurementData[country] || "Metric"; // Default to Metric if not listed
}

// Populate the country dropdown in the HTML with countries from the data
function populateCountryDropdown() {
    const countryDropdown = document.getElementById("country-dropdown");
    for (let country in countryMeasurementData) {
        let option = document.createElement("option");
        option.value = country;
        option.text = country;
        countryDropdown.add(option);
    }
}

// Display the measurement system suggestion based on selected country
function displayMeasurementSuggestion() {
    const selectedCountry = document.getElementById("country-dropdown").value;
    const suggestion = document.getElementById("measurement-suggestion");
    const system = getMeasurementSystem(selectedCountry);
    suggestion.textContent = `Suggested Measurement System: ${system}`;
}

// Call functions to populate dropdown and update suggestion
document.addEventListener("DOMContentLoaded", () => {
    populateCountryDropdown();
    const countryDropdown = document.getElementById("country-dropdown");
    countryDropdown.addEventListener("change", displayMeasurementSuggestion);
});

