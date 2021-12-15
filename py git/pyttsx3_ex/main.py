import pyttsx3
speaker = pyttsx3.init()
while True:
    num1 = int (input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))

    select = input(" Choose one  Add(+) Sub(-) Multiply(*) Division(/)")
    if select == "+":
        ans = num1+num2
    elif select == "-":
        ans = num1-num2
    elif select == "*":
        ans = num1*num2
    elif select == '/':
        ans = num1/num2
    else:
        print("Select within the given operations")
        continue

    print("The addition of two values is : ", ans)
    speaker.say("The solution is")
    speaker.say(ans)

    speaker.runAndWait()