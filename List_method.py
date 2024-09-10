# List Methods
# append():
a=[1,2,3,4,5]
a.append(6)
print(a)
d=[1,2,3]
d.append([4,5])
print(d)

# extend():
a=[10,20,30,40,50]
b=[60,70,80,90,100]
a.extend(b)
print(a)
b=[1,2,3]
b.extend([4,5])
print(b)

#insert():
n=['a','b','c','d','e']
n.insert(2,'h')
print(n)

# clear():
items = ['yogi',1,2,3]
items.clear()
print(items)

# copy():
co=['a','b','c']
print('original:',co)
ni=co.copy()
print('after:',ni)

#count():
data=['h','i','y','o','g','e','e','s','h','k','p']
count = data.count('p')
print("the count of 'p' is:",count)
count = data.count('e')
print("the count of 'e' is:",count)

#reverse():
list=[1,2,3]
list.reverse()
print("using list reverse:",list)

#remove():
go=['apple','mango','cherry']
go.remove('mango')
print(go)

#sort():
my_list=['apple','mango','orange','banana']
my_num=[4,5,6,1,2,3]
my_list.sort()
my_num.sort()
print(my_num)
print(my_list)

#pop():
pop=[1,2,3]
pop.pop()
print(pop)
y=[1,2,3,4,5]
y.pop(3)
print(y)

#index():
n=[10,20,30,40,50]
print("list of index and value")
for i in range(len(n)):
    print('index number:',i,'index value:',n[i])
