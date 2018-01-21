#我会推荐你总是使用口号
#来指明元祖的开始与结束
#尽管括号是一个可选选项
#明了胜过晦涩，显式优于隐式

zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))


new_zoo = 'monkey','camel',zoo
print('Number off cages in the zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo[2])
print('Animals brought from old zoo are',new_zoo)
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',\
len(new_zoo)-1+len(new_zoo[2]))

