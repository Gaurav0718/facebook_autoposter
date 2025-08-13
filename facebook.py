from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

# Enter credentials
email_element = driver.find_element(By.XPATH, '//*[@id="email"]')
sleep(3)
email_element.send_keys('6362802013')

password_element = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_element.send_keys('Gaurav@2000')
sleep(5)

# Click login
elem = driver.find_element(By.NAME, 'login')
elem.click()

# Pause here so you can solve CAPTCHA / 2FA manually
sleep(70)

# Wait for and click the "What's on your mind" box
wait = WebDriverWait(driver, 20)
post_element = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//div[@role="button"]//span[contains(text(), "What\'s on your mind")]')
))
post_element.click()
sleep(200)  # Pause so modal opens before next action


privacy_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Edit privacy. Sharing with Public. "]'))
)
privacy_button.click()
sleep(5)
#
only_me_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="_r_1h_"]')))
only_me_button.click()
sleep(20)
#
done_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Done")]'))
)
done_button.click()

write_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_a8"]')
write_element.send_keys('Hi this is a automation testing with selenium')
sleep(5)

post_done_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_YR"]')
post_done_element.click()
sleep(100)




