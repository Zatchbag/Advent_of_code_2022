import math

# # dictionary concatination

# exdict = {'monkey0' : 'It Works!'}

# def monkey(count):
#     print(exdict['monkey'+str(count)])

# monkey(0)

# --------------------------------------------------------------------------------------------------
# # Recursions

# def recusive_round(input, times, time_count = 0):
#     # Assuming for simplicity that "input" is just a number
#     # and that the function adds 2 * the current count to it.
#     input += 2 * time_count
#     if time_count >= times:
#         return input
#     else:
#         return recusive_round(input, times, time_count + 1)

# --------------------------------------------------------------------------------------------------
# # Operator in functions

# def processor_1(number):
#     return int(number * 7 // 3)

# def processor_2(number):
#     return int(number + 20 // 3)



# things_to_process = {
#     "1": {
#         "things" : [1,2,3,4,5],
#         "processor": processor_1
#     },
#     "2": {
#         "things": [1,3,4,6],
#         "processor": processor_2
#     }
# }


# def process_a_thing(thing_to_process, processor):
#     # say the thing to process is a list of numbers
#     # and the processor is the function that does processing of each number
#     processed_numbers = [processor(num) for num in thing_to_process]
#     return processed_numbers

# def process_all_the_things(those_things):
#     for key, value in those_things.items():
#         those_things[key]["things"] = process_a_thing(value["things"], value["processor"])

# process_all_the_things(things_to_process)


# --------------------------------------------------------------------------------------------------
# Math tests

# Prime numbers
# 1,2,3,5,7,11,13,17,19,23,29...

# Seemingly random numbers in challenge
# 50, 70, 89, 75, 66, 66, 66, 51, 71, 76, 58, 55, 58, 60, 79, 52, 55, 51, 85, 79, 52, 55, 51, 69, 92, 71, 76, 73, 98, 67, 79, 99, 82, 76, 69, 69, 57, 65, 79, 86, 79, 98, 54, 65, 75, 74, 79, 60, 97, 74

# Observations...
# Modulo output will always be < the divisor 
# square root of an int is the maximum divisor
# reduction in length of number is the name of the game, numbers quickly get too long
# need to reduce numbers in a way that still results in remainder 0
    # Chinese remainder theorem

primes = [2,3,5,7,11,13,17,19,23,29]
challengenumbers = [50, 70, 89, 75, 66, 66, 66, 51, 71, 76, 58, 55, 58, 60, 79, 52, 55, 51, 85, 79, 52, 55, 51, 69, 92, 71, 76, 73, 98, 67, 79, 99, 82, 76, 69, 69, 57, 65, 79, 86, 79, 98, 54, 65, 75, 74, 79, 60, 97, 74]
# 50
challengeuniquenumbers = [50, 51, 52, 54, 55, 57, 58, 60, 65, 66, 67, 69, 70, 71, 73, 74, 75, 76, 79, 82, 85, 86, 89, 92, 97, 98, 99]
# 27
# Only slightly more than half of the numbers used in the challenge being unique feels overly coincidental too...

from random import randint

random_int = randint(0, 1000000000000)


# Chinese remainder theorem
# Every pair of congruence relations for an unknown integer x, of the form x ≡ k (mod a) and x ≡ m (mod b), has a solution (Chinese remainder theorem); 
# in fact the solutions are described by a single congruence relation modulo ab.

# n % 3 = 2
# n % 5 = 3
# n % 7 = 2
# n % (3 * 5 * 7) = 23

# Any number shares congruence with any other set of numbers created by the subtraction of 
# any third number modulo factors of the number subtracted
# 219 - 60 = 159 - 60 = 99 - 60 = 39
# inital number = 219
# random int = 60
# number set = 219, 159, 99, 39

# 60 factorization is 3 * 4 * 5
# 219 % 3 = 0, 219 % 4 = 3, 219 % 5 = 4 
# 159 % 3 = 0, 159 % 4 = 3, 159 % 5 = 4
# 99 % 3 = 0, 99 % 4 = 3, 99 % 5 = 4
# 39 % 3 = 0, 39 % 4 = 3, 39 % 5 = 4
# therefore, 39 = lowest congruent number to larger sample, 219


# Test2
# random number = 274838601874
# second random number = 79759438021
# number set = 274838601874, 195079163853, 115319725832, 35560287811
# 79759438021 factors = 19, 29, 53, 2731207
# 274838601874 % 19 = 6, 274838601874 % 29 = 2, 274838601874 % 53 = 33, 274838601874 % 2731207 = 2703878
# 195079163853 % 19 = 6, 195079163853 % 29 = 2, 195079163853 % 53 = 33, 195079163853 % 2731207 = 2703878
# ...

def primeFactors(n): 
    while n % 2 == 0: 
        print(2) 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i == 0: 
            print(i)
            n = n / i 
    if n > 2: 
        print(n)


print(26 % 13)
print((676*676)%13)


