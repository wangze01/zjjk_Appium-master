# -*-coding:utf-8 -*-
# @Author: Tibbers
# Created on: 2021-06-15

import yaml
from Log.logger_handler import Logger
from Config.project_var import project_var

logger = Logger(logger='yaml_handle').getlog()


class Yaml:
    def get_yaml(self, file_name, keyword):
        file_path = project_var + file_name
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                cont = f.read()
                yaml_obj = yaml.load(cont, Loader=yaml.FullLoader)

                return yaml_obj[keyword]
        except Exception as e:
            logger.error('读取设备配置信息文件失败：{}'.format(e))


if __name__ == '__main__':
    file = '\Page_case\Home_search.yaml'
    kw = 'case01'
    data = Yaml().get_yaml(file, kw)
    # print(len(data))
    # for key, item in data.items():
    print(data)
    # print(type(data['case01']['']['element_info']))
