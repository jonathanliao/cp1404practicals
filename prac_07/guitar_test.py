from prac_07.Guitar import Guitar

def main():
    guitar1 = Guitar( "Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("another", 2012)
    print(guitar1)
    print('age of {} is {}'.format(guitar1.name, Guitar.get_age(guitar1)))
    print('{} is_vintage() = {}'.format(guitar1.name, Guitar.is_vintage(guitar1)))
    print(guitar2)
    print('age of {} is {}'.format(guitar2.name, Guitar.get_age(guitar2)))
    print('{} is_vintage() = {}'.format(guitar2.name, Guitar.is_vintage(guitar2)))



main()