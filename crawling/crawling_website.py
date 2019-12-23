#!python3
# -*- coding: utf-8 -*-
# crawling_website.py - 爬取网页内容，保存为 md 文件

import os
from bs4 import BeautifulSoup
import tomd
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
import re
import send2trash


# 转换 html to md
# Params:
#   html_str: html 字符串
#   target_class: node className
def gen_md(url, target_class):
    if url is not None:
        url = url.strip()
        response = requests.get(url)
        try:
            response.raise_for_status()
            # if response.status_code != 200:
            #     raise Exception('Request error! ', response.status_code)
        except Exception as err:
            print("There war a problem: %s" % (err))

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
        # 如果 output 目录下的 file_name 指定的文件存在则删除这个旧文件
        output_file_path = os.path.join(output_folder, file_name)
        if os.path.exists(output_file_path):
            send2trash.send2trash(output_file_path)

        print('Create {} beginning...'.format(file_name))
        # 打文件 如果不存在，生成新文件
        # r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
        # w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        # a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        # encoding='utf-8' 创建文件为 utf-8 编码格式，如果不指定会创建 ascii编码类型的文件，导致文件写入报错
        # output_file = open(os.path.join(output_folder, file_name), 'wb', encoding='utf-8')
        output_file = open(output_file_path, 'wb')
        # 写入文件内容 编辑为二进制
        content = md_str.encode('utf-8', 'ignore')
        # content = md_str.encode('utf-8', 'ignore').decode('utf-8')

        output_file.write(content)
        # 关闭文件
        output_file.close()
        print('Create {} completed.'.format(file_name))
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

    # 当前目录路径
    path = os.getcwd()
    print('Current work path is: ', path)
    # 判断当前目录下是否存在 output目录
    output_path = os.path.join(path, 'output')
    if os.path.exists(output_path) is False:
        # 如果不存在则创建 output 目录
        os.makedirs(output_path)
        print('Create output fold in ', output_path)

    # 自动生成文件名
    regex = re.compile(r'^(.+/)(.+)$')
    mo = regex.match(target_url)
    file_name = mo.group(2) + '.md'

    # 生成 md 内容
    md_content = gen_md(target_url, class_name)

    # 生成 md 文件
    create_md_file(md_content, output_path, file_name)
