# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n+2

# print(L)

# L = ['A','B','C','D','E','F','G']
L = list(range(100))
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# r = L[0:4] # 切片，从第0个开始取出4个元素
# r = L[-2:] #倒数切片
# r = L[::2] #每两个取一个
r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:10:2] # 前10个，每两个取一个
print(r)
