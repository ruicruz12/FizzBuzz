


""" ***************** FizzBuzz version 1 ***************** """

class FizzBuzzV1:
    def __init__(self,number):
        self.number=number
    
    def fizz(self):
        return self.number % 3 == 0 
     
    def fizzy(self):
        return str(self.number).find('3') >= 0
    
    def buzz(self):
        return self.number % 5 == 0 
    
    def buzzy(self):
        return str(self.number).find('5') >= 0
        
    def fizzbuzz(self):
        return self.fizz() and self.buzz()
            
    def lucky(self):
        return (self.fizz() or self.fizzy()) and (self.buzz() or self.buzzy()) and self.fizzbuzz()
           
    def fizz_fizz(self):
        return self.fizz() and self.fizzy()
        
    def buzz_buzz(self):
        return self.buzz() and self.buzzy()
    
    
    
def get_fizzbuzz(number):
    fizz_buzz = []
    
    for i in range(1,number):
        fb_class = FizzBuzzV1(i)
        if fb_class.lucky():
            fizz_buzz.append('lucky')
            
        elif fb_class.fizz_fizz():
            fizz_buzz.append('fizz fizz')
            
        elif fb_class.buzz_buzz():
            fizz_buzz.append('buzz buzz')
            
        elif fb_class.fizzbuzz():
            fizz_buzz.append('fizzbuzz')
            
        elif fb_class.fizz() or fb_class.fizzy():
            fizz_buzz.append('fizz')
            
        elif fb_class.buzz() or fb_class.buzzy():
            fizz_buzz.append('buzz')
            
        else:
            fizz_buzz.append(i)
            
    
    return fizz_buzz


print('Version 1: ',get_fizzbuzz(21))


""" ***************** FizzBuzz version 2 ***************** """

class FizzBuzzV2:
    def __init__(self,number):
        self.number = number
        
    def fizz_buzz(self):
        fizzbuzz_list = []
        
        for i in range(1,self.number):
            
            if (i % 3 == 0 or str(i).find('3') >= 0) and \
                (i % 5 == 0 or str(i).find('5') >= 0) and \
                    (i % 3 == 0 and i % 5 == 0):
                        
                        fizzbuzz_list.append('lucky')
        
            elif i % 3 == 0 and str(i).find('3') >= 0:
                fizzbuzz_list.append('fizz fizz')
        
            elif i % 5 == 0 and str(i).find('5') >= 0:
                fizzbuzz_list.append('buzz buzz')
        
            elif i % 3 == 0 and i % 5 == 0:
                fizzbuzz_list.append('fizzbuzz')
        
            elif i % 3 == 0 or str(i).find('3') >= 0:
                fizzbuzz_list.append('fizz')
        
            elif i % 5 == 0 or str(i).find('5') >= 0:
                fizzbuzz_list.append('buzz')
        
            else:
                fizzbuzz_list.append(i)
                
        
        return fizzbuzz_list


print('Version 2: ',FizzBuzzV2(21).fizz_buzz())
    
    
    
    
    
    
    
    
