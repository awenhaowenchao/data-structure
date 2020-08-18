from copy import copy


class ArrayList():

    def __init__(self, cap: int):
        self.orign_cap = cap
        self.l = [None] * cap
        self.cap = cap
        self.length = 0
        self.load_factor = 0.75

    def add(self, item):

        if (self.length >= self.cap * self.load_factor):
            # 扩展
            tmp = [None] * self.cap * 2
            tmp[0:self.cap] = copy(self.l)
            self.cap = self.cap * 2
            self.l = tmp
        self.l[self.length] = item
        self.length += 1

    def __str__(self):
        return str(self.l[0:self.length])

    def clear(self):
        self.l = [None] * self.orign_cap
        self.cap = self.orign_cap
        self.length = 0
        self.load_factor = 0.75

    def get(self, idx):
        if (self.length < idx):
            raise BaseException("下标越界")

        return self.l[idx]

    def remove(self, idx):
        if (self.length <= idx):
            raise BaseException("下标越界")
        tmp_value = self.l[idx]

        tmp = [None] * self.cap
        tmp_pos = 0
        for i in range(0, self.length):
            if i!=idx:
                tmp[tmp_pos] = self.l[i]
                tmp_pos +=1

        self.l = tmp
        self.length -= 1
        return tmp_value


al = ArrayList(8)
al.add(1)
al.add(2)
al.add(3)
al.add(4)
al.add(5)
print("al's cp %s" % al.cap)
al.add(6)
al.add(7)
al.add(3)
al.add(3)
print("al's cp %s" % al.cap)
print("al's cp %s" % al)

print(al.get(3))

print(al.remove(4))
print(al)
