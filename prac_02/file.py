#task1
print('task1')
name = input('please enter ur name:')
fptr = open('name.txt', 'w')
print('name is : {}'.format(name), file = fptr)
fptr.close()
print('task1 done')

#task2
print('task2')
fptr = open('name.txt', 'r')
str = fptr.readline()
print(str)
fptr.close()
print('task2 done')

#task3
print('task3')
fptr = open('number.txt', 'r')

total = int(fptr.readline())
total = total+int(fptr.readline())
print(total)
fptr.close()
print('task3 done')



#task4
print('task4')
print('task4 done')