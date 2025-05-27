class Time:
    def __init__(self , hh , mm , ss):
        self.hour = hh 
        self.minute = mm
        self.second = ss
        self.fix()
    
    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1 
            
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            
        if self.second < 0:
            self.second += 60
            self.minute -= 1 
            
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1
        
        if self.hour > 24:
            self.hour -= 24
            
        if self.hour < 1:
            self.hour += 24
        
    def sum(self,t2):
        new_h = self.hour + t2.hour   
        new_m = self.minute + t2.minute  
        new_s = self.second + t2.second
           
        result = Time(new_h,new_m,new_s)
        return result
    
    def min(self,t2):
        new_h = self.hour - t2.hour   
        new_m = self.minute - t2.minute  
        new_s = self.second - t2.second
          
        result = Time(new_h,new_m,new_s)
        return result
    
    def gmt_to_tehran(self):
        tehran_sum = self.sum(Time(3 , 30 , 0))
        return tehran_sum
        
    def time_to_second(self):
        seconds = self.hour * 3600 + self.minute * 60 + self.second
        return seconds
    
    @staticmethod
    def second_to_time(seconds):
        hour = seconds // 3600
        seconds = seconds - (hour * 3600)
        minute =  seconds // 60
        second = seconds - (minute * 60)
        t = Time(hour , minute , second)
        return t
    
    def show(self):
        print(self.hour , ":" , self.minute , ":" , self.second)



t1 = Time(3 , 75 , 17)
t1.show()

t2 = Time(4 , 50 , 2)
t2.show()
    
t3 = t1.sum(t2)    
t3.show()

t4 = t1.min(t2)    
t4.show()

t5 = t3.gmt_to_tehran()
t5.show() 

t6 = t5.time_to_second()
print(t6)

t7 = Time.second_to_time(4000)
t7.show()