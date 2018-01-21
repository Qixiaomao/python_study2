number = 23
guess = int(input("Enter an integer:"))

if guess == number:
    #新块从这里开始
    print("Congratulations,you guessed it.")
    print("but you do not win any prizes!")

elif guess < number:
    #另一块代码块
    print("No,it is a little higher than that.")

else:
    print("No,it is a little lower than that.")

print("Done")

#这最后一句语句将在
#if语句执行完毕后执行
