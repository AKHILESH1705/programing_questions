
# BMI Calculation  by using function
name1 = "akhilesh"
hight1 = 1.82
weight1 = 65

name2 = "deepak"
hight2 = 1.67
weight2 = 70

name3 = "akash"
hight3 = 1.67 
weight3 = 65


def bmi_calculator(name,hight_m, weight_kg):
    bmi=weight_kg / (hight_m**2)
    print("bmi : ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight "
    else:
        return name + " is overweight " 
result1=bmi_calculator(name1,hight1,weight1)
result2=bmi_calculator(name2,hight2,weight2)
result3=bmi_calculator(name3,hight3,weight3)

print(result1)
print(result2)
print(result3)


