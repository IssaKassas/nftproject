import csv
from os import getcwd
from os.path import join
from pathlib import Path
from decouple import config , Csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
from sys import path
path.append("C:/Users/admin/Desktop/nftproject/Json")
from jsonClass import JSON
from nftClass import NFT

# https://dashboard.heroku.com/apps/fast-forest-46836/settings
# you should create .env file and type the variables in it and in the heroku app

path = Path(getcwd())

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast = Csv())
DEBUG = config('DEBUG', default = True, cast = bool)
# we should install Chrome extension source viewer
EXTENSION_PATH = config("EXTENSION_PATH")
RECOVERY_CODE = config("RECOVERY_CODE")
PASSWORD = config("PASSWORD")
CHROME_DRIVER_PATH = config("CHROME_DRIVER_PATH")

#If google chrome not installed
#from webdriver_manager.chrome import ChromeDriverManager
#CHROME_DRIVER_PATH = ChromeDriverManager().install()

def setup_metamask_wallet(driver : webdriver.Chrome):
    driver.switch_to.window(driver.window_handles[0])
    sleep(5)
    #https://www.lambdatest.com/blog/complete-guide-for-using-xpath-in-selenium-with-examples/
    #https://www.topcoder.com/thrive/articles/python-for-web-automation-selenium-basics#:~:text=Selenium%20is%20an%20open%2Dsource,different%20tasks%20on%20the%20browser.
    #https://stackoverflow.com/questions/62320910/how-to-change-the-input-field-value-using-selenium-and-python
    #https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
    global wait
    wait = WebDriverWait(driver , timeout = 1)
    wait.until(EC.element_to_be_clickable((By.XPATH , 'button[text()="Get Started"]')))
    sleep(1)
    
    wait.until(EC.element_to_be_clickable((By.XPATH , 'button[text()="Import wallet"]')))
    sleep(1)
    
    wait.until(EC.element_to_be_clickable((By.XPATH , 'button[text()="No Thanks"]')))
    sleep(1)
    
    wait.until(EC.element_to_be_clickable((By.XPATH , "button[text() = 'Import']")))
    # inputs = wait.until(EC.element_to_be_clickable((By.TAG_NAME , "input")))
    # inputs.send_keys(RECOVERY_CODE)
    # sleep(1)
    
    # inputs[1].send_keys(PASSWORD)
    # inputs[2].send_keys(PASSWORD)
    sleep(1)
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR , ".first-time-flow__terms")))
    wait.until(EC.element_to_be_clickable((By.XPATH , "button[text() = 'Import']")))

def moveToOpenSea(driver : webdriver.Chrome):
    driver.execute_script(
        '''window.open("https://opensea.io/collection/guy-with-a-smirk/assets/create","_blank")'''
    )
    driver.switch_to.window(driver.window_handles[0])
    sleep(5)
    
def signin_to_opensea(driver : webdriver.Chrome):
    wait = WebDriverWait(driver , timeout = 1)
    wait.until(EC.element_to_be_clickable((By.XPATH , 'span[text()="MetaMask"]')))
    sleep(4)
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.element_to_be_clickable((By.XPATH , "button[text()='Next']")))
    sleep(4)
    wait.until(EC.element_to_be_clickable((By.XPATH , '//button[text()="Connect"]')))
    
def checkForAlreadyUploaded(filename):
    with open(join(f"{path}\OutputData","uploaded.csv") , "r") as file:
        reader = csv.reader(file , skipinitialspace = False , delimiter = ',' , quoting = csv.QUOTE_NONE)
        for row in reader:
            for field in row:
                if field == filename:
                    print("is in file")
                    return False
        file.close()
        return True

def fillMetaData(driver: webdriver.Chrome , metadata : dict):
    driver.find_element_by_xpath('//div[@class="AssetFormTraitSection--side"]/button').click()
    for item in metadata:
        for key in item:
            input1 = wait.until(EC.element_to_be_clickable((By.XPATH ,
                'tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[1]/div/div/input'
                )))
            input2 = wait.until(EC.element_to_be_clickable((By.XPATH ,
                'tbody[@class="AssetTraitsForm--body"]/tr[last()]/td[2]/div/div/input'
                )))
            input1.send_keys(str(key))
            input2.send_keys(str(item[key]))
            wait.until(EC.element_to_be_clickable((By.XPATH ,"button[text()='Add more']")))
    
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH ,"button[text()='Save']")))

def uploadNFT(driver : webdriver.Chrome , nft: NFT):
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.element_to_be_clickable((By.ID , "media"))).send_keys(nft.file)
    wait.until(EC.element_to_be_clickable((By.ID , "name"))).send_keys(nft.name)
    wait.until(EC.element_to_be_clickable((By.ID , "description"))).send_keys(nft.description)
    fillMetaData(driver , nft.metadata)
    wait.until(EC.element_to_be_clickable((By.XPATH ,'button[text()="Create"]')))
    driver.execute_script('location.href="https://opensea.io/collection/ether-swimmers/assets/create"')

def addFileToComplete(filename):
    with open(join(f"{path}\OutputData","uploaded.csv") , "r") as file:
        writer = csv.writer(file , delimiter = ',' , quoting = csv.QUOTE_NONE)
        writer.writerow([filename])
        file.flush()
        file.close()
    
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(service = Service(CHROME_DRIVER_PATH) , options = options)
driver.maximize_window()
driver.get("https://www.google.com")
sleep(2)

setup_metamask_wallet(driver)
sleep(2)

moveToOpenSea(driver)
signin_to_opensea(driver)

driver.execute_script('window.open("htttps://opensea.io/collection/ether-swimmers/assets/create" , "_blank")')
driver.switch_to.window(driver.window_handles[-1])
sleep(3)

file = JSON(r"C:\Users\admin\Desktop\nftproject\OutputData\metadata.json").reader()
for data in file:
    for key in data:
        if checkForAlreadyUploaded(data[key]['file']):
            name = data[key]['name']
            description = data[key]['description']
            filename = data[key]['file']
            metadata = data[key]['attributes']
            uploadNFT(driver , NFT(name , description , metadata , f"{path}\Output\Data\{filename}"))
            addFileToComplete(filename)
            
print("Done!!!!")