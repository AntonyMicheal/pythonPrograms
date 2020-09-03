a={}
while True:
    ch = int(input('Enter your choice: 1.insert into Dictionary | 2.search student  details | 3.edit Student details'))
    if ch==1:
        n=int(input('enter the number of students whos details are to be entered: '))
        for i in range(2,n+2):
            roll=int(input('Enter the roll number of students: '))
            name=input('Enter name of the student: ')
            age = int(input('Enter the age of the student: '))
            b=[roll,name,age]
            a[roll]=b
        print(a)
    elif ch==2:
        print(a)
        search = int(input('Enter the roll number to be searched: '))
        if search in a:
            print(a[search])
        else:
            print('student not present in the dictionary')
    elif ch==3:
        edit = int(input('Enter the roll number to be edited: '))
        print(a)
        if edit in a:
            b=a[edit]
            newName=input('enter the name to replace: ')
            b[1]=newName
        print(a[edit])
                
            
        
            
