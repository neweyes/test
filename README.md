# Python Quicksort Implementation

这是一个用 Python 实现的快速排序算法项目，包含了完整的实现、测试用例和性能测试。

## 项目结构

```
├── quicksort.py      # 快速排序核心实现
├── main.py          # 主程序和基本测试用例
└── performance_test.py  # 性能测试和与内置排序的比较
```

## 功能特点

- 使用中间元素作为基准值（pivot）的快速排序实现
- 支持各种输入场景：
  - 空数组
  - 单元素数组
  - 已排序数组
  - 逆序数组
  - 包含重复元素的数组
- 包含性能测试，可与 Python 内置排序函数比较

## 使用方法

### 基本用法

```python
from quicksort import quicksort

# 对数组进行排序
array = [3, 6, 8, 10, 1, 2, 1, 5, 7, 9]
sorted_array = quicksort(array)
print(sorted_array)
```

### 运行测试

```bash
# 运行基本测试用例
python main.py

# 运行性能测试
python performance_test.py
```

## 性能测试

性能测试程序会：
1. 生成不同大小的随机数组
2. 比较自定义快速排序与 Python 内置排序的性能
3. 多次运行并计算平均执行时间

## 实现细节

快速排序算法的实现采用了以下策略：
1. 选择数组中间位置的元素作为基准值
2. 将数组分为三部分：小于基准值、等于基准值和大于基准值
3. 递归处理小于和大于基准值的部分
4. 最后合并所有部分得到有序数组

这种实现方式在处理包含重复元素的数组时特别高效。
