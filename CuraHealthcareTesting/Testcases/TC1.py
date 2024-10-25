# Here, I am performing Functional Testing on Cura Healthcare Service Website

"""Testcase 1:
To test the login process using invalid username or password
"""


from selenium.webdriver.common.by import By
import time
import sys

# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\CuraHealthcareTesting\\utility')  

# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver

def test_login():
    driver = initialize_driver()


    try:
        # Open the website
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(2)  # Wait for the page to load
        
        # Click the "Make Appointment" button
        driver.find_element(By.ID, 'btn-make-appointment').click()
        time.sleep(2)  # Wait for the transition

        # Enter username and password
        driver.find_element(By.ID, "txt-username").send_keys('John Doey')
        driver.find_element(By.ID, "txt-password").send_keys('ThisIsAPassword')
        
        # Click the login button
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(2)  # Wait for the login attempt to process

        # Verify the error message
        error_message = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text

        expected_message = "Login failed! Please ensure the username and password are valid."
        
        assert error_message == expected_message, f"Expected '{expected_message}', but got '{error_message}'"
        print("Test passed: Error message is as expected.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_login()
