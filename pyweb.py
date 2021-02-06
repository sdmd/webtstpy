from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
import time
import schedule


print('The script test starts at', time.ctime())


def tst():
    print("I'm still working...")
    print(time.ctime())


def webauto():
    start_time = time.process_time()
    print('Starting the webautomation ', time.ctime())
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.get('https://ucam.uiu.ac.bd/Security/Login.aspx')
    # driver.maximize_window()
    time.sleep(3)
    print('Open webpage successfully')
    print('starting login process')

    username_field = driver.find_element_by_id('logMain_UserName')
    username_field.send_keys('*')
    username_field.send_keys(Keys.RETURN)
    print('userid done!')
    time.sleep(2)
    password_field = driver.find_element_by_id('logMain_Password')
    password_field.send_keys('*')
    password_field.send_keys(Keys.RETURN)
    print('password done!')

    print('You are logged in!')
    time.sleep(3)

    btn = driver.find_element_by_id('ctl00_lbtnIQAC')
    btn.click()
    time.sleep(1)
    print('Ending webpage ', time.ctime())
    # browser quit
    driver.quit()
    # total time calculate
    runtime = time.process_time() - start_time
    print("runtime is",  time.strftime("%H:%M:%S", time.gmtime(runtime)))
    print("  ")


schedule.every().sunday.at("15:50").do(tst)
schedule.every().minute.at(":10").do(webauto)


while True:
    schedule.run_pending()
    time.sleep(1)

