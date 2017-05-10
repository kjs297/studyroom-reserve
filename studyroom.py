import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass

### 사용자로부터 고려대학교 포탈 id와 password를 입력받는다.

user_id = input('ID를 입력하세요: ')
user_pwd = getpass.getpass('PWD를 입력하세요(Not echoing): ')

### 고려대학교 포탈에 GET 방식으로 접속한다.

print("(1/4) URL에 접속합니다...")
portal_url = 'http://portal.korea.ac.kr/front/Intro.kpd'

driver = webdriver.Chrome('C:/Users/asus/Desktop/Code/mine/Python/programs/studyroom-reserve/chromedriver.exe')
driver.get(portal_url)

### 고려대학교 포탈에 LOGIN을 실시한다.

print("(2/4) LOGIN을 실시합니다...")

input_id = driver.find_element_by_xpath("//input[@id='oneid']")
input_pwd = driver.find_element_by_name('pw')

input_id.send_keys(user_id)
input_pwd.send_keys(user_pwd)

btn_login = driver.find_element_by_class_name('submit')
ActionChains(driver).click(btn_login).perform()

### 로그인 후 상단 바에 있는 정보생활 버튼을 클릭한다.

print("(3/4) LOGIN이 완료되었습니다.")

btn_infolife = driver.find_element_by_xpath("//a[contains(.,'정보생활')]")
ActionChains(driver).click(btn_infolife).perform()

### 왼쪽 사이드 바에 있는 공간예약/관리를 클릭한다.

btn_space1 = driver.find_element_by_xpath("//li[@id='m143']")
ActionChains(driver).click(btn_space1).perform()

### 공간예약/관리의 하위 항목인 공간관리 및 예약신청을 클릭한다.

btn_space2 = driver.find_element_by_xpath("//li[@id='sm1260']")
ActionChains(driver).click(btn_space2).perform()

print("(4/4) 공간예약/관리 페이지에 접속되었습니다.")

### 숙제! 자동검색 탭 누르게까지 해보기




# reserve_url = "http://cafm.korea.ac.kr/archibus/connect.jsp"
# driver.get(reserve_url)
