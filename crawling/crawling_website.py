#!python3
# -*- coding: utf-8 -*-
# crawling_website.py - 爬取网页内容，保存为 md 文件

import os
from bs4 import BeautifulSoup
import tomd
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
import re


# 转换 html to md
# Params:
#   html_str: html 字符串
#   target_class: node className
def gen_md(url, target_class):
    if url is not None:
        url = url.strip()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception('Request error! ', response.status_code)
        except ReadTimeout:
            raise Exception('Timeout')
        except ConnectionError:
            raise Exception('Connect error')
        except RequestException:
            raise Exception('Error')
        soup = BeautifulSoup(response.content, 'html.parser')
        # 提取 html 内容
        content = str(soup.find_all(class_=target_class)[0])
        # 将 html 转换为 md
        md_str = tomd.convert(content)
        return md_str
    else:
        return None


# 创建 md 文件
def create_md_file(md_str, output_folder, file_name='unnamed.md'):
    if os.path.isdir(output_folder):
        print('Create {}.md beginning...'.format(file_name))
        # 打文件 如果不存在，生成新文件
        # r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
        # w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        # a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        # encoding='utf-8' 创建文件为 utf-8 编码格式，如果不指定会创建 ascii编码类型的文件，导致文件写入报错
        output_file = open(os.path.join(output_folder, file_name), 'w+', encoding='utf-8')
        # 写入文件内容
        content = md_str.encode('utf-8', 'ignore').decode('utf-8')
        # content =

        output_file.write(content)
        # 关闭文件
        output_file.close()
        print('Create {}.md completed.'.format(file_name))
    else:
        print('Output folder is error, Please check it exist! ------> ', output_folder)


if __name__ == '__main__':
    # 爬取网络页面
    while True:
        print('Please input your target web page:')
        target_url = str(input())
        if target_url is not None:
            break
        else:
            print('Press ctrl & c to exit')

    while True:
        print('Please input your target the node class name: ')
        class_name = input()
        if class_name is not None:
            break
        else:
            print('Press ctrl & c to exit')

    # 输入导出文件的目录
    while True:
        print('Please input your output fold: ')
        output_path = input()
        if os.path.isdir(output_path):
            break
        else:
            print('Press ctrl & c to exit')

    md_content = gen_md(target_url, class_name)

    # 自动生成文件名
    regex = re.compile(r'^(http|https)://(.+/)(.+)$')
    mo = regex.match(target_url)
    file_name = mo.group(3) + '.md'

    create_md_file(md_content, output_path, file_name)
