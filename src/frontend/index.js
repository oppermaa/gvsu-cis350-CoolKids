/* General reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

/* Body styling */
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f4f4f9;
    color: #333;
    padding: 20px;
    min-height: 100vh;
}

/* Header section */
header {
    text-align: center;
    margin-bottom: 20px;
}

header h1 {
    font-size: 2rem;
    color: #333;
}

header p {
    margin: 10px 0;
    font-size: 1rem;
    color: #666;
}

/* Main container for the form */
.converter-container {
    width: 100%;
    max-width: 500px;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

/* Dropdowns and inputs */
label {
    display: block;
    font-size: 1rem;
    margin-top: 15px;
    color: #333;
}

select, input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
}

/* Button styling */
button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    margin-top: 15px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #45a049;
}

/* Output section */
#output-value {
    margin-top: 15px;
    font-size: 1.2rem;
    color: #333;
    text-align: center;
    font-weight: bold;
}

/* Horizontal line separator */
hr {
    width: 100%;
    border: none;
    border-top: 2px solid #ddd;
    margin: 20px 0;
}

/* Responsive adjustments */
@media (max-width: 500px) {
    .converter-container {
        padding: 15px;
    }
}
