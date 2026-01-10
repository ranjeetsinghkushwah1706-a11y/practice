class A:
    def show_a(self):
        print("This is class A")

class B:
    def show_b(self):
        print("This is class B")

class C(A, B):
    def show_c(self):
        print("This is class C")

c1 = C()
c1.show_a()
c1.show_b()
c1.show_c()
