"""
井字棋建模
"""

theBoard = {
    'top-L': '',
    'top-M': '',
    'top-R': '',
    'mid-L': '',
    'mid-M': '',
    'mid-R': '',
    'low-L': '',
    'low-M': '',
    'low-R': ''
}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


def display_inventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v

    print('Total number of items: ' + str(total))


def add_to_inventory(inventory, addItems):
    for i in range(len(addItems)):
        # 设置默认值为0
        inventory.setdefault(addItems[i], 0)
        inventory[addItems[i]] += 1

    return inventory


if __name__ == '__main__':
    # display_inventory(stuff)
    # print_board(theBoard)
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = [
        'gold coin',
        'dagger',
        'gold coin',
        'gold coin',
        'ruby'
    ]

    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)