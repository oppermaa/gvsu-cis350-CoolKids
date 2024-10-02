# CoolKids

Project description (~1 paragraph)

* This project is a unit conversion tool that supports both Imperial and Metric conversions. The tool allows users to input values and receive conversions for distance, volume, and weight. Additional features include dark mode support and location-based suggestions for measurement systems based on user location (e.g., Imperial or Metric). The tool is accessible via a web interface and can be extended with more features.


## Team Members and Roles

* [Adam Opperman](https://github.com/oppermaa/CIS350-HW2-opperman) (Captain, Testing, Visual Design, Documentation)
* [Shamurat (Shon) Raimbekov](https://github.com/opperman/CIS350-HW2-opperman) (Backend Development, Frontend Development, Backend Logic/DevOps)

## Prerequisites

## Prerequisites

To run this project, we will need the following:

- Python 3.x 
- Flask: Used for the web interface and backend.
- Git: Version control to clone the repository and manage code changes.
- HTML/CSS: For designing the frontend user interface.
- JavaScript: For interactivity in the frontend (if needed).
- Requests library: Used for location-based suggestions.
- ipinfo API: To determine the user's location based on IP for suggesting the appropriate measurement system.

 
## Run Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/raimbekov/gvsu-cis350-CoolKids.git
2. **Navigate to the project directory**:
   ```bash
   cd gvsu-cis350-CoolKids
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the application**:
   ```bash
   python app.py
5. **Access the web app**:
   - Open your browser and go to `http://localhost:5000` to use the unit conversion tool.
