#sum of list elements
'''list=[3,4,5,6,7]
sum=0
for i in list:
    sum=sum+i
print(sum)'''

#find maximum and minimum without using max and min element in list
'''list=[8,10,8,4,5,4]
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i
        print(max)
        print(min)'''

#counting even and odd numbers in list
'''list=[1,2,3,4,5,6,7]
even=0
odd=0
for i in list:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers :",even)
print("odd numbers :",odd)
'''
#reverse the list without using reverse function
'''list[10,12,4,8,6]
list1=[]
for i in range (len(list)-1):
list1.append(list[i])
print(list1)'''
#multipy all elements in list
'''list=[2,3,4,5,6]
a=1
for i in list:
    a=a*i
print(a)'''

#merging two lists into one list
'''list1=[1,2,3,4]
list2=[6,7,8,9,10]
list3=[]
for i in list1:
    list3.append(i)
    for i in list2:
        list3.append(i)
    print(list3)'''
#write the vowels and consonants in a string
'''a=["Lion","Tiger","Cheetah","Elephant"]
b=['a','e','i','o','u']
for i in a:
    for j in i:
        if j.lower() in b:
            print(j,end=" ")
            print()'''
#print 0 at last
'''a=[1,0,1,0,2,4,0]
z=[]
nz=[]
for i in a:
    if i==0:
        z.append(i)
    else:
        nz.append(i)
print(nz+z)'''

#reversing a string without using reverse function
'''l=["hello","world","python","java"]
u=list(l)
j=len(u)-1
for i in range(len(u)):
    print(u[j],end=" ")
    j=j-1'''

    #reverse
'''l=[2,3,4,5,6]
j=len(l)-1
for i in range(len(l)):
    print(l[j],end=" ")
    j=j-1'''
#duplicates
'''l=[2,4,5,5,7]
u=[]
for i in l:
    if i not in u:
        u.append(i)
print(u)'''
#filtering of given no greater then list of no
'''l=[20,40,50,90]
a=20
for i in l:
    if a<i:
        print(i)'''
#find duplicates in list
'''l=[2,4,5,5,7]
s=[]
d=[]
for i in l:
    if i in s and i not in d:
        d.append(i)
    else:
        s.append(i)
print(d)
print(s)'''

