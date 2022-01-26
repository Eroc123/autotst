from selenium.webdriver import Firefox, Edge
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options as edoptions
from selenium.webdriver.common.by import By
from base64 import b64decode
from cryptography.fernet import Fernet
import time
import os

def getfilename():
    files = os.listdir('.')
    for i in range(1,1000):
        if f'TST{i}.png' in files:
            pass
        else:
           name = f'TST{i}.png'
           break
    return name
filename = getfilename()


with open('KEY', 'rb') as file:
    key = file.read()
fernet = Fernet(key)

with open('EMAIL', 'rb') as enc_file:
    email = enc_file.read()
with open('PASSWORD', 'rb') as enc_file:
    password = enc_file.read()
  
# decrypting the file
email = fernet.decrypt(email).decode()
password = fernet.decrypt(password).decode()

try:
    options = Options()
    options.headless = True
    driver = Firefox(executable_path =r".\driver\geckodriver.exe", options = options)
except:
    options = edoptions()
    options.headless = False
    driver = Edge(executable_path =r".\driver\msedgedriver.exe", options = options)
   
driver.get('https://savethai.anamai.moph.go.th/login.php') #Go to login page
usernamefd = driver.find_element(By.ID, 'C_USERNAME') #Find username field
passwordfd = driver.find_element(By.ID, 'C_PASSWORD') #Find password field
usernamefd.send_keys(email) #enter email
passwordfd.send_keys(password) #enter password
driver.find_element(By.CLASS_NAME, 'btn-lg').click() #click login

driver.get('https://savethai.anamai.moph.go.th/lang_en.php') #go to english translation
driver.get('https://savethai.anamai.moph.go.th/form_check.php') #create new form
driver.find_element(By.ID, 'C_SICK_2').click() #1st choice second radio
driver.find_element(By.ID, 'C_NOT_SMELL_2').click() #2nd choice second radio
driver.find_element(By.ID, 'C_NOT_TALK_2').click() #3rd choice second radio
driver.find_element(By.ID, 'C_NOT_TALK_2').click() #4th choice second radio
driver.find_element_by_xpath("//input[@name='C_TRAVEL' and @value='1']").click() #5h choice second radio
driver.find_element(By.CLASS_NAME, 'btn-lg').click() #submit


#DMHTA submit, because of vaccine
driver.get('https://savethai.anamai.moph.go.th/dmhta.php')
driver.find_element(By.CLASS_NAME, 'btn-lg').click() #Submit form
driver.get('https://savethai.anamai.moph.go.th/lang_en.php')

driver.set_window_size(1920, 1080)
driver.get('https://savethai.anamai.moph.go.th/home_user.php')
time.sleep(0.7)

driver.save_screenshot(filename)
driver.quit()
os.unlink('geckodriver.log')
