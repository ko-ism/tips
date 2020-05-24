from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')
# print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

stats = driver.find_element(by=By.ID, value="resultStats").text
stats = driver.find_element_by_id("resultStats").text
# # elements のように複数形にするとリストを取得できます
# stats = driver.find_elements(by=By.ID, value="resultStats")[0].text
# stats = driver.find_elements_by_id("resultStats")[0].text
# # CSSセレクタも使えますが By ID の方が効率がよいはず
# stats = driver.find_element_by_css_selector("#resultStats").text
# stats = driver.find_elements_by_css_selector("#resultStats")[0].text
print(stats)

# driver.save_screenshot('search_results.png')
driver.quit()