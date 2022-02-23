
from selenium import webdriver
from bs4 import BeautifulSoup

def get_lecture(id, pw):
    browswer = webdriver.Chrome('./webdriver/chromedriver.exe')

    browswer.get('https://ecampus.kangnam.ac.kr/login.php')

    browswer.find_element_by_name('username').send_keys(id)
    browswer.find_element_by_name('password').send_keys(pw)
    browswer.find_element_by_name('loginbutton').click()

    browswer.get('https://ecampus.kangnam.ac.kr/local/ubion/user/?ctype=R')
    html = browswer.page_source
    soup = BeautifulSoup(html, 'html.parser')
    li = soup.select('.coursefullname')

    #사용자별 수강과목 리스트
    for i in li:
        print(i.text) 

id = '강남대학교 웹사이트 ID(학번)'
pw = '강남대학교 웹사이트 PW(비밀번호)'

get_lecture(id, pw)
