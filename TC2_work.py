import datetime
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# TC 2번 경로(현재 디렉토리 경로 내...)
TC1_RESULT = "__result2__"

'''
####### 자동화 케이스 2 ###################################################
## [1] Home화면의 Latest Blocks 들중 Transactions Value가 1이 나올때까지 검색하는 기능				
## [2] Transaction 클릭 전 화면 캡처 후 저장하고, 이동후 화면 캡처 후 저장						
########################################################################	
'''

def TC2():

    driver = webdriver.Chrome("./chromedriver.exe")


    url = 'https://explorer.kstadium.io/'
    driver.get(url)

    time.sleep(3)

    while True:
        # [1] Home화면의 Latest Blocks 들중 Transactions Value가 1이 나올때까지 검색하는 기능
        for i in range(2, 12):
            transaction_xpath = "//*[@id='root']/div[2]/main/section[2]/div/div[1]/table/tbody/tr[%d]/td[3]/a" % i
            transaction_value = driver.find_element(By.XPATH, value=transaction_xpath).text

            # if 정상 동작 확인
            if transaction_value != '0':
                # 현재 스크롤의 가장 아래로 내림
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                # blockheight_value
                blockheight_xpath = "//*[@id='root']/div[2]/main/section[2]/div/div[1]/table/tbody/tr[%d]/td[1]/a" % i
                blockheight_value = driver.find_element(By.XPATH, value=blockheight_xpath).text

                # 스크린 샷
                nowtime = datetime.datetime.now()
                driver.save_screenshot("C:\\Users\지창희\PycharmProjects\pythonProject\Prac_1\__result2__\TC2_capture" + nowtime.strftime('%Y%m%d_%H%M%S') + "_이전" + ".png")

                # transaction page로 이동
                pre_url = 'https://explorer.kstadium.io/block/%s' % blockheight_value
                url = pre_url + '/txs'
                driver.get(url)

                # 스크린 샷
                time.sleep(2)
                nowtime = datetime.datetime.now()
                driver.save_screenshot("C:\\Users\지창희\PycharmProjects\pythonProject\Prac_1\__result2__\TC2_capture" + nowtime.strftime('%Y%m%d_%H%M%S') + "_이후" + ".png")

                time.sleep(2)
                break
                driver.close()

            if i == 11:
                time.sleep(5)
                print("새로 시작")
                driver.refresh()
                time.sleep(3)

            print(i)
    end

if __name__ == '__main__':

    TC2()

