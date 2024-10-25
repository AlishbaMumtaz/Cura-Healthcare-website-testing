"""Testcase 4:
To test the appointment booking process by selecting facility, healthcare program, comment and leaving the date field empty
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\CuraHealthcareTesting\\utility')  

# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver

def test_appointment_without_date():
    driver = initialize_driver()

    try:
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(2)
        driver.find_element(By.ID, 'btn-make-appointment').click()
        time.sleep(2)
        driver.find_element(By.ID, "txt-username").send_keys('John Doe')
        driver.find_element(By.ID, "txt-password").send_keys('ThisIsNotAPassword')
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)

        # Selecting facility and healthcare program
        Select(driver.find_element(By.ID, 'combo_facility')).select_by_visible_text('Tokyo CURA Healthcare Center')
        driver.find_element(By.XPATH, "//label[normalize-space()='Medicare']").click()
        
        # Leaving visit date empty and filling the comment
        comment_field = driver.find_element(By.ID, 'txt_comment')
        comment_field.send_keys('Leaving date empty')

        # Attempt to book appointment
        book_button = driver.find_element(By.ID, 'btn-book-appointment')
        book_button.click()

        # Checkingf for validation message using JavaScript
        date_field = driver.find_element(By.ID, 'txt_visit_date')
        validation_message = driver.execute_script("return arguments[0].validationMessage;", date_field)
        
        # Printing the validation message
        if validation_message:
            print(f"Test passed: Validation message displayed - {validation_message}")
        else:
            print("Test failed: No validation message displayed.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_appointment_without_date()


'''
Issues faced in running this testcase:
Faced issues in locating the error message when the date feild is left empty but tackled it after multiple attempts and by using JS validation message function
'''
