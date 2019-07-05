#!python3
# printTable.py - print table

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(data):
    colWidths = [0] * len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if colWidths[i] < len(data[i][j]):
                colWidths[i] = len(data[i][j])

    text = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = data[i][j].rjust(colWidths[i])
        text += '|'.join(data[i]) + '\n'

    print(text)


if __name__ == '__main__':
    print_table(tableData)