#Automation Test Selenium Python

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
driver.maximize_window()

#Name
driver.find_element(By.ID,"name").send_keys("RAJEEV KUMAR DAS")
time.sleep(2)

#Tabs
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("laptop")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(3)

#Email ID
driver.find_element(By.ID,"email").send_keys("rajeevdas@gmail.com") 

#Phone Number
driver.find_element(By.ID,"phone").send_keys("9966228899")
time.sleep(3)

#Address
driver.find_element(By.ID,"textarea").send_keys("Chandaka, Bhubaneswar, Odisha")
time.sleep(2)

#Alert Click
driver.find_element(By.XPATH,"//button[@onclick='myFunctionAlert()']").click()
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(3)
driver.find_element(By.ID,"male").click()
#Double Click
button = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
act = ActionChains(driver)
act.double_click(button).perform()
time.sleep(4)

#Days
driver.find_element(By.ID,"wednesday").click()
time.sleep(3)
driver.find_element(By.ID,"thursday").click()
time.sleep(3)
driver.find_element(By.ID,"monday").click()
time.sleep(3)
driver.find_element(By.ID,"sunday").click()
time.sleep(4)

#Drag&Drop
source_element = driver.find_element(By.ID,"draggable")
target_element = driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.drag_and_drop(source_element ,target_element ).perform()
time.sleep(4)

#Drop&Down
drop_down  = Select(driver.find_element(By.ID,"country"))
#element = Select(drop_down)
drop_down.select_by_visible_text("India")
time.sleep(4)

#Color
driver.find_element(By.XPATH,"//option[@value='green']").click()
time.sleep(4)
# driver.find_element(By.ID,"datepicker").click()

#Slider
slider = driver.find_element(By.CSS_SELECTOR,"#slider > span")
time.sleep(4)
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(slider,200,0).perform()
time.sleep(3)


#Date
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a").click()
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
#Frames
driver.switch_to.frame("frame-one796456169")
#Name
driver.find_element(By.ID,"RESULT_TextField-0").send_keys("rajeev")
time.sleep(4)
#Gender
driver.find_element(By.XPATH,"//*[@id='q2']/table/tbody/tr[1]/td/label").click()
time.sleep(4)
#DOB
driver.find_element(By.XPATH,"//*[@id='q4']/span").click()
driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[6]/a").click()
time.sleep(6)
#Job
drop_down  = Select(driver.find_element(By.ID,"RESULT_RadioButton-3"))
drop_down.select_by_visible_text("Automation Engineer")
time.sleep(5)
#Submit 
driver.find_element(By.ID,"FSsubmit").submit()
time.sleep(3)
