
def binary_search(list, item):#二分法 寻找一个数的位置
    low = 0
    n = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2) #python3 用int python2就不需要了，2默认向下取整
        n += 1
        guess = list[mid]
        if guess == item:
            return mid, n
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
    return None, n
my_list = [1, 3, 7, 5, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


def quick_sort(arr):#递归  快速排序
    if len(arr) == 1:#如果只有一个元素，返回本事，不用排序了
        return arr
    elif len(arr) == 2:#如果有两个，从小到大
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        p = arr[0]
        less = [i for i in arr[1:] if i <= p]
        great = [i for i in arr[1:] if i > p]
        return quick_sort(less) + [p] + quick_sort(great)
print(quick_sort([3,2,5,4,1]))
