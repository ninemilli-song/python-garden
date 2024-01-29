#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
import os
import uuid


def get_dt_tree(dt, parent_uuid=-1):
    titles = []
    title_soup = dt.find('h3', recursive=False)
    title = {}
    if title_soup is not None:
        title = {
            'uuid': str(uuid.uuid1()),
            'parent_uuid': parent_uuid,
            'add_date': title_soup['add_date'],
            'icon': title_soup.get('icon'),
            'title': title_soup.get_text()
        }
        titles.append(title)

    bookmarks_soup = dt.find_all('a', recursive=False)
    bookmarks = []
    bookmark = {}
    for bookmark_soup in bookmarks_soup:
        bookmark = {
            'uuid': str(uuid.uuid1()),
            'parent_uuid': parent_uuid,
            'href': bookmark_soup['href'],
            'add_date': bookmark_soup['add_date'],
            'icon': bookmark_soup.get('icon'),
            'title': bookmark_soup.get_text()
        }
        bookmarks.append(bookmark)

    # Get dl -> dt
    if dt.dl is not None:
        # sub_trees = dt.dl.find_all('dt', recursive=False)
        # for sub_tree in sub_trees:
        #     sub_title, sub_bookmarks = get_dt_tree(sub_tree, title['uuid'])
        #     titles.extend(sub_title)
        #     bookmarks.extend(sub_bookmarks)

        dl_titles, dl_bookmarks = get_dl_tree(dt.dl, title['uuid'])
        titles.extend(dl_titles)
        bookmarks.extend(dl_bookmarks)

    return titles, bookmarks


def get_dl_tree(dl, parent_uuid=-1):
    dt_list = dl.find_all('dt', recursive=False)
    # print(dt_list)
    # print(f'dit_list length: {len(dt_list)}')
    # H3 and A Tag is DT tag direct chile, so get them

    all_titles = []
    all_bookmarks = []
    for dt in dt_list:
        # print(f'get dt: {dt}')
        # Get H3 tag
        titles, bookmarks = get_dt_tree(dt, parent_uuid)
        all_titles.extend(titles)
        all_bookmarks.extend(bookmarks)

    return all_titles, all_bookmarks


# Main function
def main(file_path):
    # Parse command line args, environment, etc.
    # Get json object from html file
    with open(file_path, 'rt') as file:
        data = file.read()

        soup = BeautifulSoup(data, 'html5lib')

    # print(soup.prettify())

    # get DL
    dl = soup.html.body.dl
    # dl = soup.select('dl', recursive=False)
    # print(f'get DL : {dl}')

    titles, bookmarks = get_dl_tree(dl)
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
        json.dump({
            'titles': titles,
            'bookmarks': bookmarks
        }, outfile, indent=2)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]}' ' [filepath]')
    file_path = sys.argv[1]
    main(file_path)