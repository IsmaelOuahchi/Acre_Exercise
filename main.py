from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from helper_functions import run_morgage_detail_scenario, employment_income_detail_scenario, expenditure_detail_scenario


if __name__ == "__main__":

    # TODO Enter your ChromeDriver path location
    chrome_driver_path = input("Please enter the path to your ChromeDriver: ")


    with open('applicants_data.json', 'r') as file:
        data = json.load(file)


    results = {}


    # Iterate over each application
    for application in data:
        try:

            # Initialize the ChromeDriver service
            service = Service(chrome_driver_path)

            # Initialize the WebDriver with the service
            driver = webdriver.Chrome(service=service)

            driver.get("https://www.coventrybuildingsociety.co.uk/calculators/AffordabilityCalculator.aspx?ch=broker")



            # Extract mortgage details for the current application
            mortgage_details = application['mortgage_details']

            # Run the scenarios with the extracted data
            run_morgage_detail_scenario(driver, mortgage_details)
            employment_income_detail_scenario(driver, mortgage_details)
            expenditure_detail_scenario(driver, mortgage_details['expenditure_details'])


            max_loan_element = driver.find_element(By.ID, 'MainContent_AffordabilityCalculator1_MaxLoanAmtLbl')
            max_monthly_pay_element = driver.find_element(By.ID, 'MainContent_AffordabilityCalculator1_MaxMonthlyPayLbl')
            print("Maximum loan amount for application ID", application['application_id'], ": ", max_loan_element.text)
            print("Maximum monthly payment for application ID", application['application_id'], ": ", max_monthly_pay_element.text)



            max_loan_amount = float(max_loan_element.text.replace('\u00a3', '').replace(',', '').strip())
            max_monthly_payment = float(max_monthly_pay_element.text.replace('\u00a3', '').replace(',', '').strip())

            # Store the results in the dictionary
            results[application['application_id']] = {
                "Maximum loan amount in £": max_loan_amount,
                "Maximum monthly payment in £": max_monthly_payment
            }


        except Exception as e:
            print(f"An error occurred for application ID {application['application_id']}: {e}")

        finally:
            driver.quit()
        
        with open('results.json', 'w') as result_file:
            json.dump(results, result_file, indent=4)

    
