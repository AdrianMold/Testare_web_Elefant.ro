# Automated Testing Project for www.elefant.ro

## Project Overview
This project focuses on automated testing of the website www.elefant.ro. It includes various scenarios covering different aspects of the website, from user login to product search and manipulation in the shopping cart.

## Features Tested
1. **User Login**
   - Valid login with email and password.
   - Handling wrong email and password inputs.
2. **Product Search and Interaction**
   - Searching for products (books, games, etc.).
   - Navigating through website categories.
   - Adding and removing products from the shopping cart.
3. **UI Elements Verification**
   - Checking the presence of specific elements (e.g., logo, promotional banners).
4. **Special Characters Search**
   - Testing the search functionality with special characters.

## Tools and Technologies
- **Selenium WebDriver**: For browser automation.
- **Behave (BDD framework)**: For writing tests in natural language style.
- **Python**: Programming language used for writing test scripts.
- **WebDriver Manager**: For managing browser driver dependencies.
- **ChromeDriver**: WebDriver for Chrome browser.

## Setup and Configuration

### Environment Setup
- Ensure Python is installed.
- Install necessary Python packages: Selenium, Behave, WebDriver Manager.

### Running Tests
- Tests can be executed using the Behave command: `behave -f html -o behave-report.html`
- This generates an HTML report for the test execution.

### Browser Configuration
- Tests are configured to run on the Chrome browser.
- Browser options (like headless mode) can be adjusted in the `browser.py` file.

## Test Scenarios
The project includes multiple scenarios, each covering different functionalities of the website. Scenarios are defined in Gherkin syntax and are located in the `features` directory.

## Page Object Model
This project follows the Page Object Model (POM) design pattern, including:
- **BasePage class**: Contains common methods used across different pages.
- **LoginPage and SearchPage classes**: Contain methods specific to login and search functionalities.

## Behave Configuration
The `behave.ini` file contains configuration for the Behave framework, including the formatter for generating HTML reports.

## Code Organization
- `pages` directory: Contains page classes (LoginPage, SearchPage, etc.).
- `features` directory: Contains `.feature` files with test scenarios.
- `steps` directory: Contains step implementations for the scenarios.
- `browser.py` file: Contains the Browser class for managing the WebDriver instance.

## Reporting
Test execution results are generated in an HTML format for easy visualization and analysis.

## Project Structure

project_root/
│
├── features/ # Gherkin feature files
│ └── elefant.feature # Feature file for elefant.ro tests
├── pages/ # Page classes for Page Object Model (POM)
│ ├── base_page.py # Base page class with common functionalities
│ ├── login_page.py # Page class for the login page functionalities
│ └── search_page.py # Page class for the search functionalities
├── steps/ # Step definition implementations for BDD
│ ├── login_steps.py # Step definitions for login-related scenarios
│ └── search_steps.py # Step definitions for search-related scenarios
├── browser.py # Browser setup and management utilities
├── behave.ini # Configuration file for Behave framework
└── README.md # Detailed documentation of the project

## In this Structure

- `features/`
  - Contains `.feature` files describing the test scenarios in a readable format using Gherkin syntax.

- `pages/`
  - Implements the Page Object Model, encapsulating web page interactions into page classes to simplify test scripts.

- `steps/`
  - Holds the step implementation files, with each file corresponding to a particular feature:
    - `login_steps.py`: Includes the implementation of steps specific to login functionality.
    - `search_steps.py`: Contains the step implementations for search functionality, aligning with the scenarios in the feature files.

- `browser.py`
  - Provides functionalities to set up and manage the web browser for tests.

- `behave.ini`
  - The configuration file for setting up and customizing the Behave BDD framework.

- `README.md`
  - Serves as a comprehensive guide, detailing project setup, execution of tests, and other relevant information.

## Conclusion
This project aims to provide comprehensive automated testing for www.elefant.ro, ensuring the reliability and performance of the website's key functionalities.
