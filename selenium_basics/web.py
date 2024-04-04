from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://www.bing.com/search?q=companies+offering+shopify+website+design+services+in+the+UK&cvid=14ecd58f95074138a6e8c8217f6ddd31&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg70gEIMjk1MGowajmoAgCwAgA&FORM=ANAB01&PC=U531")
time.sleep(20)
file = open("webdesigners.txt", mode='w')
link = driver.find_element(By.XPATH, "(//a[@draggable='false'])[5]").get_attribute('href')
driver.get(link)
time.sleep(15)

elements = driver.find_elements(By.XPATH, "(//ul[@class='b_vList b_divsec'])[1]/li")
print(len(elements))

for element in elements:
    name = element.find_element(By.XPATH, ".//div[@class='b_vPanel']/div[1]/div").text
    category = "None"
    location = element.find_element(By.XPATH, ".//div[@class='b_vPanel']/div[3]/div/span").text
    opening_time = "None"
    open = "None"
    click = element.find_element(By.XPATH, ".//div[@class='b_vPanel']/div[1]/div").click()
    website = "None"


    try:
        category = element.find_element(By.XPATH, ".//div[@class='b_vPanel']/div[2]/div").text
    except:
        pass

    try:
        opening_time = element.find_element(By.XPATH, ".//span[@class='opHours']/span").text
    except:
        pass

    try:
        open = element.find_element(By.XPATH, ".//span[@class='opHours']/span/span").text
    except:
        pass

    try:
        website = element.find_element(By.XPATH, ".//div[@id='IconItem_3']/a").text
    except:
        pass

    print(name, category, location ,opening_time, open, website)

    file.write(f"name: {name}, \n category: {category},\n location: {location},\n opening_time: {opening_time},\n open: {open}, \n website: {website}, \n \n")


file.close()