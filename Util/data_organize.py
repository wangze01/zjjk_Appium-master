# -*-coding:utf-8 -*-
# @Author: Tibbers
# Created on: 2021-06-15

from Util.Excel_parse import HandleExcel


def test_data():
    exc = HandleExcel()
    exc_data = exc.get_all_data()
    result = []
    print('exc_data',exc_data)
    for item in exc_data:
        lst = []
        lst.append(item[0])
        lst.append(item[3].split('\n'))
        lst.append(item[5])
        result.append(lst)
        print('lst',lst)
        print('result',result)
    return result


if __name__ == "__main__":
    print(test_data())

