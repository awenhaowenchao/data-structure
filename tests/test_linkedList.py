from src.chaptor_02.linkedlist import LinkedList

llist = LinkedList()

print(llist.size())
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print(llist.size())
print(llist)
llist.delete(2)
print(llist.size())
print(llist)

print(llist.get(2))
llist.remove(2)
print(llist)
print(llist.size())
