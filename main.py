from webdriver import driver


driver.get('https://www.youtube.com/')
while True:
    try:
        skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
        skip.click()
    except:
        continue
