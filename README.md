# Mortgage Affordability Calculator Automation

This program automates the process of filling out the mortgage affordability calculator form on the Coventry Building Society website using the provided applicant data. The results for each applicant are printed to the terminal and saved in a new file called `result.json`.

## Prerequisites

- **Python**: Make sure you have Python installed on your machine.
- **Selenium**: Install the Selenium package using pip.
- **ChromeDriver**: Download the ChromeDriver compatible with your Chrome browser version from [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/).

## Setup

1. **Install Required Libraries**:
    ```bash
    pip install selenium
    ```

2. **Download ChromeDriver**:
    - Download the ChromeDriver from the link provided above.
    - Note the path to the downloaded ChromeDriver executable.

3. **Update `main.py`**:
    - Open `main.py`.
    - Update the `chrome_driver_path` variable (line 12) with the path to your downloaded ChromeDriver executable.

## Files

- **`main.py`**: The main execution script that runs the automation.
- **`helper_functions.py`**: Contains helper functions used by `main.py` to interact with the web page.
- **`applicants_data.json`**: JSON file containing the data for each applicant.

## Running the Program

1. **Prepare the Applicant Data**:
- The `applicants_data.json` file is pre-populated with six applicant data entries that cover various scenarios. These scenarios are designed to test different aspects of the application process.
- You can add new applicant data if needed, but ensure that all necessary information is included.

2. **Execute the Script**:
    - Run the `main.py` script:
    ```bash
    python3 main.py
    ```

3. **View Results**:
    - The results for each applicant will be printed to the terminal.
    - A new file called `results.json` will be created in the same directory, containing the results.

## Result

- The terminal will display the maximum loan amount and the maximum monthly payment for which the lender is willing to offer for each applicant.
- The `result.json` file will store these results for further reference.

## Notes

- Ensure that your Chrome browser is updated to a version compatible with the ChromeDriver.

