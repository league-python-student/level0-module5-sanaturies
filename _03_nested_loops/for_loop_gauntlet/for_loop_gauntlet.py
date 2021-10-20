"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    def count():
        for i in range(101):
            print(i)
    def count1():
        for i in range(100,0,-1):
            print(i)
    def count2():
        for i in range(2,101,2):
            print(i)
    def count3():
        for i in range(501):
            if i%2==0:
                print(i,"even")
            else:
                print(i,'odd') 
    def divisible():
        for i in range(778):
            if i%7==0:
                print(i)      
    def age():
        birth=2008
        from datetime import date
        todays_date=date.today()
        today=todays_date.year  
        for i in range(birth,today+1):
            print(i,'i was',i-birth,'years old')
    
    def combination():
        for i in range(3):
            for j in range(3):
                print(i,j)
    def square():
        string=''
        for i in range(1,10):
            i=str(i)
            if i=='4' or i=='7':
                string+="\n"
            string+=' '+i
        print(string)

    def triangle():
        for i in range(6):
            o='*'
            print(o*i)
    def countdown():
        for i in range(1,101):
            print(100-i)
    
    countdown()
    
