class myClass():
    def method1(self):
        print "Guru99"

    def method2(self):
        print "Software Testing:"


class childClass(myClass):
    def method1(self):
     myClass.method1(self);
     print "Child Class Method1"

    def method2(self):
        print "childClass method2"


def main():
    c1=myClass()
    c1.method1()
    print "a"
    c1.method2()
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    print "b"
    c2.method2()
    print "c"


if __name__ == "__main__":
    main()