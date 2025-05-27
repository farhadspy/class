class Fraction:
    
   def __init__(self,ss,mm):
       self.face = ss
       self.denominator = mm 
   
   def Multi(self,f2):
       result_s = self.face * f2.face
       result_d = self.denominator * f2.denominator
       
       x = Fraction(result_s,result_d)
       return x
       
   def Div(self,f2):
       result_s = self.face * f2.denominator
       result_d = self.denominator * f2.face
       
       x = Fraction(result_s,result_d)
       return x
       
   def sum(self,f2):
       result_s = (self.face * f2.denominator) + (f2.face * self.denominator)
       result_d = self.denominator * f2.denominator
       
       x = Fraction(result_s,result_d)
       return x
       
   def minus(self,f2):
       result_s = (self.face * f2.denominator) - (f2.face * self.denominator)
       result_d = self.denominator * f2.denominator
       
       x = Fraction(result_s,result_d)
       return x   
       
   def fraction_to_number(self,b,d):
       ...    
       
   def show(self):
       print(self.face, "/" , self.denominator)
   
   
print("a/b * c/d")
print("a/b / c/d") 
print("a/b + c/d")
print("a/b - c/d")    
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))
d = int(input("enter number 4: "))

aa = Fraction(a,b)
aa.show()

bb = Fraction(c,d)
bb.show()

print("if you want Multiplication:")
show_Multiplication = aa.Multi(bb)
show_Multiplication.show()

print("if you want Division:")
answer_Division = aa.Div(bb)
answer_Division.show()

print("if you want sum:")
answer_sum = aa.sum(bb)
answer_sum.show()

print("if you want minus:")
answer_min = aa.minus(bb)
answer_min.show()
                       
                                                                                               