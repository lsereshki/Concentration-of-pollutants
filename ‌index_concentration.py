#This program calculates the concentration of pollution from given AQI
#AQI (air quality index) is always an integer.
#numer allocated to each pollution:
#CO :1, NO2 :2, O3: 3, PM2.5 : 4 , PM10: 5, SO2: 6
####### CO (ppm) ############
number = input('what is the number of pollution?  ')
number = int(number)
if number ==1:
    index = input ('what is the index?  ')
    index = int(index)
    if 0<=index<=50:
        def concentration(index):
           return (index*4.4)/50 
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(4.9*(index-51)/49)+4.5
        value = concentration(index)
    elif 101<=index<=150:
        def concentration(index)            :
            return(2.9*(index-101)/49)+9.5
        value = concentration(index) 
    elif 151<=index<=200:
        def concentration(index)            :
            return(2.9*(index-151)/49)+12.5
        value = concentration(index)      
    elif 201<=index<=300:
        def concentration(index)            :
            return(14.9*(index-201)/99)+15.5   
        value = concentration(index)
    elif 301<=index<=400:
        def concentration(index)            :
            return(9.9*(index-301)/99)+30.5
        value = concentration(index)   
    elif 401<=index<=500:
        def concentration(index)            :
            return(9.9*(index-401)/99)+40.5
        value = concentration(index)
################# NO2 (ppm) ######################
elif number ==2:
    index = input ('what is the index?  ')
    index = int(index)
    if 0<=index<=50:
        def concentration(index)            :
            return(0.053*index)/50   
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(0.046*(index-51)/49)+0.054   
        value = concentration(index)
    elif 101<=index<=150:
        def concentration(index)            :
            return(0.259*(index-101)/49)+0.101 
        value = concentration(index)
    elif 151<=index<=200:
        def concentration(index)            :
            return(0.288*(index-151)/49)+0.361   
        value = concentration(index)
    elif 201<=index<=300:
        def concentration(index)            :
            return(0.59*(index-201)/99)+0.65   
        value = concentration(index)
    elif 301<=index<=400:
        def concentration(index)            :
            return(0.39*(index-301)/99)+1.25   
        value = concentration(index)
    elif 401<=index<=500:
        def concentration(index)            :
            return(0.39*(index-401)/99)+1.65    
        value = concentration(index)
###########  O3 (ppm) #######################
#For 0<=index<=100 just eight hour average ozone concentration is defined and for 301<=index<=500 just hourly concentration is defined.
#For 100<index<=300, the hourly concentration and eight hours concentration have different value.
elif number ==3:
    index = input ('what is the index?  ')
    index = int(index)
    hournumber = input ('which ozone do u want? 1 or 8 hours: ')
    hournumber = int(hournumber) 
    if 0<=index<=50:
        def concentration(index):
           return (index*0.059)/50 
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(0.015*(index-51)/49)+0.06
        value = concentration(index)
    elif 101<=index<=150:
        if hournumber==8:
            def concentration(index)            :
                return(0.014*(index-101)/49)+0.071
            value = concentration(index)
        elif hournumber ==1:
            def concentration(index)            :
                return(0.039*(index-101)/49)+0.125     
            value = concentration(index)
    elif 151<=index<=200:
        if hournumber==8:
            def concentration(index)            :
                return(0.019*(index-101)/49)+0.086
            value = concentration(index)
        elif hournumber ==1:
            def concentration(index)            :
                return(0.039*(index-101)/49)+0.165     
            value = concentration(index)
    elif 201<=index<=300:
        if hournumber==8:
            def concentration(index)            :
                return(0.094*(index-101)/99)+0.106
            value = concentration(index)
        elif hournumber ==1:
            def concentration(index)            :
                return(0.199*(index-101)/99)+0.205  
            value = concentration(index)
    elif 301<=index<=500:
            def concentration(index)            :
                return(0.199*(index-301)/199)+0.405  
            value = concentration(index) 
########## PM2.5 (micrograms/m3) ###############################
elif number ==4:
    index = input ('what is the index?  ')
    index = int(index)
    if 0<=index<=50:
        def concentration(index):
           return (index*15.4)/50
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(24.9*(index-51)/49)+15.5
        value = concentration(index)
    elif 101<=index<=150:
        def concentration(index)            :
            return(24.9*(index-101)/49)+40.5 
        value = concentration(index)
    elif 151<=index<=200:
        def concentration(index)            :
            return(84.9*(index-151)/49)+65.5  
        value = concentration(index)
    elif 201<=index<=300:
        def concentration(index)            :
            return(99.9*(index-201)/99)+150.5   
        value = concentration(index)
    elif 301<=index<=400:
        def concentration(index)            :
            return(99.9*(index-301)/99)+250.5   
        value = concentration(index)
    elif 401<=index<=500:
        def concentration(index)            :
            return(149.9*(index-401)/99)+350.5  
        value = concentration(index)
#############   PM10 (micrograms/m3) ############################
elif number ==5:
    index = input ('what is the index?  ')
    index = int(index)
    if 0<=index<=50:
        def concentration(index):
           return (index*54)/50 
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(99*(index-51)/49)+55
        value = concentration(index)
    elif 101<=index<=150:
        def concentration(index)            :
            return(99*(index-101)/49)+155 
        value = concentration(index)
    elif 151<=index<=200:
        def concentration(index)            :
            return(99*(index-151)/49)+255  
        value = concentration(index)
    elif 201<=index<=300:
        def concentration(index)            :
            return(69*(index-201)/99)+355   
        value = concentration(index)
    elif 301<=index<=400:
        def concentration(index)            :
            return(79*(index-301)/99)+425   
        value = concentration(index)
    elif 401<=index<=500:
        def concentration(index)            :
            return(index-401)+505 
        value = concentration(index)
############  SO2 (ppm) ############################
#For SO2 index<201 implies hourly concentration & index>=201 means 24 hours concentration
elif number ==6:
    index = input ('what is the index?  ')
    index = int(index)
    if 0<=index<=50:
        def concentration(index):
           return (index*0.034)/50 
        value = concentration(index)
    elif 51<=index<=100:
        def concentration(index)            :
            return(0.109*(index-51)/49)+0.035
        value = concentration(index)
    elif 101<=index<=150:
        def concentration(index)            :
            return(0.079*(index-101)/49)+0.145 
        value = concentration(index)
    elif 151<=index<=200:
        def concentration(index)            :
            return(0.079*(index-151)/49)+0.0225  
        value = concentration(index)
    elif 201<=index<=300:
        def concentration(index)            :
            return(0.299*(index-201)/99)+0.305   
        value = concentration(index)
    elif 301<=index<=400:
        def concentration(index)            :
            return(0.199*(index-301)/99)+0.605   
        value = concentration(index)
    elif 401<=index<=500:
        def concentration(index)            :
            return(0.199*(index-401)/99)+0.805
        value = concentration(index)                                                        
print('concentration = ',value)
       

