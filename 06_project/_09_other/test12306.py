from splinter.browser import Browser

if __name__ == '__main__':
    browser = Browser(driver_name='chrome')
    browser.driver.maximize_window()
