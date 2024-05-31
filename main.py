# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# #                                              MY CODE
#
# PROMISED_DOWN = 150
# PROMISED_UP = 10
# # CHROME_DRIVER_PATH = "/development/chromedriver-win64/chromedriver"
# TWITTER_EMAIL = "@gmail.com"
# TWITTER_PASSWORD = ""
#
# # THIS IS TO KEEP CHROME OPEN AFTER PROGRAM FINISHES
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://twitter.com/i/flow/signup")


# download_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[
# 3]/div[3]' '/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span') print(download_speed.text)

# result_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
#                                                    '/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span')


# class InternetSpeedTwitterBot:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.down = 0
#         self.up = 0
#
#     def get_internet_speed(self):
#         driver.get("https://www.speedtest.net/")
#
#         time.sleep(3)
#
# go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
# '/div[1]/a/span[4]') go_button.click()
#
#         time.sleep(60)
#
#         self.down = driver.find_element(By.XPATH,
#                                         value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
#                                               '/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span').text
#
# self.up = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
# '/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span').text
#
#     def tweet_at_provider(self):
#         pass
#
#
# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()


# driver.get("https://www.speedtest.net/")
# go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
# go_button.click()


########################################################################################################################
# class InternetSpeedTwitterBot:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.down = 0
#         self.up = 0
#
#     def get_internet_speed(self):
#         self.driver.get("https://www.speedtest.net/")
#
#         # Allow time for the page to load
#         time.sleep(10)
#
# try: # go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]' #
# '/div[1]/a/span[4]') go_button = self.driver.find_element(By.CLASS_NAME, 'js-start-test') go_button.click()
#
#             # Allow time for the speed test to complete
#             time.sleep(60)
#
#             self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
#                                                            '/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div['
#                                                            '2]/span').text
#             self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
#                                                          'div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div['
#                                                          '2]/div/div[2]/span').text
#         except Exception as e:
#             print("Error occurred:", e)
#
#     def tweet_at_provider(self):
#         pass
#
#
# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# print(f"Download speed: {bot.down} Mbps")
# print(f"Upload speed: {bot.up}")
# bot.tweet_at_provider()
########################################################################################################################

#                                                  REFERENCE CODE

# from selenium import webdriver
#
# PROMISED_DOWN = 150
# PROMISED_UP = 10
# TWITTER_EMAIL = "YOUR TWITTER EMAIL"
# TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"
#
#
# class InternetSpeedTwitterBot:
#     def __init__(self, driver_path):
#         self.driver = webdriver.Chrome()
#         self.up = 0
#         self.down = 0
#
#     def get_internet_speed(self):
#         pass
#
#     def tweet_at_provider(self):
#         pass
#
#
# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                           'div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div['
                                                           '2]/div/div[2]/span').text

        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                             '/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div['
                                                             '2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                         '/form/div/div[1]/label/div/div[2]/div/input')

        password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                            '/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div'
                                                                 '/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/'
                                                                 'div[2]/div[1]/div/div/div/div/div/div/div/div/div'
                                                                 '/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}" \
                f"up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                      '/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]'
                                                      '/div[4]/div/div/div[2]/div[3]')

        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
