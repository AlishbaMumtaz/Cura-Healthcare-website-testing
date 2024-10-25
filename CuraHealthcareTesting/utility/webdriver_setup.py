
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def initialize_driver():
    # Create a Service object for ChromeDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=service)
    
    return driver

