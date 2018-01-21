shoplist = ['apple','mango','carrot','banana']

name = 'swaroop'

#indexing or 'Subscription' operation
#索引活下标（Subscription）操作符

print('item 0 is',shoplist[0])
print('item 1 is',shoplist[1])
print('item 2 is',shoplist[2])
print('item 3 is',shoplist[3])
print('item -1 is',shoplist[-1])
print('item -2 is',shoplist[-2])
print('Character 0 is',name[0])

#Slicing on a list
print('item 1 to 3 is',shoplist[1:3])
print('item 2 to end is',shoplist[2:])
print('item 1 to -1 is',shoplist[1:-1])
print('item start to end is',shoplist[:])

#从某一字符串中切片
print('charaters 1 to 3 is',name[1:3])
print('charaters 2 to end is',name[2:])
print('charaters 1 to -1 is',name[1:-1])
print('charaters start to end is',name[:])
