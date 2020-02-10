

def isPrime(num):
    if num == 0 or num == 1:
        return "Not prime"
    if num % 2 == 0:
        return "Come on dude, you know even numbers are not prime!"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"


def isFactorial(number):
    factorial = 1
    for i in range(1, int(number) + 1):
        factorial *= i
    return factorial


def isPalindrome(number):
    reversedNum = 0
    tempNumber = int(number)
    while tempNumber > 0:
        reversedNum = int(reversedNum * 10)
        reversedNum = int(reversedNum + (tempNumber % 10))
        tempNumber = int(tempNumber / 10)
    return reversedNum == number


def hasSqrtRoot(number):
    flag = False
    for i in range(2, int(number / 2) + 1):
        if int(i * i) == number:
            flag = True
            break
    return "True" if flag else "False"