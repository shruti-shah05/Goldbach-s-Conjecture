# CSC 430 : Python Programming
# Assignment 0301 : Goldbach's Conjecture
# Name : Shruti Shah
# Date : 10/04/2020


def listPrimeNumbers(highestNum):
    '''
    This function lists all the prime numbers less than one hundred.

    '''
    listForPrimeNums = []               #initializing list for prime numbers
    for num in range(2, highestNum):
        for i in range(2, num):         #iterating from 2
            if (num % i) == 0:          #if the num is divisible, then it will break
                break
        else:  
            listForPrimeNums.append(num)        #adding number to the list

    return listForPrimeNums            #returing the list


def CompareNumToPrimeNums(num, listOfPrimeNumbers):
    '''
    The function compares the subtracted number with prime number, it checks if the subtracted value exists in the list that contains prime numbers upto 100 
    '''

    if(num == 0 or len(listOfPrimeNumbers) == 0):       #Error checking
        return
    for primeNumber in listOfPrimeNumbers:              
        if(num == primeNumber):                         #if the number is in list of prime numbers
            return primeNumber                          #returns prime number
    return 0


def subtractPrimeNumToNum(evenNum, primeNumber):
    '''
    This function does the calcultation to get two primes that can sum to the integer
    '''
    if(evenNum == 0 or primeNumber == 0):       #Error checking if even number equals to 0 or prime number equals to 0
         return
    num = evenNum - primeNumber                 #if not, then it will subtract the prime number from even number and store it in a variable call num.
    return num                                  #returns num
         

def printResult(evenNum, primeNumber, num2):
    '''
    This function prints out a single line showing how two primes can sum to the integer
    '''
    print(str(evenNum) + " = " + str(primeNumber) + " + " + str(num2))


#master function calls other functions
def main():
    highestNum = 100
    startingNum = 4

    listOfPrimeNumbers = listPrimeNumbers(highestNum+1)             #calling the listPrimeNumbers() and storing it in a new variable called listOfPrimeNumbers
    for evenNum in range(startingNum, highestNum+1, 2):             #iterates over the even numbers up until 100
        for primeNumber in listOfPrimeNumbers:                      #iterates over all the prime numbers up to 100
            num = subtractPrimeNumToNum(evenNum, primeNumber)       #calls the subtractPrimeNumToNum() which subtracts the prime number from even number and stores it in num
            num1 = CompareNumToPrimeNums(num, listOfPrimeNumbers)   # compares the subtracted num with prime number, checks if the subtracted value exists in the list that contains prime numbers upto 100 and stores it in num1
            if(num1 != 0):
                printResult(evenNum, primeNumber, num1)             #print result 
                break

main()