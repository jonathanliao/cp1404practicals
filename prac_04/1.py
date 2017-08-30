def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number : ")))

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[4]))
    print("The last number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the number is {}".format(sum(numbers)/5))
    #print(numbers)




main()
