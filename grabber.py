import os, time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def driverSetup():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driverPath = os.path.abspath("chromedriverV97")
    s = Service(driverPath)
    driver = webdriver.Chrome(service=s, options=options)
    return driver

def login(driver):
    username = getpass("Enter your username: ")
    password = getpass("Enter your password: ")
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/p[2]/a").click()
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[1]/div[2]/p/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[1]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input").click()
    iframe = driver.find_element_by_xpath("/html/body/div[3]/div/iframe")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[1]/fieldset[1]/div[2]/button").click()
    code = getpass("Enter the code: ")
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[1]/fieldset[1]/div[2]/div/input").send_keys(code)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset[1]/div[2]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div[2]/a").click()
    driver.switch_to.default_content()

def grab(driver, link):
    pages = input("Pages to be captured: ")
    folder = input("Folder name: ")
    os.makedirs(folder)
    driver.get(link)
    login(driver)
    time.sleep(5)
    for i in range(1,int(pages)):
        src = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div[3]/div/div/div[1]/div[{}]/div/div/img".format(str(i))).get_attribute('src')
        driver.execute_script('''window.open("{}","_blank");'''.format(src))
        driver.switch_to.window(driver.window_handles[1])
        driver.save_screenshot(folder + "/{}.png".format(i))
        print("Captured page {}".format(i))
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/nav/div[2]/ul/li[6]/span/ul/li[2]").click()

