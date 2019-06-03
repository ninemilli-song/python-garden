def bubble_sort(arr):
    """
    冒泡排序步骤遍历列表并比较相邻的元素对。如果元素顺序错误，则交换它们。
    重复遍历列表未排序部分的元素，直到完成列表排序。
    因为冒泡排序重复地通过列表的未排序部分，所以它具有最坏的情况复杂度O(n^2)。
    :param arr:
    :return:
    """
    print("******************************************************************************")
    print("****** 冒泡排序步骤遍历列表并比较相邻的元素对。如果元素顺序错误，则交换它们。")
    print("****** 重复遍历列表未排序部分的元素，直到完成列表排序。")
    print("****** 因为冒泡排序重复地通过列表的未排序部分，所以它具有最坏的情况复杂度O(n^2)。")
    print("******************************************************************************")

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr


def selection_sort(arr):
    """
    通过选择排序，我们将输入列表/数组分为两部分：已经排序的子列表和剩余要排序的子列表，
    它们构成了列表的其余部分。我们首先在未排序的子列表中找到最小的元素，并将其放置在排序的子列表的末尾。
    因此，我们不断地获取最小的未排序元素，并将其按排序顺序放置在排序的子列表中。
    此过程将重复进行，直到列表完全排序。
    :param arr:
    :return:
    """
    print("******************************************************************************")
    print("****** 通过选择排序，我们将输入列表/数组分为两部分：已经排序的子列表和剩余要排序的子列表，")
    print("****** 它们构成了列表的其余部分。我们首先在未排序的子列表中找到最小的元素，并将其放置在排序的子列表的末尾。")
    print("****** 因此，我们不断地获取最小的未排序元素，并将其按排序顺序放置在排序的子列表中。")
    print("****** 此过程将重复进行，直到列表完全排序。")
    print("******************************************************************************")

    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


def insertion_sort(arr):
    """
    在每个循环迭代中，插入排序从数组中删除一个元素。
    然后，它在另一个排序数组中找到该元素所属的位置，并将其插入其中。
    它重复这个过程，直到没有输入元素。
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr
