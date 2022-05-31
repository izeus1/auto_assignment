import os
import time
import random
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver



# TC 1번 경로(현재 디렉토리 경로 내...)
TC1_RESULT = "__result__"
'''
####### 자동화 케이스 1 ###################################################
## [1] Home화면의 Latest Blocks 들중 하나를 랜덤으로 선택 후				
## [2] Block Height 클릭 후 연결되는 Overview화면의 Block Height값이 일치 확인				
## [3] Overview화면의 데이터를 결과로 출력(File or google spreadsheet)				
## [4] (Block Height, Timestamp, Transactions, Block Reward)		
########################################################################	
'''

def TC1():

    results = []


    driver = webdriver.Chrome("./chromedriver.exe")

    url = 'https://explorer.kstadium.io/'
    driver.get(url)

    time.sleep(3)

    # [1] Home화면의 Latest Blocks 들중 하나를 랜덤으로 선택 후 >> 랜덤 선택된 block_height_num get
    i = random.randrange(2, 12)
    random_block_height_xpath = "//*[@id='root']/div[2]/main/section[2]/div/div[1]/table/tbody/tr[%d]/td[1]/a" % i

    random_block_height = driver.find_element(By.XPATH, value=random_block_height_xpath).text

    url = 'https://explorer.kstadium.io/block/%s' % random_block_height
    driver.get(url)

    time.sleep(10)
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id='root']/div/main/section/div/div/div[2]/table/tbody/tr[1]/td[2]'))
    # print(element)


    # Block Details page
    # overview_BlockHeight_value_xpath = "//*[@id='root']/div/main/section/div/div/div[2]/table"
    overview_BlockHeight_value_xpath = "//*[@id='root']/div/main/section/div/div/div[2]/table/tbody/tr[1]/td[2]"
    overview_BlockHeight_value = driver.find_element(By.XPATH, value=overview_BlockHeight_value_xpath).text

    overview_Timestamp_value_xpath = "//*[@id='root']/div/main/section/div/div/div[2]/table/tbody/tr[2]/td[2]"
    overview_Timestamp_value = driver.find_element(By.XPATH, value=overview_Timestamp_value_xpath).text

    overview_Transaction_value_xpath = "//*[@id='root']/div/main/section/div/div/div[2]/table/tbody/tr[3]/td[2]/a"
    overview_Transaction_value = driver.find_element(By.XPATH, value=overview_Transaction_value_xpath).text

    overview_BlockReward_value_xpath = "//*[@id='root']/div/main/section/div/div/div[2]/table/tbody/tr[4]/td[2]"
    overview_BlockReward_value = driver.find_element(By.XPATH, value=overview_BlockReward_value_xpath).text

    # 확인용
    print(random_block_height)
    print(overview_BlockHeight_value)

    if random_block_height == overview_BlockHeight_value:
        print("랜덤 블록 하이트 값과 오버뷰 블록 하이트 값이 같습니다.")
    else:
        print("랜덤 블록 하이트 값과 오버뷰 블록 하이트 값이 다릅니다.")

    # csv 저장
    results.append([overview_BlockHeight_value, overview_Timestamp_value, overview_Transaction_value, overview_BlockReward_value])

    table = pd.DataFrame(results, columns=['blockheight', 'timestamp', 'transaction', 'blockreward'])

    if 'overview_blockchain.csv' not in os.listdir():
        table.to_csv(
            '{0}/overview_blockchain.csv'.format(TC1_RESULT),
            encoding='utf-8-sig',
            mode='w',
            index=True)
    else:
        table.to_csv(
            './overview_blockchain.csv'.format(TC1_RESULT),
            encoding='utf-8-sig',
            mode='a',
            index=True)



if __name__ == '__main__':

    TC1()

