from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

# ...省略...
# タイムアウト時間を固定するならまとめておく
wait = WebDriverWait(driver, 10)  # Timeout 10秒（最大待ち時間）

# 例1: すべて読み込まれて"Google"を含むタイトルが表示されるまで待つ
driver.get('https://www.google.com')
wait.until(EC.title_contains("Google"))

# # 例2: 何かをクリックしてから、innerTextに"ほげ"を持ちかつclass属性が hoge である要素が現れるのを待つ。
# element = find_element...
# element.click()
# wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "hoge"), "ほげ")
# )

# # 例3: class属性が fuga である要素が visible になるのを待ってからクリックする。
# xpath = "//a[@class='fuga']"
# a = wait.until(
#     EC.visibility_of_element_located((By.XPATH, xpath))
# )
# a.click()

driver.quit()