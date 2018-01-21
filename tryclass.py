#This is about the BMI sys
#tryclass.py

import sys
import math


print("**********BMI************\n")
BMI = 0.0
kg = 0.0
m = 0.0

def main():
    kg = eval(input("Please input aboout your kg:\n"))
    m = eval(input("Please input your m2:"))
    m2 = pow(m,2)
    BMI = kg / m2
    print("Your Result:{}".format(BMI))
    if BMI < 18.5:
        print("偏瘦\n")
        print("国际BMI值：{} 国内BMI值：{}".format("<18.5","<18.5"))
    elif 18.5 <= BMI <= 25:
        print("正常\n")
        print("国际BMI值：{} 国内BMI值：{}".format("18.5~25","18.5~24"))
    elif 25 <= BMI <= 30:
        print("偏胖\n")
        print("国际BMI值：{} 国内BMI值：{}".format("25~30","24~28"))
    elif BMI >= 30 :
        print("肥胖\n")
        print("国际BMI值：{} 国内BMI值：{}".format(">=30",">=28"))

main()
