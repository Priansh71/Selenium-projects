from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
from datetime import datetime as dt

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver
    
    
def clean_text(text):
  """ Extract only temprature form text"""
  output = float(text.split(": ")[1])
  return output


def write_file(text):
    """Write input in a text file"""
    filename = f"{dt.now()strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    """ To covert datetime "dt.now()" into string - dt.now()strftime("%Y-%m-%d.%H-%M-%S")"""
    with open(filename,'w') as file:
    # w is write mode 
        file.write(text)


def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  #return element.text
  text = str(clean_text(element.text))
  write_file(text)
  
print(main())
