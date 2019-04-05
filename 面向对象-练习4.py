#校区信息
class School:
    def __init__(self,name):
        self.name=name

#课程信息:课程包含，周期，价格，通过校区创建课程
class Course(School):
    def __init__(self, name,day,price):
        School.__init__(self, name)
        self.day=day
        self.price=price

    def c1(self):
        print('%s：人工智能' % self.name)

    def c2(self):
        print('%s:区块链' % self.name)

    def c3(self):
        print('%s:数据分析' % self.name)

    def s1(self):
        print('%s：闵行校区' % self.name)

    def s2(self):
        print('%s:青浦校区' % self.name)


#老师信息：关联校区
class Teacher(Course):
    def __init__(self,name):
        School.__init__(self,name)

    def t1(self):
        print('%s：沈老师' % self.name)
        super().s1()

    def t2(self):
        print('%s:吴老师' % self.name)
        super().s2()

#校区创建班级信息:班级关联课程、讲师
class School2(Teacher,Course):
    def __init__(self, name):
        School.__init__(self, name)

    def s1(self):
        # print('%s：闵行校区' % self.name)
        super().s1()
        super().c2()

    def s2(self):
        # print('%s:青浦校区' % self.name)
        super().s2()
        super().c1()
        super().c3()

    def a1(self):
        print('%s：一班' % self.name)
        super().t1()

    def a2(self):
        print('%s:二班' % self.name)
        super().t2()

#学生信息:选择校区，关联班级
class Student(School2,Course):
    def __init__(self, name):
        School.__init__(self, name)

    def s3(self):
        # super().s1()
        super().a1()

    def s4(self):
        # super().s2()
        super().a2()




s=Student('anan')
s.s3()


s2=School2('一班')
# s2.s1()
s2.s1()
s2.a1()


t=Teacher('艾老师')
t.s2()

c=Course('语文',2,88)
c.s1()





