import decimal
import locale

from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import re
import openpyxl as xl
import numpy as np
from decimal import Decimal

d = {
        'K': 3,
        'M': 6,
        'B': 9
}
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
rows_with_no_data = []
def getData():
    session = Edge()
    session.get('https://www.benzinga.com/calendars/earnings')
    time.sleep(5)

    header = WebDriverWait(session, 100).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "ant-table-tbody")))
    element_list = header.find_elements(By.CSS_SELECTOR, 'tr.ant-table-row.ant-table-row-level-0')
    for count, value in enumerate(element_list):
        element_list[count] = value.get_attribute("innerText")
    session.quit()

    return element_list


def refine(element_list):
    clean_list = element_list
    for x in reversed(range(len(element_list))):
        list_text = element_list[x].split('\t')
        # clean_list[count] = list_text
        if len(list_text) < 5 or list_text[5] == "":
            del clean_list[x]
    for count, value in enumerate(clean_list):
        list_text = value.split('\t')
        clean_list[count] = list_text
    return clean_list


def process():
    stocks = getData()
    refined = refine(stocks)

    indices_to_delete = [3,7,11,12]
    refined = np.delete(refined, indices_to_delete, 1)


    EPS_estimated_growth_of_stocks = []
    Rev_estmated_growth_of_stocks = []
    percent_EPS_growth = 0
    percent_Rev_growth = 0


    for stock_info in refined:

        percent_EPS_growth = round((convertToNum(stock_info[4])- convertToNum(stock_info[3])) / (convertToNum(stock_info[3])+.000001)*100,2)
        percent_Rev_growth = round((convertToNum(stock_info[7]) - convertToNum(stock_info[6])) / convertToNum(stock_info[6]) * 100,2)
        EPS_estimated_growth_of_stocks.append(percent_EPS_growth)
        Rev_estmated_growth_of_stocks.append(percent_Rev_growth)


    refined = np.insert(refined, 5, EPS_estimated_growth_of_stocks,1)
    refined = np.insert(refined,9,Rev_estmated_growth_of_stocks,1)

    refined = refined.tolist()
    return refined

def convertToNum(text):
    if "$" in text:
        text = text.replace('$',"")
    if len(text) == 0:
        return 0
    elif text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        return float(num) * 10 ** d[magnitude]
    else:
        return float(text)


if __name__ == '__main__':
    list_of_stocks = getData()
    refined_list = refine(list_of_stocks)

