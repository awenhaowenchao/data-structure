from src.chaptor_02.arraylist import ArrayList

alist = ArrayList(8)
alist.add(1)
alist.add(2)
alist.add(3)
alist.add(4)
alist.add(5)
print("al's cp %s" % alist._cap)
alist.add(6)
alist.add(7)
alist.add(3)
alist.add(3)
print("al's cp %s" % alist._cap)
print("al's cp %s" % alist)

print(alist.get(3))

print(alist.remove(4))
print(alist)

print(alist.size())

print(alist.is_empty())
