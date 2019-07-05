"""
4.10.1
"""


def listToStr(list):
    result = ''
    if len(list) == 0:
        return result
    elif len(list) == 1:
        return list[0]
    else:
        for i in range(len(list)):
            if i != len(list) - 1:
                result += list[i] + ','
            else:
                result += 'and ' + list[i]

        return result


"""
4.10.2
"""


def printGrid():
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if y == len(grid[x]) - 1:
                print(grid[x][y])
            else:
                print(grid[x][y], end='')




if __name__ == '__main__':
    printGrid()