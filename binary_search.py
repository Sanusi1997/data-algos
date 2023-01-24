

def binarySearch(input_array, target_value):
    min = 0
    max = len(input_array) - 1
    guess = 0
    while(min <= max):
        guess = (max + min) // 2
        if(input_array[guess] == target_value):
            print("You found the target at position {}". format(guess))
            break
        elif(input_array[guess] < target_value):
            min = guess + 1
        else:
            max = guess - 1
    return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];    

binarySearch(primes, 3)


