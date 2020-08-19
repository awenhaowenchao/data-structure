from copy import copy


class ArrayList():
    """
    数组列表
    """

    def __init__(self, cap: int=16):
        self.orign_cap = cap
        self._datas = [None] * cap
        self._cap = cap
        self._length = 0
        self.load_factor = 0.75

    def add(self, item):

        if (self._length >= self._cap * self.load_factor):
            # 扩展
            tmp = [None] * self._cap * 2
            tmp[0:self._cap] = copy(self._datas)
            self._cap = self._cap * 2
            self._datas = tmp
        self._datas[self._length] = item
        self._length += 1

    def __str__(self):
        return str(self._datas[0:self._length])

    def clear(self):
        self._datas = [None] * self.orign_cap
        self._cap = self.orign_cap
        self._length = 0
        self.load_factor = 0.75

    def get(self, idx):
        if (self._length < idx):
            raise BaseException("下标越界")

        return self._datas[idx]

    def size(self):
        return self._length

    def remove(self, idx):
        if (self._length <= idx):
            raise BaseException("下标越界")
        tmp_value = self._datas[idx]

        tmp = [None] * self._cap
        tmp_pos = 0
        for i in range(0, self._length):
            if i!=idx:
                tmp[tmp_pos] = self._datas[i]
                tmp_pos +=1

        self._datas = tmp
        self._length -= 1
        return tmp_value

    def is_empty(self):
        return 0 == self._length


