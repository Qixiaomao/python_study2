#ab是地址（Address）簿（Book）的缩写

ab = {
 'Swaroop':'swaroop@swaroopch.com',
 'Larry':'larry@wall.org',
 'Matsumoto':'matz@ruby-lang.org',
 'Spammer':'spammer@hotmail.com'
 
    }

print("Swaroop's address is",ab['Swaroop'])

#删除一堆键值一值配对

del ab['Spammer']

print("\n There are{}conntacts in the address-books\n".format(len(ab)))

for name,address in ab.items():
    print('Contact{}at{}'.format(name,address))

#添加一对键值一值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is",ab['Guido'])
