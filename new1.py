def find_max_product(n):
    quotient = n // 3
    remainder = n % 3
    if remainder == 1:
        quotient -= 1
        remainder += 3
    return [3] * quotient + [remainder]

n = 2001
result = find_max_product(n)
print(result)
print(2**10,2**20,2**30,2**40,2**50)
def valid_state(state):
    # 判断当前状态是否合法
    if state[1] == state[2] and state[0] != state[1]:
        return False
    if state[2] == state[3] and state[0] != state[2]:
        return False
    return True

def search(state, visited, path):
    # 深度优先搜索
    visited.append(state)  # 将当前状态添加到访问列表

    if state == (1, 1, 1, 1):
        # 已经到达目标状态
        print("可行方案: ", path)
        return

    for i in range(4):
        if state[i] == state[0]:
            # 当前物体在同一岸，可以选择带或不带这个物体
            new_state = list(state)
            new_state[0] = 1 - new_state[0]
            new_state[i] = 1 - new_state[i]

            if tuple(new_state) not in visited and valid_state(new_state):
                # 如果新状态没有访问过且是合法状态，继续搜索
                search(tuple(new_state), visited, path + [new_state])

        else:
            # 当前物体在不同岸，只能选择带这个物体
            new_state = list(state)
            new_state[0] = 1 - new_state[0]
            new_state[i] = 1 - new_state[i]

            if tuple(new_state) not in visited and valid_state(new_state):
                # 如果新状态没有访问过且是合法状态，继续搜索
                search(tuple(new_state), visited, path + [new_state])

# 初始化起始状态
start_state = (0, 0, 0, 0)

# 初始化访问列表和路径
visited = []
path = [start_state]

# 开始搜索
search(start_state, visited, path)
def square_root_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
    while(abs(g*g-c)>0.0001):
        g+=0.00001
        i=i+1
        print("%d:g=%.5f"%(i,g))
square_root_1()
def square_root_3():
    c=2
    g=c/2
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
square_root_3()
def square_root_3():
    c=2000
    g=c/2
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
square_root_3()
def square_root_3():
    c=2
    g=c
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
square_root_3()
def square_root_3():
    c=2
    g=c/4
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
square_root_3()
c = 10  # 方程中的常数

x = 1  # 初始化猜测值

# 迭代计算改进猜测值
for _ in range(10):  # 设置最大迭代次数为10
    fx = x ** 3 - c  # 计算函数值 f(x)
    fpx = 3 * x ** 2  # 计算函数导数值 f'(x)
    x = x - fx / fpx  # 更新猜测值

print("解为:", x)
import math

# Leibniz Series
def leibniz_series(n):
    approx_pi = 0
    sign = 1
    for i in range(n):
        term = 1 / (2 * i + 1)
        approx_pi += sign * term
        sign *= -1
    return 4 * approx_pi

# Archimedes' Method
def archimedes_method(iterations):
    sides = 6  # Initial number of sides (hexagon)
    radius = 1  # Radius of the circle

    for i in range(iterations):
        perimeter_poly = sides * 2 * radius
        apothem = math.sqrt(radius ** 2 - (perimeter_poly / (2 * sides)) ** 2)
        sides *= 2  # Double the number of sides for the next iteration

    approx_pi = perimeter_poly / (2 * apothem)
    return approx_pi

# Machin's Method
def machin_method():
    approx_pi = 4 * (4 * math.atan(1/5) - math.atan(1/239))
    return approx_pi

# Calculate π using different methods
leibniz_approx = leibniz_series(10**7)
archimedes_approx = archimedes_method(20)
machin_approx = machin_method()

# Compare the results
exact_pi = math.pi
print("Exact value of π:", exact_pi)
print("Approximation using Leibniz Series:", leibniz_approx)
print("Approximation using Archimedes' Method:", archimedes_approx)
print("Approximation using Machin's Method:", machin_approx)

# Calculate the differences from the exact value
leibniz_diff = abs(exact_pi - leibniz_approx)
archimedes_diff = abs(exact_pi - archimedes_approx)
machin_diff = abs(exact_pi - machin_approx)

print("Difference from exact value using Leibniz Series:", leibniz_diff)
print("Difference from exact value using Archimedes' Method:", archimedes_diff)
print("Difference from exact value using Machin's Method:", machin_diff)
import random
import math


def monte_carlo_integration(f, a, b, num_samples):
    integral_sum = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        integral_sum += f(x)

    integral_avg = integral_sum / num_samples
    integral_value = (b - a) * integral_avg
    return integral_value


def func(x):
    return x ** 2 + 4 * x * math.sin(x)


a = 2  # Lower limit of integration
b = 3  # Upper limit of integration
num_samples = 10 ** 6  # Number of random samples

integral_approx = monte_carlo_integration(func, a, b, num_samples)
print("Approximation of the definite integral:", integral_approx)