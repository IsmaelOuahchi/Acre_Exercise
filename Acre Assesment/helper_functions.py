from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


def select_dropdown(driver, element_id, option, timeout=10):
        select_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.ID, element_id))
        )

        select = Select(select_element)
        
        select.select_by_visible_text(option)



def enter_text(driver, element_id, text, timeout=10):
        
        text_box = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.ID, element_id))
        )
    
        text_box.clear()
        
        # Enter the provided text into the text box
        text_box.send_keys(text)



def run_morgage_detail_scenario(driver, data):
    # Enter Mortgage details
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_421", data['property_price'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_422", data['postcode'])
    select_dropdown(driver, "MainContent_AffordabilityCalculator1_DDL_423", data['no_applicants'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_424", data['no_adults_resident'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_425", data['no_financial_dependants'])
    select_dropdown(driver, "MainContent_AffordabilityCalculator1_DDL_426", data['council_tax_reduction'])

    # Enter Loan details 
    select_dropdown(driver, "MainContent_AffordabilityCalculator1_DDL_430", data['type_of_loan'])
    select_dropdown(driver, "MainContent_AffordabilityCalculator1_ProductsDDL", data['product'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_431", data['total_morgage_amount'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_432", data['term_years'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_TB_433", data['term_months'])

    # Enter Applicant details
    applicant_one = data['applicant1']
    enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets1_TB_428_DAY", applicant_one['day_of_birth'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets1_TB_428_MONTH", applicant_one['month_of_birth'])
    enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets1_TB_428_YEAR", applicant_one['year_of_birth'])
    select_dropdown(driver, "MainContent_AffordabilityCalculator1_AppDets1_DDL_429", applicant_one['gender'])

    if "applicant2" in data:
        applicant_two = data['applicant2']
        enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets2_TB_428_DAY", applicant_two['day_of_birth'])
        enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets2_TB_428_MONTH", applicant_two['month_of_birth'])
        enter_text(driver, "MainContent_AffordabilityCalculator1_AppDets2_TB_428_YEAR", applicant_two['year_of_birth'])
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_AppDets2_DDL_429", applicant_two['gender'])

    # Press Continue
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ContBtn"))  
    )
    continue_button.click()

     


def employment_income_detail_scenario(driver, data):
    #  Applicant 1
    job1 = data['job_applicant1']

    if job1['employment_type'] in ["Retired", "Unemployed", "House manager"]:
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc1_DDL_434", job1['employment_type'])


    elif job1['employment_type'] in ["Employed", "LLP - PAYE registered", "LLP - Not PAYE registered", "Contract", "Contract / Daily Rate Contractor", ]:
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc1_DDL_434", job1['employment_type'])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_436", job1["annual_income"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_439", job1["annual_bonus"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_440", job1["Total_overtime_shift_commission"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_445", job1["planned_retirement"])
        if "anticipated_annual_retirement_income" in job1:
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_446", job1["anticipated_annual_retirement_income"])

    elif job1['employment_type'] == "Sole trader/Partnership/Sub-Contracting":
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc1_DDL_434", "Sole trader/Partnership/Sub-Contracting")
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_443", job1["annual_net_profit"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_445", job1["planned_retirement"])
        if "anticipated_annual_retirement_income" in job1:
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_446", job1["anticipated_annual_retirement_income"])

    elif job1['employment_type'] == "Director >= 20% Shareholder":
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc1_DDL_434", "Director >= 20% Shareholder")
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_444", job1["annual_net_profit_plus_salary"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_445", job1["planned_retirement"])
        if "anticipated_annual_retirement_income" in job1:
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_446", job1["anticipated_annual_retirement_income"])

    elif job1['employment_type'] == "Director < 20% Shareholder":
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc1_DDL_434", "Director < 20% Shareholder")
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_436", job1["annual_income"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_439", job1["annual_bonus"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_440", job1["Total_overtime_shift_commission"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_441", job1["dividend_last_year"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_442", job1["dividend_previous_year"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_445", job1["planned_retirement"])
        if "anticipated_annual_retirement_income" in job1:
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc1_TB_446", job1["anticipated_annual_retirement_income"])

    if "other_source_income_type" in job1:
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_AddInc1_DDL_448", "Yes")
        select_dropdown(driver, "MainContent_AffordabilityCalculator1_AddInc1_DDL_449", job1["other_source_income_type"])
        enter_text(driver, "MainContent_AffordabilityCalculator1_AddInc1_TB_450", job1["other_source_income_amount"])


    

    if "job_applicant2" in data:
        job2 = data['job_applicant2']
        if job2['employment_type'] in ["Retired", "Unemployed", "House manager"]:
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc2_DDL_434", job2['employment_type'])

        elif job2['employment_type'] in ["Employed", "LLP - PAYE registered", "LLP - Not PAYE registered", "Contract", "Contract / Daily Rate Contractor", ]:
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc2_DDL_434", job2['employment_type'])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_436", job2["annual_income"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_439", job2["annual_bonus"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_440", job2["Total_overtime_shift_commission"])                
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_445", job2["planned_retirement"])
            if "anticipated_annual_retirement_income" in job2:
                enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_446", job2["anticipated_annual_retirement_income"])


        elif job2['employment_type'] == "Sole trader/Partnership/Sub-Contracting":
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc2_DDL_434", "Sole trader/Partnership/Sub-Contracting")
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_443", job2["annual_net_profit"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_445", job2["planned_retirement"])
            if "anticipated_annual_retirement_income" in job2:
                enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_446", job2["anticipated_annual_retirement_income"])

        elif job2['employment_type'] == "Director >= 20% Shareholder":
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc2_DDL_434", "Director >= 20% Shareholder")
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_444", job2["annual_net_profit_plus_salary"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_445", job2["planned_retirement"])
            if "anticipated_annual_retirement_income" in job2:
                enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_446", job2["anticipated_annual_retirement_income"])

        elif job2['employment_type'] == "Director < 20% Shareholder":
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_EmpInc2_DDL_434", "Director < 20% Shareholder")
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_436", job2["annual_income"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_439", job2["annual_bonus"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_440", job2["Total_overtime_shift_commission"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_441", job2["dividend_last_year"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_442", job2["dividend_previous_year"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_445", job2["planned_retirement"])
            if "anticipated_annual_retirement_income" in job2:
                enter_text(driver, "MainContent_AffordabilityCalculator1_EmpInc2_TB_446", job2["anticipated_annual_retirement_income"])

        
        if "other_source_income_type" in job2:
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_AddInc2_DDL_448", "Yes")
            select_dropdown(driver, "MainContent_AffordabilityCalculator1_AddInc2_DDL_449", job2["other_source_income_type"])
            enter_text(driver, "MainContent_AffordabilityCalculator1_AddInc2_TB_450", job2["other_source_income_amount"])

    time.sleep(3)
    # Press Continue
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ContBtn"))  
    )
    continue_button.click()


def expenditure_detail_scenario(driver, data):
    # School fees
    applicant1_details = data['applicant1_expenditure']
    if "school_fees" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_495_1", applicant1_details["school_fees"])
    if "nursery_childminding_fees" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_496_1", applicant1_details["nursery_childminding_fees"])
    if "life_insurance" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_497_1", applicant1_details["life_insurance"])
    if "building/contents_insurance" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_498_1", applicant1_details["building/contents_insurance"])
    if "ground_rent/service_charge" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_499_1", applicant1_details["ground_rent/service_charge"])
    if "unsecured_loan" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_500_1", applicant1_details["unsecured_loan"])
    if "personal_hp_agreement" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_501_1", applicant1_details["personal_hp_agreement"])
    if "credit_agreements" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_502_1", applicant1_details["credit_agreements"])
    if "secured_loans" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_503_1", applicant1_details["secured_loans"])
    if "other_mortgage_payments" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_504_1", applicant1_details["other_mortgage_payments"])
    if "continuing_child_maintenance" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_505_1", applicant1_details["continuing_child_maintenance"])
    if "student_loans" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_506_1", applicant1_details["student_loans"])
    if "monthly_pension_contributions" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_455_1", applicant1_details["monthly_pension_contributions"])
    if "total_credit_card_balances" in applicant1_details:
        enter_text(driver, "MainContent_AffordabilityCalculator1_TB_453_1", applicant1_details["total_credit_card_balances"])

    if "applicant2_expenditure" in data:
        applicant2_details = data['applicant2_expenditure']
        if "school_fees" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_495_2", applicant2_details["school_fees"])
        if "nursery_childminding_fees" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_496_2", applicant2_details["nursery_childminding_fees"])
        if "life_insurance" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_497_2", applicant2_details["life_insurance"])
        if "building/contents_insurance" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_498_2", applicant2_details["building/contents_insurance"])
        if "ground_rent/service_charge" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_499_2", applicant2_details["ground_rent/service_charge"])
        if "unsecured_loan" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_500_2", applicant2_details["unsecured_loan"])
        if "personal_hp_agreement" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_501_2", applicant2_details["personal_hp_agreement"])
        if "credit_agreements" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_502_2", applicant2_details["credit_agreements"])
        if "secured_loans" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_503_2", applicant2_details["secured_loans"])
        if "other_mortgage_payments" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_504_2", applicant2_details["other_mortgage_payments"])
        if "continuing_child_maintenance" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_505_2", applicant2_details["continuing_child_maintenance"])
        if "student_loans" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_506_2", applicant2_details["student_loans"])
        if "monthly_pension_contributions" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_455_2", applicant2_details["monthly_pension_contributions"])
        if "total_credit_card_balances" in applicant2_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_453_2", applicant2_details["total_credit_card_balances"])


    if "joint" in data:
        joint_details = data['joint']
        if "school_fees" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_495_J", joint_details["school_fees"])
        if "nursery_childminding_fees" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_496_J", joint_details["nursery_childminding_fees"])
        if "life_insurance" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_497_J", joint_details["life_insurance"])
        if "building/contents_insurance" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_498_J", joint_details["building/contents_insurance"])
        if "ground_rent/service_charge" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_499_J", joint_details["ground_rent/service_charge"])
        if "unsecured_loan" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_500_J", joint_details["unsecured_loan"])
        if "personal_hp_agreement" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_501_J", joint_details["personal_hp_agreement"])
        if "credit_agreements" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_502_J", joint_details["credit_agreements"])
        if "secured_loans" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_503_J", joint_details["secured_loans"])
        if "other_mortgage_payments" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_504_J", joint_details["other_mortgage_payments"])
        if "continuing_child_maintenance" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_505_J", joint_details["continuing_child_maintenance"])
        if "student_loans" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_506_J", joint_details["student_loans"])
        if "monthly_pension_contributions" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_455_J", joint_details["monthly_pension_contributions"])
        if "total_credit_card_balances" in joint_details:
            enter_text(driver, "MainContent_AffordabilityCalculator1_TB_453_J", joint_details["total_credit_card_balances"])

    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ContBtn"))  
    )
    continue_button.click()