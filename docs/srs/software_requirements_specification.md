# Team Name:
**Coolkids**

# Team Members:
- Adam Opperman
- Shamurat (Shon) Raimbekov

# Software Requirements Specification (SRS)

## Overview

The purpose of this document is to outline the functional and non-functional requirements for the development of the Unit Conversion Tool. This tool will allow users to convert units between Metric and Imperial systems, provide location-based suggestions for measurement systems, and offer accessibility options like dark mode and font size adjustments. It will include both web and mobile versions, ensuring compatibility across different devices and offering users an intuitive interface for their conversion needs.

## Functional Requirements

1. **Conversion Functionality**
   1. The system shall allow users to convert between Metric and Imperial systems.
   2. The system shall support conversions for distance, volume, weight, and temperature.
   3. The system shall provide a toggle switch to switch between Metric and Imperial conversions.
   4. The system shall display the converted value below the input value.

2. **Location-Based Suggestions**
   1. The system shall detect the user’s location using the IP address.
   2. The system shall suggest the appropriate measurement system (Metric or Imperial) based on the detected location.
   3. The system shall allow users to override the suggested system by manually selecting a different country.

3. **Accessibility Features**
   1. The system shall offer a dark mode and bright mode, depending on the user’s preference or system time.
   2. The system shall allow users to adjust the font size for better readability.
   3. The system shall provide accessibility settings in the Settings menu.

4. **Conversion Categories**
   1. The system shall allow users to select a category of measurement such as distance, volume, weight, temperature, or length.
   2. The system shall provide conversion options specific to the selected category (e.g., kilometers to miles for distance).

5. **User Interface**
   1. The system shall provide a drop-down menu for country selection.
   2. The system shall provide a drop-down menu for selecting the type of measurement to convert (e.g., liquid, weight, height).
   3. The system shall display a menu icon on the top left corner of the page to navigate to different sections (Home, Articles, About Us, Settings).

6. **Error Handling**
   1. The system shall display an error message if the input value is invalid (e.g., negative numbers in certain conversions).
   2. The system shall not proceed with conversions if required fields are not filled.

7. **Articles Section**
   1. The system shall provide users with informative articles about different measurement systems.
   2. The system shall display the history, usage, and conversion formulas for various measurement systems.

8. **Settings**
   1. The system shall allow users to adjust display settings like dark mode and font size in the Settings menu.
   2. The system shall allow users to change language preferences if needed.

## Non-Functional Requirements

1. **Performance**
   1. The system shall respond to user inputs and display the converted value within 2 seconds.
   2. The system shall handle at least 100 concurrent users without performance degradation.

2. **Reliability**
   1. The system shall be available 99.9% of the time during operational hours.
   2. The system shall ensure data accuracy for conversions, with no more than a 0.1% margin of error in results.

3. **Security**
   1. The system shall not store any personal user data.
   2. The system shall use secure communication (HTTPS) for data transfer.
   3. The system shall comply with IP-based privacy regulations and ensure that location data is not stored.

4. **Usability**
   1. The system shall be user-friendly and intuitive, requiring minimal learning to use.
   2. The system shall be compatible with major browsers like Chrome, Firefox, Safari, and Edge.
   3. The system shall support both mobile and desktop users.

5. **Compatibility**
   1. The system shall work on mobile platforms (iOS, Android) and desktop platforms (Windows, macOS, Linux).
   2. The system shall work on screen readers to provide accessibility for users with visual impairments.

6. **Maintainability**
   1. The system shall have a modular code structure that allows easy updates or fixes.
   2. The system shall be documented in such a way that new developers can understand the code within 1 week of reading the documentation.

7. **Scalability**
   1. The system shall be scalable to handle increased traffic or new features without requiring major architectural changes.
   2. The system shall allow for the addition of new conversion types without rewriting the core code.

8. **Localization**
   1. The system shall support multiple languages for users in different countries.
   2. The system shall allow for easy translation of text into supported languages.

9. **Extensibility**
   1. The system shall be designed in such a way that new conversion types can be added easily by developers.
   2. The system shall support adding future measurement units without major changes to the core structure.

10. **Data Integrity**
    1. The system shall ensure that all data entered by users is stored and processed correctly.
    2. The system shall prevent data corruption during conversion processes.

11. **Response Time**
    1. The system shall ensure that conversion operations complete within 1 second under normal load.
    2. The system shall provide users with an immediate response if the system is down.

12. **Supportability**
    1. The system shall include clear documentation for users to understand how to use the app effectively.
    2. The system shall provide troubleshooting steps in case of technical issues.

13. **Error Recovery**
    1. The system shall recover from unexpected errors without loss of user data.
    2. The system shall provide users with error messages and suggest ways to fix issues encountered during conversions.

14. **Aesthetic Design**
    1. The system shall have a clean, modern design that adapts to both light and dark modes seamlessly.
    2. The system shall use high-contrast colors to ensure readability in both bright and dark settings.

15. **Data Privacy**
    1. The system shall ensure that no user location data is stored longer than the session duration.
    2. The system shall not request any unnecessary permissions from users, focusing only on functionality.

_This document is a living document.
