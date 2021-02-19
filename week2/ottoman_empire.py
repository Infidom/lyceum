num_1 = int(input("Введите 1 число\n"))

znak_1 = input("Введите знак 1\n")

num_2 = int(input("Введите 2 число\n"))

znak_2 = input("Введите знак 2\n")

num_3 = int(input("Введите 3 число\n"))

#+-*/

if znak_1 == "+" and znak_2 == "+":
    result = num_1 + num_2 + num_3
    print("Answer: " + str(result))
elif znak_1 == "+" and znak_2 == "-":
    result = num_1 + num_2 - num_3
    print("Answer: " + str(result))
elif znak_1 == "-" and znak_2 == "+":
    result = num_1 - num_2 + num_3
    print("Answer: " + str(result))
elif znak_1 == "-" and znak_2 == "-":
    result = num_1 - num_2 - num_3
    print("Answer: " + str(result))
elif znak_1 == "*" and znak_2 == "*":
    result = num_1 * num_2 * num_3
    print("Answer: " + str(result))
elif znak_1 == "*" and znak_2 == "+":
    result = num_1 * num_2 + num_3
    print("Answer: " + str(result))
elif znak_1 == "+" and znak_2 == "*":
    result = num_3 * num_2 + num_1
    print("Answer: " + str(result))
elif znak_1 == "*" and znak_2 == "-":
    result = num_1 * num_2 - num_3
    print("Answer: " + str(result))
elif znak_1 == "-" and znak_2 == "*":
    result = num_1 - num_2 * num_3
    print("Answer: " + str(result))
elif znak_1 == "/" and znak_2 == "/":
    try:
        result = num_1 / num_2 / num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
elif znak_1 == "/" and znak_2 == "+":
    try:
        result = num_1 / num_2 + num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
elif znak_1 == "/" and znak_2 == "-":
    try:
        result = num_1 / num_2 - num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
elif znak_1 == "+" and znak_2 == "/":
    try:
        result = num_1 + num_2 / num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
elif znak_1 == "/" and znak_2 == "*":
    try:
        result = num_1 / num_2 * num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
elif znak_1 == "*" and znak_2 == "/":
    try:
        result = num_1 * num_2 / num_3
        print("Answer: " + str(result))
    except ZeroDivisionError:
        print("Мы осуждаем кибербуллинг!")
else:
    print("Мы осудили кибербуллинг!")