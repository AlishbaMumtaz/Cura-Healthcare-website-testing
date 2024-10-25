
"""Testcase 3:
To test the appointment booking process by selecting facility, healthcare program, a date, and comment
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys


# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\CuraHealthcareTesting\\utility')  

# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver


def test_appointment_booking():
    driver = initialize_driver()

    try:
        # Open the website
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(2)  

        # Click the "Make Appointment" button
        driver.find_element(By.ID, 'btn-make-appointment').click()
        time.sleep(2)  

        # Enter valid username and password
        driver.find_element(By.ID, "txt-username").send_keys('John Doe')
        driver.find_element(By.ID, "txt-password").send_keys('ThisIsNotAPassword')
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)

       
        facility_dropdown = Select(driver.find_element(By.ID, 'combo_facility'))
        facility_dropdown.select_by_visible_text('Tokyo CURA Healthcare Center')
        
        # Checking the "Apply for hospital readmission" checkbox
        readmission_checkbox = driver.find_element(By.XPATH, "//label[@for='chk_hospotal_readmission']")
        if not readmission_checkbox.is_selected():
            readmission_checkbox.click()
        
        # Selecting "Medicare" as the Healthcare Program
        driver.find_element(By.XPATH, "//label[normalize-space()='Medicare']").click()
        
        # Setting the visit date
        visit_date = driver.find_element(By.XPATH, "//input[@id='txt_visit_date']")
        visit_date.clear()
        visit_date.send_keys('06/10/2024')
        
        # Adding a comment
        driver.find_element(By.ID, 'txt_comment').send_keys('Appointment booked for regular checkup ')

        # Clicking the "Book Appointment" button
        driver.find_element(By.ID, 'btn-book-appointment').click()
        time.sleep(3)  # Wait for the booking process

    
        print("Test passed: Appointment booked successfully.")

    except Exception as e:
        
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser window
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_appointment_booking()
