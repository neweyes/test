def quicksort(arr):
    """
    原地快速排序实现
    :param arr: 要排序的数组
    :return: 排序后的数组（同一个对象）
    """
    def _quicksort(arr, low, high):
        if low < high:
            # 找到分区点
            pivot_index = partition(arr, low, high)
            # 递归排序左右两部分
            _quicksort(arr, low, pivot_index - 1)
            _quicksort(arr, pivot_index + 1, high)
    
    def partition(arr, low, high):
        # 选择最右边的元素作为基准
        pivot = arr[high]
        # i 是小于区域的边界
        i = low - 1
        
        # 遍历数组，将小于基准的元素放到左边
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # 将基准元素放到正确的位置
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # 如果数组为空或只有一个元素，直接返回
    if len(arr) <= 1:
        return arr
    
    # 开始原地快速排序
    _quicksort(arr, 0, len(arr) - 1)
    return arr