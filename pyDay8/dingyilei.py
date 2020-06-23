class Student():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print("{}正在学习{}".format(self.name,course_name))

    def watch_movie(self):
        if self.age < 18:
            print("{}只能看熊出没".format(self.name))
        else:
            print("{}正在看岛国".format(self.name))


#def main():
stu1 = Student('aa',25)
stu1.study('puupShenji')
stu1.watch_movie()

#main()
