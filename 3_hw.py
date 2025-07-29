def max_num(a:int,b:int):
   print(max(a,b))


def difference_135(a:int,b:int):
    if a + 135 == b or a - 135 == b:
        print("yes")
    else:
        print('no')


def month(a:int):
    if a in [1,2,12]:
        print('зима')
    elif a in [3,4,5]:
        print('весна')
    elif a in [6,7,8]:
        print('лето')
    else:
        print('осень')


def check_more10(a:int,b:int,c:int):
    if a > 10 and b > 10 and c > 10 :
        print('yes')
    else:
        print('no')


def list_positive(number_list: list[int]):
    total_positive = 0
    for i in number_list:
        if i > 0:
            total_positive += 1
    print(total_positive)


def count_days(years:int, months:int):
    print( years*12*29 + months*29)


max_num(5, 10)                       
difference_135(200, 65)          
month(4)                           
check_more10(11, 12, 13)            
list_positive([1, -2, 3, 0, 5])     
count_days(1, 2)
