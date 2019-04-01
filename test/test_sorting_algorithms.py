from sorting_algorithms import main as sort

if __name__ == '__main__':
    action = input("Which method is your prefer to sort your array? "
                   "[B]ubble_sort, [S]election_sort, [I]nsertion_sort, [M]erge_sort, [P]artition").upper()

    if action not in "BSIMP" or len(action) != 1:
        print("I'm confused!")

    arr = input('Please input a number list such as 1, 3, 2, 4, which your want to sort: ').replace(' ', '').split(',')
    if action == 'B':
        sortedArr = sort.bubble_sort(arr)
    elif action == 'S':
        sortedArr = sort.selection_sort(arr)

    print('🌹 sorted list is : ', sortedArr)
