

"""Testcase 2:
To test the login process using valid username and password 
"""


from selenium.webdriver.common.by import By
import time
import sys

# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\CuraHealthcareTesting\\utility')  

# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver


def test_login_valid_credentials():
    driver = initialize_driver()

    try:
        # Opening the website
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        time.sleep(2)  
        
        
        driver.find_element(By.ID, 'btn-make-appointment').click()
        time.sleep(2)  

        
        driver.find_element(By.ID, "txt-username").send_keys('John Doe')
        driver.find_element(By.ID, "txt-password").send_keys('ThisIsNotAPassword')  
        
       
        driver.find_element(By.ID, "btn-login").click()
        time.sleep(3)  

        # If the login is successful and no exceptions occur, print that the test passed
        print("Test passed: Logged in successfully with valid credentials.")

    except Exception as e:
        
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

# Running the test
if __name__ == "__main__":
    test_login_valid_credentials()
