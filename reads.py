def collatz (number):

    if number % 2==0:
        print(number//2)
        return  (number//2)
    else:
        print((3*number)+1)
        return (3*number)+1
try:
    people = int(input())
    while people!=1:
        people =collatz(people)
except ValueError:
    print("Please enter a valid INTEGER.")

