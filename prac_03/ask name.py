def main():
    name = get_name()
    frequency = int(input("please enter the frequency : "))
    print_name(name, frequency)


def print_name(name, step=2):
    for i in range(0, len(name), step):
        print(name[i])


def get_name():
    name = input("please enter your name : ")
    while len(name) == 0:
        print("name cant be blank.")
        name = input("please enter your name : ")
    return name


main()
