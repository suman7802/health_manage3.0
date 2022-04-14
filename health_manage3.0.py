def suman(k):
    if k == 1:
        print("hello suman you select edit file mode by pressing", k)
        input2 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input2 == 1:
            print("currently you are in exercise section")
            try:
                old = open("suman_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_exercise.txt", "w") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")
        else:
            print("currently you are in diet section")
            try:
                old = open("suman_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_diet.txt", "w") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

    else:
        print("hello suman you select add content file mode by pressing", k)
        input3 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input3 == 1:
            print("currently you are in exercise section")
            try:
                old = open("suman_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_exercise.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

        else:
            print("currently you are in diet section")
            try:
                old = open("suman_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_diet.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")


def sahina(k):
    if k == 1:
        print("hello sahina you select edit file mode by pressing", k)
        input2 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input2 == 1:
            print("currently you are in exercise section")
            try:
                old = open("sahina_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("sahina_exercise.txt", "w") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")
        else:
            print("currently you are in diet section")
            try:
                old = open("sahina_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("sahina_diet.txt", "w") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

    else:
        print("hello suman you select add content file mode by pressing", k)
        input3 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input3 == 1:
            print("currently you are in exercise section")
            try:
                old = open("suman_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_exercise.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

        else:
            print("currently you are in diet section")
            try:
                old = open("suman_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("suman_diet.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")


def sumahi(k):
    if k == 1:
        print("hello sumahi you select edit file mode by pressing", k)
        input2 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input2 == 1:
            print("currently you are in exercise section")
            try:
                old = open("sumahi_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
                with open("sumahi_exercise.txt", "w") as exe:
                    text = str(input())
                    exe.write(text)
                    print("your file is successfully saved")
        else:
            print("currently you are in diet section")
            try:
                old = open("sumahi_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("sumahi_diet.txt", "w") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

    else:
        print("hello suman you select add content file mode by pressing", k)
        input3 = int(input("press 1 for exercise\npress 2 for diet\n"))
        if input3 == 1:
            print("currently you are in exercise section")
            try:
                old = open("sumahi_exercise.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("sumahi_exercise.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")

        else:
            print("currently you are in diet section")
            try:
                old = open("sumahi_diet.txt", "r")
                print(old.readlines())
                old.close()
            except Exception as e:
                print(e)
            with open("sumahi_diet.txt", "a") as exe:
                text = str(input())
                exe.write(text)
                print("your file is successfully saved")


print("welcome in fitness app")
while True:
    input001 = int(input("press 1 for start/continue and 0 for back/exit\n"))
    if input001 == 0:
        print("GOOD BYE")
        break
    print("select your profile")
    input1 = int(input("press 1 for suman\npress 2 for sahina\npress 3 for sumahi\n"))
    if input1 == 1:
        print("current profile: suman")
        d = int(input("Press 1 for edit\npress 2 for add content\n"))
        suman(d)
    elif input1 == 2:
        print("current profile: sahina")
        d = int(input("Press 1 for edit\npress 2 for add content\n"))
        sahina(d)
    else:
        print("current profile: sumahi")
        d = int(input("Press 1 for edit\npress 2 for add content\n"))
        sumahi(d)
