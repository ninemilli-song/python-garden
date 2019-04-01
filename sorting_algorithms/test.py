# from . import main
import sys
sys.path.append('/path')

if __name__ == '__main__':
    arr = main.bubble_sort([8, 3, 2, 6, 7, 1])
    print(arr)