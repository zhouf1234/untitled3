#校区信息
class School:
    def __init__(self,name):
        self.name=name

    def s1(self):
        print('%s：闵行校区' % self.name)

    def s2(self):
        print('%s:青浦校区' % self.name)

#老师信息：
class Teacher(School):
    def __init__(self,name):
        School.__init__(self,name)

#学生信息
class Student(School):
    def __init__(self, name):
        School.__init__(self, name)


#课程信息
class Course(School):
    def __init__(self, name,day,price):
        School.__init__(self, name)
        self.day=day
        self.price=price

    def c1(self):
        print('%s：人工智能' % self.name)
        super().s2()

    def c2(self):
        print('%s:区块链' % self.name)
        super().s1()

    def c3(self):
        print('%s:数据分析' % self.name)
        super().s2()

#校区班级信息
class School2(Teacher,Course):
    def __init__(self, name):
        School.__init__(self, name)



#实例化
t=Teacher('林老师')
t.s1()

c=Course('语文',2,44)
c.c1()


s=Student('anan')
s.s1()


s2=School2('一班')
s2.c1()






