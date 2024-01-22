#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
import os

# Main function
def main(file_path):
    # Parse command line args, environment, etc.
    with open(file_path, 'rt') as file:
        data = file.read()

        soup = BeautifulSoup(data, 'html.parser')

    # Get json object from html file
    bookmarks = []
    for link in soup.find_all('a'):
        # print(f'link attrs : {link}')
        bookmark = {
            'href': link['href'],
            'add_date': link['add_date'],
            'icon': link.get('icon'),
            'description': link.get_text()
        }
        bookmarks.append(bookmark)

    # print('generate bookmarks: ', bookmarks)

    # write bookmarks to json
    # path = os.getcwd()
    path = sys.path[0]

    # 判断当前目录下是否存在 output目录
    output_path = os.path.join(path, 'output')
    # print('Current work path is: ', output_path)
    if os.path.exists(output_path) is False:
        # 如果不存在则创建 output 目录
        os.makedirs(output_path)
        print('Create output fold in ', output_path)

    with open(f'{output_path}/bookmark.json', 'w+') as outfile:
        json.dump(bookmarks, outfile, indent = 2)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' ' [filepath]')
    file_path = sys.argv[1]
    main(file_path)