document.addEventListener("DOMContentLoaded", () => {
    // Element references
    const conversionTypeSelect = document.getElementById("conversion-type");
    const fromUnitSelect = document.getElementById("from-unit");
    const toUnitSelect = document.getElementById("to-unit");
    const convertButton = document.getElementById("convert-button");
    const inputValueElement = document.getElementById("input-value");
    const outputValueElement = document.getElementById("output-value");

    // Unit options by conversion type
    const unitOptions = {
        length: ["Kilometer", "Meter", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        mass: ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce"],
        volume: ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce"],
        time: ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"],
        area: ["Square Meter", "Square Kilometer", "Square Mile", "Acre", "Hectare"],
        "data-transfer-rate": ["Bit per Second", "Kilobit per Second", "Megabit per Second", "Gigabit per Second"],
        "digital-storage": ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"],
        frequency: ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
        "fuel-economy": ["Miles per Gallon", "Kilometers per Liter", "Liters per 100 Kilometer"],
        energy: ["Joule", "Kilojoule", "Watt Hour", "Kilowatt Hour", "Calorie"],
        "plane-angle": ["Degree", "Radian", "Gradian"],
        pressure: ["Pascal", "Bar", "Atmosphere", "Pound per Square Inch", "Torr"],
        speed: ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Knots"],
        temperature: ["Celsius", "Fahrenheit", "Kelvin"],
    };

    // Event listener for conversion type selection
    conversionTypeSelect.addEventListener("change", () => {
        const selectedType = conversionTypeSelect.value;

        console.log(`Selected Conversion Type: ${selectedType}`); // Debug log

        // Clear the "From" and "To" dropdowns
        fromUnitSelect.innerHTML = "<option value=''>--Select Unit--</option>";
        toUnitSelect.innerHTML = "<option value=''>--Select Unit--</option>";

        // Populate the "From" and "To" dropdowns based on selected type
        if (unitOptions[selectedType]) {
            unitOptions[selectedType].forEach(unit => {
                const fromOption = document.createElement("option");
                const toOption = document.createElement("option");

                fromOption.value = unit.toLowerCase().replace(/ /g, "_"); // Match backend formatting
                fromOption.textContent = unit;

                toOption.value = unit.toLowerCase().replace(/ /g, "_");
                toOption.textContent = unit;

                fromUnitSelect.appendChild(fromOption);
                toUnitSelect.appendChild(toOption);
            });
        }
    });

    // Conversion button logic
    convertButton.addEventListener("click", () => {
        const fromUnit = fromUnitSelect.value; // Already formatted
        const toUnit = toUnitSelect.value;
        const inputValue = parseFloat(inputValueElement.value);

        // Input validation
        if (!fromUnit || !toUnit || isNaN(inputValue)) {
            alert("Please select valid units and enter a valid number.");
            return;
        }

        console.log(`Converting: ${inputValue} ${fromUnit} to ${toUnit}`); // Debug log

        // Send data to the backend for conversion
        fetch("/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                from_unit: fromUnit,
                to_unit: toUnit,
                value: inputValue,
            }),
        })
            .then(response => {
                console.log(`Response Status: ${response.status}`); // Debug log
                return response.json();
            })
            .then(data => {
                console.log("Received Data:", data); // Debug log
                if (data.result) {
                    outputValueElement.value = data.result.toFixed(2);
                } else if (data.error) {
                    alert(`Error: ${data.error}`);
                }
            })
            .catch(error => {
                console.error("Fetch Error:", error);
                alert("An error occurred while performing the conversion.");
            });
    });
});
