#! python3
# period.py - 录入期初数据，保存到 shelve 文件中
# 记录 基金编码（code） 起始时间（beginning） 起始金额（amount）

import shelve, time


def get_shelve():
    """
    open file
    :return: shelve Object
    """
    return shelve.open('./data/period_data')


def save(code, beginning, amount):
    """
    保存期初数据
    :param code: 基金代码
    :param beginning: 起始时间
    :param amount: 起始金额
    :return: None
    """
    shelf_file = get_shelve()
    if code is None:
        raise Exception('❌ Code is None, Please check it.')
    elif beginning is None:
        raise Exception('❗️Start time is None. Please check it.')
    elif amount is None:
        raise Exception('⚠️ Amount is None. Please check it.')
    data = {
        'code': code,
        'beginning': beginning,
        'amount': amount
    }
    shelf_file[code] = data
    print('🎯保存数据 => {}'.format(data))
    shelf_file.close()


def get(code):
    """
    根据编码返回数据
    编码为空返回全部数据
    :param code: 基金编码 可空
    :return: {} or List<{}>
    """
    sh = get_shelve()
    if code != '' and sh[code] is not None:
        return sh[code]
    else:
        items = []
        for item in sh.items():
            items.append(item[1])
        return items


def delete(code):
    """
    删除数据 - 编辑为空清空全部数据
    :param code: 指定基金编码
    :return: None
    """
    sh = get_shelve()
    if code != '' and sh[code] is not None:
        del sh[code]
        print('❗️删除数据 => {}'.format(code))
    elif code == '':
        for key in list(sh.keys()):
            del sh[key]
            print('❗️删除数据 => {}'.format(key))
    pass


def display(code):
    """
    显示期初数据
    :param code: 基金代码
    :return: None
    """
    # 打印表头
    table_header = ['基金编码'.center(12, '-'), '起始时间'.center(12, '-'), '金额'.center(12, '-')]
    print('|' + '|'.join(table_header) + '|')

    # 打印数据
    data = get(code)
    if isinstance(data, dict):
        # print('数据[{}] = [{}]'.format(code, data))
        row = [
            str(data['code']).ljust(12, '-'),
            str(data['beginning']).ljust(12, '-'),
            str(data['amount']).rjust(12, '-'),
        ]
        print('|' + '|'.join(row) + '|')
    elif isinstance(data, list):
        for item in data:
            row = [
                str(item['code']).ljust(12, '-'),
                str(item['beginning']).ljust(12, '-'),
                str(item['amount']).rjust(12, '-'),
            ]
            print('|' + '|'.join(row) + '|')

    # 打印表尾
    table_footer = ['-'*12, '-'*12, '-'*12]
    print('|' + '|'.join(table_footer) + '|')
    pass


def main():
    print('请输入您的操作（1 - 录入基金期初， 2 - 显示基金期初数据，3 - 删除基金期初数据， 0 - 退出）：')
    op = input()
    if op == '1':
        print('👉🏻基金代码：')
        code = input()
        print('👉🏻起始时间(YYYY/MM/DD)：')
        beginning = input()
        # 转换为时间戳
        mktime = time.mktime(time.strptime(beginning, '%Y/%m/%d'))
        print('👉🏻起始金额：')
        amount = input()
        save(code, mktime, amount)
    elif op == '2':
        print('👉🏻基金代码（不输入显示全部数据）：')
        code = input()
        display(code)
    elif op == '3':
        print('👉🏻基金代码（不输入会删除全部数据）：')
        code = input()
        delete(code)
    elif op == '0':
        exit()


if __name__ == '__main__':
    main()
