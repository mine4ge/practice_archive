# NHKニュース(https://www3.nhk.or.jp/news)のトップニュースの記事タイトルを取得する
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def nhk_topnews_titles():
  # driverのpathを指定
  serv = Service('./venv/bin/chromedriver')

  # ユーザーエージェントに連絡先を明示
  opts = Options()
  opts.add_argument('user-agent=test crawler; e-mail(3ne4gehira@gmail.com)')

  # driver(ブラウザ)の起動
  driver = webdriver.Chrome(service=serv, options=opts)

  # NHKニュースへ遷移
  driver.get("https://www3.nhk.or.jp/news/")
  agent = driver.execute_script("return navigator.userAgent")

  # 要素が表示されるまで待つ
  driver.implicitly_wait(10)
  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "module--featured-articles--tokushu-web")))

  # ニュースのタイトルを検索(一致するもの全て)
  condition = '//article[@class="module module--news-main index-main"]//em[@class="title"]'
  elements = driver.find_elements(By.XPATH, condition)
  if len(elements)==0:
    print('ニュースが取得できません')
  else:
    for e in elements:
      print(e.text)

  quit()

if __name__ == '__main__':
  nhk_topnews_titles()
