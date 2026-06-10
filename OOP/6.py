import os
os.system("cls")

class A:
    def move(self):
        print("A class moving...")
    
class B(A):
    def jump(self):
        print("B class jumping...")
    
class C(B):
    def suzmoq(self):
        print("C class suzmoqda...")

c1 = C()
c1.jump()
c1.move()
c1.suzmoq()