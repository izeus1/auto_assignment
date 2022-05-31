import datetime
import os
import time
from selenium.webdriver.common.by import By
import pandas as pd

from selenium import webdriver


# TC 3번 경로(현재 디렉토리 경로 내...)
TC3_RESULT = "__result3__"

'''
####### 자동화 케이스 3 ###################################################
## [1] Home화면에서 0xFc50afdd6db9dE442251f643b6Efb0A1926FE0b5 서칭				
## [2] 서칭 결과중 Overview 화면 캡처 저장 및 Balance 추출				
## [3] 서칭 결과중 Transaction table 추출 후 저장(File or google spreadsheet)							
########################################################################	
'''

def TC3():
    results = []
    each_result = []

    driver = webdriver.Chrome("./chromedriver.exe")

    url = 'https://explorer.kstadium.io/'
    driver.get(url)

    time.sleep(3)

    # 검색어 입력
    search_item = '0xFc50afdd6db9dE442251f643b6Efb0A1926FE0b5'

    search_bar = driver.find_element(By.XPATH, value="//*[@id='root']/div[2]/main/section[1]/div[1]/div/form/input")
    search_bar.send_keys(search_item)
    time.sleep(5)

    # 검색 버튼 클릭
    driver.find_element(By.XPATH,value="//*[@id='root']/div[2]/main/section[1]/div[1]/div/form/button").click()
    time.sleep(3)

    # 스크린 샷
    nowtime = datetime.datetime.now()
    driver.save_screenshot("C:\\Users\지창희\PycharmProjects\pythonProject\Prac_1\__result3__\TC3_capture" + nowtime.strftime(
        '%Y%m%d_%H%M%S') + ".png")
    time.sleep(1)

    # Balance 추출
    time.sleep(3)
    overview_Transactions_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[1]/td[2]"
    overview_Transactions_value = driver.find_element(By.XPATH, value=overview_Transactions_xpath).text

    print(overview_Transactions_value)

    # 서칭 결과중 Transaction table 추출 후 저장
    time.sleep(3)
    driver.find_element(By.XPATH, value="//*[@id='root']/div/main/section/div/div[1]/button[2]").click()
    time.sleep(3)

    # Transaction table 추출
    for i in range(2, 22):
        txnhash_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[1]/a" % i
        txnhash_value = driver.find_element(By.XPATH,value=txnhash_xpath).text

        method_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[2]" % i
        method_value = driver.find_element(By.XPATH, value=method_xpath).text

        block_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[3]/a" % i
        block_value = driver.find_element(By.XPATH, value=block_xpath).text

        age_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[4]" % i
        age_value = driver.find_element(By.XPATH, value=age_xpath).text

        from_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[5]/a" % i
        from_value = driver.find_element(By.XPATH, value=from_xpath).text

        to_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[6]" % i
        to_value = driver.find_element(By.XPATH, value=to_xpath).text

        value_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[7]" % i
        value = driver.find_element(By.XPATH, value=value_xpath).text


        each_result.append([txnhash_value, method_value, block_value, age_value, from_value, to_value, value])

    print(each_result)


    # 2번째 페이지 작업
    driver.find_element(By.XPATH, value="//*[@id='root']/div/main/section/div/div[2]/div/div/span[2]/a").click()

    time.sleep(5)

    for i in range(2, 9):
        txnhash_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[1]/a" % i
        txnhash_value = driver.find_element(By.XPATH, value=txnhash_xpath).text

        method_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[2]" % i
        method_value = driver.find_element(By.XPATH, value=method_xpath).text

        block_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[3]/a" % i
        block_value = driver.find_element(By.XPATH, value=block_xpath).text

        age_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[4]" % i
        age_value = driver.find_element(By.XPATH, value=age_xpath).text

        from_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[5]/a" % i
        from_value = driver.find_element(By.XPATH, value=from_xpath).text

        to_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[6]" % i
        to_value = driver.find_element(By.XPATH, value=to_xpath).text

        value_xpath = "//*[@id='root']/div/main/section/div/div[2]/table/tbody/tr[%d]/td[7]" % i
        value = driver.find_element(By.XPATH, value=value_xpath).text

        each_result.append([txnhash_value, method_value, block_value, age_value, from_value, to_value, value])

    print(each_result)

    # csv 저장
    table = pd.DataFrame(each_result, columns=['txnhash_value', 'method', 'block', 'age', 'from', 'to', value])

    if 'overview_blockchain.csv' not in os.listdir():
        table.to_csv(
            '{0}/transaction_table.csv'.format(TC3_RESULT),
            encoding='utf-8-sig',
            mode='w',
            index=True)
    else:
        table.to_csv(
            './transaction_table.csv'.format(TC3_RESULT),
            encoding='utf-8-sig',
            mode='a',
            index=True)


if __name__ == '__main__':

    TC3()

