def calltime(x, h, t):
    # 导入 math 模块，用于使用数学函数，如平方根计算
    import math
    # 定义重力加速度，单位为 m/s²
    g = 9.8
    # 累加小球下落过程的路程，初始高度即为下落距离
    x += h
    # 计算小球下落的时间，根据自由落体运动公式 t = sqrt(2h/g)
    t += math.sqrt(2 * h / g)
    # 计算小球反弹后的高度，每次反弹高度为前一次高度的一半
    h = h / 2
    # 计算小球反弹的时间，反弹过程与下落过程对称，时间计算方式相同
    t += math.sqrt(2 * h / g)
    # 累加小球反弹过程的路程，即反弹高度
    x += h
    # 返回当前的总路程、当前反弹高度和当前总时间
    return x,h,t
#定义总的小球下降到上升的函数
def sum_time(x, h, t, n):
    # 循环 n 次，模拟小球的 n 次反弹过程
    for i in range(1, n + 1):
       # 调用 calltime 函数进行一次反弹过程的计算，并更新总路程、当前反弹高度和总时间
        x, h, t = calltime(x, h, t)
    # 返回最终的总路程、最终反弹高度和总时间
    return x,h,t
# 提示用户输入小球的初始高度，并将输入转换为浮点数
h = float(input("请输入小球的初始高度（米）："))
# 提示用户输入小球的反弹次数
n_input = input("请输入小球的反弹次数：")

# 检查输入是否为正整数，不然直接报错。
if not n_input.isdigit() or int(n_input) <= 0:
    print("反弹次数必须是正整数，请重新运行程序并输入有效的正整数。")
else:
    n = int(n_input)
    # 初始化总路程为 0
    x = 0
    # 初始化总时间为 0
    t = 0
    # 调用 sum_time 函数，根据用户输入的初始高度和反弹次数计算总路程、最终反弹高度和总时间
    x, h, t = sum_time(x, h, t, n)
        # 打印最终的反弹高度、总路程和总时间，保留两位小数
    print("反弹了{:.2f}m，此时球一共经过{:.2f}m，运动了{:.2f}s".format(h, x, t))
