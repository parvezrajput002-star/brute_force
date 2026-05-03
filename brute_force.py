def four_combination (Number_for_zfill):
    Combination = []
    for i in range (10000):
        combination = str(i).zfill(4)
        Combination.append(combination)
        
    return Combination

def six_combination (Number_for_zfill):
    Combination = []
    for i in range (1000000):
        combination = str(i).zfill(6)
        Combination.append(combination)
    return Combination
        
Number_for_zfill = int(input("Enter number :"))
if Number_for_zfill == 4:
    Four_combination = four_combination(Number_for_zfill)
    Result_1 = Four_combination
    with open("combination.txt","w") as f:
        for item in Result_1 :
            f.write(item+"\r")
        print("your file is ready !")
    
elif Number_for_zfill == 6:
    Six_combination = six_combination(Number_for_zfill)
    Result_2 = Six_combination
    with open("combination.txt","w") as f:
        for item in Result_2 :
            f.write(item+"\r")
        print("your file is ready !")
else:
    print("have default !")
    
