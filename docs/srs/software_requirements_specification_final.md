# Overview

The purpose of this document is to outline the functional and non-functional requirements for the development of the Unit Conversion Tool. This tool will allow users to convert units between Metric and Imperial systems, provide location-based suggestions for measurement systems, and offer accessibility options like dark mode and font size adjustments. It will include both web and mobile versions, ensuring compatibility across different devices and offering users an intuitive interface for their conversion needs.

# Software Requirements

<Describe the structure of this section>

## Functional Requirements

### <Unit Conversion Features>

| ID | Requirement |
| :-------------: | :----------: |
| FR1 | Allow users to select conversion categories (e.g., Length, Mass). |
| FR2 | Support conversion between units within selected categories |
| FR3 | Display converted value instantly (Currently Operating in Postman and cURL). |
| FR4 | Ensure accurate conversions using the Pint library. |
| FR5 | Provide dropdowns for "From" and "To" units dynamically based on selection. |

### <Accessibility Feature>

| ID | Requirement |
| :-------------: | :----------: |
| FR6 | Include dark mode toggle for better visual accessibility. |
| FR7 | Provide font size adjustment buttons. |
| FR8 | Persist user settings for theme and font size across pages. |
| FR9 | Ensure front-end compatability across browsers. |
| FR10 | Maintain accessible navigation for screen readers. |

### <Front-End Visual Aspects>

| ID | Requirement |
| :-------------: | :----------: |
| FR11 | Provide a consistent navigation bar across all pages. |
| FR12 | Ensure dropdown menus dynamically update on selection. |
| FR13 | Maintain a visually appealing layout for (Home, Articles, AboutUs, and Settings. |
| FR14 | Include responsive design to ensure usability on mobile and desktop. |
| FR15 | Link all pages (Home, Articles, About, Settings) for seamless navigation. |

## Non-Functional Requirements

### <Performance>

| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | Ensure conversions execute within 1 second. |
| NFR2 | API calls should not block the UI for more than 2 seconds. |
| NFR3 | Handle up to 1000 simultaneous users without performance degradation. |
| NFR4 | Provide clear error messages for invalid inputs or failed conversions. |
| NFR5 | Ensure smooth navigatio and interaction between all linked pages, such as articles and settings, without noticeable delay or page reload issues. |

### <Usability & Scalability>

| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | Maintain a clean, responsive UI across devices. |
| NFR7 | Ensure all interactive elements are accessible via keyboard. |
| NFR8 | Allow integration of additional unit categories easily. |
| NFR9 | Ensure code modularity for future feature additions. |
| NFR10 | Implement rate limiting to protect the API from misuse. |

### <Security>

| ID | Requirement |
| :-------------: | :----------: |
| NFR11 | Secure local storage of user preferences for theme and font size. |
| NFR12 | Prevent unauthorized access to API endpoints. |
| NFR13 | Use HTTPS for all communications to ensure secure data transfer. |
| NFR14 | Validate all user inputs to prevent injection attacks. |
| NFR15 | Implement rate limiting to protect the API from misuse. |

# Software Artifacts

<Describe the purpose of this section>

* [Use Case Diagram](../artifacts/use_case_diagram/use_case_diagram.png)
* [Class / Object Diagram (NEED TO CREATE)](to_some_file.pdf)
* [Sequence / Communication Diagram (NEED TO CREATE)](to_some_file.pdf)
