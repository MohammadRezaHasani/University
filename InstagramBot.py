from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from InstagramBot_Credentials import pw
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot():
        links = []
        comments = ['Great post!', 'Awesome']
    
        def __init__(self):
            self.login('cybersecurity_company', pw)
            self.like_comment_by_hashtag('programming')

        def login(self, username, password):
            self.driver = webdriver.Chrome()
            self.driver.get('https://www.instagram.com')
            sleep(3)
            accept_cookies = WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow')]")))
            accept_cookies.click()
            sleep(1)
            username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            username_input.send_keys(username)
            sleep(1)
            password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            password_input.send_keys(password)
            sleep(1)
            login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
            login_btn.click()
            sleep(6)

        def like_comment_by_hashtag(self, hashtag):
            self.driver.get('https://www.instagram.com/explore/tags/{}'.format(hashtag))
            sleep(5)
            links = self.driver.find_elements(By.TAG_NAME, 'a')
            sleep(3)

            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            sleep(2)

            for i in range(5):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

                    for link in self.links:
                        self.driver.get(link)
                #like
                        sleep(4)
                        #like_btn = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button//*[name()='svg'][@aria-label='Like']")))
                        #like_btn.click()
                        #like_btn = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[.//svg[contains(@aria-label, 'Like')]]")))
                        #like_btn.click()
                        #like_btn = WebDriverWait(self.driver, 5).until(
                        #like_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//svg[@aria-label="Like"]/ancestor:div[2]')))
                        #like_btn.click()
                        #like_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//svg[@aria-label="Like"]/ancestor::div[@role="button"]')))
                        #like_btn.click()
                        #sleep(2)

                #comment
                        comment_box = self.driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
                        comment_box.click()
                        sleep(1)
                        comment_box.send_keys(self.comments[randint(0,1)])

def main():
    my_bot = Bot()
    input("Press Enter to close the browser...")




main()








# python3 -i "/Users/mohammadreza/Downloads/Master's Files/InstagramBot/InstagramBot.py"
