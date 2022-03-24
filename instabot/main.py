import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chromedriver_path = "C:\development\chromedriver.exe"
ser = Service(executable_path=chromedriver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.instagram.com")

def creds():
        with open("insta bot\cred.json","r") as data:
            df = json.load(data)
        user = df['username']
        password = df['password']
        return user, password


class InstaBot:

    def __init__(self,user,password):
        self.user = user
        self.password = password


    def connect(self):
        time.sleep(2)
        username = driver.find_element_by_name("username")
        username.send_keys(user)
        time.sleep(2)
        pw = driver.find_element_by_name("password")
        pw.send_keys(password)
        time.sleep(2)
        log_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        # AFTER LOG IN
        time.sleep(4)
        not_now_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        # # notification not now btn
        time.sleep(4)
        noti_btn = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()


    def look_up_user(self):
        # search 
        time.sleep(2)
        search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # profile of user we want
        search.send_keys("cleverqazi")
        time.sleep(2)
        first_person = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        # go to followers list
        time.sleep(3)
        followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()

user = creds()[0]
password = creds()[1]
bot = InstaBot(user,password)
bot.connect()
bot.look_up_user()