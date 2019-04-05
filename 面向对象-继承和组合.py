class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
#老师信息：
class Teach(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title = job_title
        self.courses=[]
        self.students=[]

#学生信息
class Student(People):
    def __init__(self,name,age,sex,school):
        People.__init__(self,name,age,sex)
        self.school=school
        self.courses=[]
#课程信息
class Course:
    def __init__(self,name,des,price):
        self.name=name
        self.des=des
        self.price=price

t=Teach('anan',36,'male','魏王')
s1=Student('a',18,'male','阳光小学')
s2=Student('b',28,'male','阳光幼儿园')
s3=Student('c',38,'male','阳光大学')

php=Course('数学','很好',58)
py=Course('语文','一般',66666)

t.courses.append(php)
t.courses.append(py)


t.students.append(s1)
t.students.append(s2)
t.students.append(s3)


for i in t.students:
    print(i)

print(php.name,php.des,php.price)
