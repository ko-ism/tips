from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')
# print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

for g_h3 in driver.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)

driver.save_screenshot('search_results.png')
driver.quit()