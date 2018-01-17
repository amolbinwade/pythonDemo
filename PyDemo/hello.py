name = input("What is your name?")
print("Hello {}!".format(name))
age = int(input('How old are you {}?'.format(name)))

if age >= 21:
    print("You are old enough to get married")
else:
    print("You need to wait for {} years to get married.".format(21-age))
