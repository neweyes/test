# 快速排序实现说明

本项目实现了一个原地快速排序（In-place Quicksort）算法。该实现具有以下特点：

## 1. 算法特点

- **原地排序**：直接在原数组上进行操作，不需要额外的数组空间
- **不稳定排序**：相同元素的相对位置可能会改变
- **递归实现**：通过递归方式处理子数组

## 2. 性能特征

- **时间复杂度**：
  - 平均情况：O(n log n)
  - 最坏情况：O(n²)（当数组已排序或反向排序时）
  - 最好情况：O(n log n)
- **空间复杂度**：
  - O(log n)：仅需要递归调用的栈空间
  - 不需要额外的数组空间

## 3. 实现细节

### 3.1 主函数 `quicksort(arr)`

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    _quicksort(arr, 0, len(arr) - 1)
    return arr
```

- 处理基本情况（空数组或单元素数组）
- 调用内部函数 `_quicksort` 进行实际排序
- 返回排序后的数组（同一个对象）

### 3.2 递归排序函数 `_quicksort(arr, low, high)`

```python
def _quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        _quicksort(arr, low, pivot_index - 1)
        _quicksort(arr, pivot_index + 1, high)
```

- 使用分治策略
- 通过 `partition` 函数获取分区点
- 递归处理左右两个子数组

### 3.3 分区函数 `partition(arr, low, high)`

```python
def partition(arr, low, high):
    pivot = arr[high]      # 选择最右边的元素作为基准
    i = low - 1           # i 是小于区域的边界
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

- 使用 Lomuto 分区方案
- 选择最右边的元素作为基准（pivot）
- 将数组分为三部分：
  1. `[low, i]`：小于等于 pivot 的元素
  2. `[i+1, j-1]`：大于 pivot 的元素
  3. `[j, high-1]`：待处理的元素
- 最后将 pivot 放到正确的位置

## 4. 使用示例

```python
# 导入快速排序函数
from quicksort import quicksort

# 创建测试数组
arr = [3, 6, 8, 10, 1, 2, 1, 5, 7, 9]

# 排序数组
sorted_arr = quicksort(arr)
print(sorted_arr)  # 输出: [1, 1, 2, 3, 5, 6, 7, 8, 9, 10]
```

## 5. 性能测试

项目包含性能测试脚本 `performance_test.py`，可以比较自定义快速排序与 Python 内置排序的性能：

```python
python performance_test.py
```

测试结果显示：
- 对于 1000 个元素的数组：
  - 自定义快速排序平均耗时：~0.0005 秒
  - Python 内置排序平均耗时：~0.00006 秒

## 6. 优化空间

1. **基准选择优化**：
   - 可以使用三数取中法选择基准
   - 可以随机选择基准

2. **小数组优化**：
   - 对于小规模数组（如长度<=10），可以使用插入排序

3. **重复元素处理**：
   - 可以使用三路快排处理大量重复元素的情况

## 7. 注意事项

- 该实现不保证排序稳定性
- 对于已经排序的数组，性能可能退化为 O(n²)
- 递归深度可能达到 O(n)，极端情况下可能导致栈溢出