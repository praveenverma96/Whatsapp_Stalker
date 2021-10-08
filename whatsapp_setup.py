from selenium import webdriver
import Constants as C

CHROME_PROFILE_PATH = C.CHROME_PROFILE_PATH

options_ = webdriver.ChromeOptions()
options_.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(executable_path= C.executable_path , options=options_)

driver.get("https://web.whatsapp.com/")