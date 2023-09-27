# 1
def decimal_to_binary(decimal_num, num_of_places=8):
    # 将小数部分转换为二进制
    binary_fraction = ""
    for _ in range(num_of_places):
        decimal_num *= 2
        if decimal_num >= 1:
            binary_fraction += "1"
            decimal_num -= 1
        else:
            binary_fraction += "0"
    return binary_fraction
# 输入一个十进制小数
decimal_number = 0.625
# 将整数部分和小数部分分开
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part
# 将整数部分转换为二进制
binary_integer = bin(integer_part)[2:]  # 去掉'0b'前缀
# 将小数部分转换为二进制，这里假设取8位小数部分
binary_fraction = decimal_to_binary(fractional_part, num_of_places=8)
# 输出二进制表示
binary_representation = f"{binary_integer}.{binary_fraction}"
print(f"十进制数 {decimal_number} 转换为二进制为 {binary_representation}")
# 2
import random
# 生成一个随机浮点数，范围在[10, 20]
random_float = random.uniform(10, 20)
# 打印生成的随机浮点数
print("随机浮点数:", random_float)
# 3
import re
def validate_id_card(id_card):
    # 定义身份证号的正则表达式模式
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}(\d|X|x)$'
    # 使用正则表达式匹配身份证号
    if re.match(pattern, id_card):
        return True
    else:
        return False
# 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # 在链表尾部添加一个节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    # 在指定位置插入一个节点
    def insert(self, data, position):
        if position < 0:
            raise ValueError("Invalid position")
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while count < position - 1:
            current = current.next
            count += 1
            if current is None:
                raise ValueError("Invalid position")
        new_node.next = current.next
        current.next = new_node
    # 删除第一个匹配的节点
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    # 查找节点
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    # 打印链表
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# 5
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
# 6
# 获取用户输入的百分制成绩
score = float(input("请输入百分制成绩: "))
# 使用if语句将百分制成绩转换为等级制
if score < 60:
    grade = "不合格"
elif score >= 60 and score <= 74:
    grade = "合格"
elif score >= 75 and score <= 89:
    grade = "良好"
else:
    grade = "优秀"
# 输出等级
print("等级制成绩:", grade)
# 7
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# 获取用户输入的两个正整数
num1 = int(input("请输入第一个正整数: "))
num2 = int(input("请输入第二个正整数: "))
# 调用gcd函数计算最大公约数
result = gcd(num1, num2)
# 输出最大公约数
print(f"{num1} 和 {num2} 的最大公约数是 {result}")
# 8
import random
import time
from sorting_algorithms import selection_sort, merge_sort
# 定义选择排序算法
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
# 定义归并排序算法
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
# 生成多组随机数列
def generate_random_arrays(num_arrays, max_length, max_value):
    random_arrays = []
    for _ in range(num_arrays):
        array_length = random.randint(1, max_length)
        random_array = [random.randint(1, max_value) for _ in range(array_length)]
        random_arrays.append(random_array)
    return random_arrays
# 9
def construct_array_b(A):
    n = len(A)
    # 初始化左边乘积数组和右边乘积数组
    left = [1] * n
    right = [1] * n
    # 计算左边乘积数组
    left_product = 1
    for i in range(1, n):
        left_product *= A[i - 1]
        left[i] = left_product
    # 计算右边乘积数组
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= A[i + 1]
        right[i] = right_product
    # 构建数组B
    B = [left[i] * right[i] for i in range(n)]
    return B
# 1
def is_prime(a):
    if a <= 1:
        return False  # 1和负数都不是质数
    # 2是唯一的偶数质数
    if a == 2:
        return True
    # 如果a是偶数，它不是质数
    if a % 2 == 0:
        return False
    # 从3开始，每次增加2，只检查奇数
    for i in range(3, int(a**0.5) + 1, 2):
        if a % i == 0:
            return False
    return True
# 获取用户输入的数
a = int(input("请输入一个整数："))
# 判断a是否为质数
if is_prime(a):
    print(f"{a} 是质数")
else:
    print(f"{a} 不是质数")
# 2
import time
# 记录程序开始时间
start_time = time.time()
# 这里放入您的程序代码

# 记录程序结束时间
end_time = time.time()
# 计算程序执行时间
execution_time = end_time - start_time
print(f"程序执行时间：{execution_time:.6f} 秒")
# 3
def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 从第二个元素开始，将其插入到已排序部分的合适位置
        key = arr[i]
        j = i - 1
        # 将比key大的元素向后移动，为key腾出位置
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入key到合适位置
        arr[j + 1] = key
# 4
# 时间复杂度：最坏：O(n^2) 平均:O(n^(3/2)) 空间复杂度：O(1)