'''assingments_list=[]
Students_names=[]
Students_marks=[]
number_of_students=int(input("Enter the number of students"))
for i in range(number_of_students):
    print("Enter the students details:")
    names_of_students=input("Enter the names of the students") 
        #Students_names.append(names_of_students)
    marks_of_students=int(input("enter the marks of the students"))
    Students_names.append(names_of_students)
    Students_marks.append(marks_of_students)
    print("Displaying the names of the students:")
for i in range(len(Students_names)):
    print(f"{Students_names[i]},{Students_marks[i]}")
    
j=0
count=0
while j<len(Students_marks):
    if Students_marks[j]>75:
        count=count+1
        print("the number of students scored above 75",count)
        j=j+1
    else:
        print("no student scored above 75")

Students_names.upper()
print(Students_names)'''

books=["harry potter","To kill a mocking bird","1984","The great gatsby"]
authors=["J.K Rowling","Harper Lee","George Orwell","F.Scott Fitzgerald"]
status=["available","checkout","available","checkout"]
search_book=[]
title=[]
for i in range(len(books)):
    print(f"{books[i]},{authors[i]},{status[i]}")
    print("Displaying the books which are available:")
    search_book(title)
if title in books:
    index=books.index(title)
    print(f"{books[index]},{authors[index]},{status[index]}")
else:
    print("book not there")
    

    