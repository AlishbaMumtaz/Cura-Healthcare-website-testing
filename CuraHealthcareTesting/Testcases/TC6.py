"""Testcase 6:
To test the application's handling of a 404 error by navigating to a non-existent page.
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sys


# Adding the utility folder to the system path
sys.path.insert(0, 'C:\\Users\\HD\\CuraHealthcareTesting\\utility')  

# Importing the initialize_driver function from webdriver_setup
from webdriver_setup import initialize_driver



def test_404_error_handling():
    driver = initialize_driver()

    try:
        # Open the website
        driver.get("https://katalon-demo-cura.herokuapp.com/nonexistentpage")
        time.sleep(2)

        # Check if an error message is displayed
        error_message = driver.find_element(By.TAG_NAME, "body").text  # You may want to be more specific
        assert "404" in error_message or "not found" in error_message.lower(), "Error message not displayed as expected."

        print("Test passed: 404 error handled correctly with a user-friendly message.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser window
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_404_error_handling()
