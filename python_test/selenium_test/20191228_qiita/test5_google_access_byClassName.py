from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

# for i, g in enumerate(driver.find_elements_by_class_name("g")):
#     print("------ " + str(i+1) + " ------")
#     r = g.find_element_by_class_name("r")
#     print(r.find_element_by_tag_name("h3").text)  # タイトル
#     print("\t" + r.find_element_by_tag_name("a").get_attribute("href"))  # URL
#     s = g.find_element_by_class_name("s")
#     print("\t" + s.find_element_by_class_name("st").text)  # サマリー


for i, g in enumerate(driver.find_elements(By.CLASS_NAME, "g")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element(By.CLASS_NAME, "r")
    print(r.find_element(By.TAG_NAME, "h3").text)
    print("\t" + r.find_element(By.TAG_NAME, "a").get_attribute("href"))
    s = g.find_element(By.CLASS_NAME, "s")
    print("\t" + s.find_element(By.CLASS_NAME, "st").text)


driver.quit()