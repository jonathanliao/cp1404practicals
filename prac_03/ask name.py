def main():
    name = get_name()
    for i in range(1, len(name), 2):
        print(name[i])


def get_name():
    name = input("please enter your name : ")
    while len(name) == 0:
        print("name cant be blank.")
        name = input("please enter your name : ")
    return name


main()