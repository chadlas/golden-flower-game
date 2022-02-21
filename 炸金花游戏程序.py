import random

class Carter:
    def __init__(self, cart_type, index):
        self.cart_type = cart_type
        self.index = index

    def show(self):
        print(self.cart_type, self.index)


class Human:
    def __init__(self, name, cart, level):
        self.name = name
        self.cart = cart
        self.level = level

    def show(self):
        print(self.name, self.level, end=" cart:\n")
        for i in self.cart:
            i.show()

    def get_name(self):
        return self.name


def transform(n):
    if n == "A":
        return 20
    elif n == "J":
        return 11
    elif n == "Q":
        return 12
    elif n == "K":
        return 13
    else:
        return n


def func(li):
    counter = 0
    for i in li:
        counter += transform(i.index)
    return counter


# 制作牌
cartList = []
for i in ["红桃", "黑桃", "梅花", "方块"]:
    cartList.append(Carter(i, "A"))
    for j in range(2, 11):
        cartList.append(Carter(i, j))
    for k in ["J", "Q", "K"]:
        cartList.append(Carter(i, k))
# 输出初始化状态
# for i in cartList:
#     i.show()

# 发牌
humanList = []
for i in range(5):
    humanList.append(Human("player" + str(ｉ + 1), [], 0))

for i in humanList:
    for j in range(3):
        res = cartList.pop(random.randint(0, len(cartList) - 1))
        # 输出随机pop的cart
        # res.show()
        i.cart.append(res)


# 发牌后的humanList
for i in humanList:
    # print(type(i.cart))
    for a in range(len(i.cart)):
        for b in range(a + 1, len(i.cart)):
            if transform(i.cart[a].index) > transform(i.cart[b].index):
                i.cart[a], i.cart[b] = i.cart[b], i.cart[a]
print("初始发牌：")
for i in humanList:
    i.show()
#
#
for i in humanList:
    # 豹子 ： 三张一样
    if i.cart[0].index == i.cart[1].index == i.cart[2].index:
        i.level += 100 * 4
        i.level += func(i.cart)
        # print("leve1")
    # 顺金 花色相同的顺子
    elif i.cart[0].cart_type == i.cart[1].cart_type == i.cart[2].cart_type and transform(
            i.cart[0].index) + 2 == transform(i.cart[1].index) + 1 == transform(i.cart[2].index):
        i.level += 100 * 3
        i.level += func(i.cart)
        # print("leve2")
    # 顺子
    elif transform(i.cart[0].index) + 2 == transform(i.cart[1].index) + 1 == transform(i.cart[2].index):
        i.level += 100 * 2
        i.level += func(i.cart)
        # print("leve3")
    # 对子
    elif i.cart[0].index == i.cart[1].index or i.cart[0].index == i.cart[2].index or i.cart[1].index == i.cart[2].index:
        i.level += 100
        i.level += func(i.cart)
        # print("leve4")
    # 单张
    else:
        i.level += func(i.cart)
        # print("leve5")
# 输出包括level的信息
# for i in humanList:
#     i.show()
# for i in range(3):
#     for j in range(i, 3 - i):
#         if (humanList[i].level > humanList[j]):
#             humanList[i],

for i in range(len(humanList)):
    for j in range(i + 1, len(humanList)):
        if humanList[i].level < humanList[j].level:
            humanList[i], humanList[j] = humanList[j], humanList[i]

print("按照牌的大小排序：")
for i in humanList:
    i.show()
print("玩家名次：")
for i in humanList:
    print(i.get_name())
