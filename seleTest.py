
from gettext import install
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains        
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
import time

driver.get("https://testautomationpractice.blogspot.com/")
# driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()
time.sleep(3)
#Pagination Table1
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[1]/td[4]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[2]/td[4]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[3]/td[4]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[4]/td[4]/input").click()
time.sleep(3)
#Table2
driver.find_element(By.XPATH,"//*[@id='pagination']/li[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[1]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[2]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[3]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[4]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[5]/td[4]/input").click()
#Table3
driver.find_element(By.XPATH,"//*[@id='pagination']/li[3]/a").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[1]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[3]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[5]/td[4]/input").click()
#Table4
driver.find_element(By.XPATH,"//*[@id='pagination']/li[4]/a").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[1]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[3]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[2]/td[4]/input").click()
driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[5]/td[4]/input").click()
time.sleep(4)








# #Frames
# driver.switch_to.frame("frame-one796456169")
# #Name
# driver.find_element(By.ID,"RESULT_TextField-0").send_keys("rajeev")
# time.sleep(4)
# #Gender
# driver.find_element(By.XPATH,"//*[@id='q2']/table/tbody/tr[1]/td/label").click()
# time.sleep(4)
# #DOB
# driver.find_element(By.XPATH,"//*[@id='q4']/span").click()
# driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[6]/a").click()
# time.sleep(6)
# #Job
# drop_down  = Select(driver.find_element(By.ID,"RESULT_RadioButton-3"))
# drop_down.select_by_visible_text("Automation Engineer")
# time.sleep(5)
# #Submit 
# driver.find_element(By.ID,"FSsubmit").submit()
# time.sleep(3)
