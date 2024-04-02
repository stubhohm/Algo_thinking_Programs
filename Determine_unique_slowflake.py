import random
import time
MAX_SNOWFLAKES = 100000
HASH_DIVISOR = 2
HASH_TABLE_SIZE = int(MAX_SNOWFLAKES/HASH_DIVISOR)
MIN_SNOWFLAKES = 1
MIN_ARM_SIZE = 1
MAX_ARM_SIZE = 1000
SNOWFLAKE_ARMS = 6

'''
This program impliments hashing to sort snowflakes into 'buckets' or 'bins'.
The hashing function is: ((arm length product)modulus + (sum of their arm length))modulus
Even in a list of 100,000 this keeps the bins to well below 10 items. 
The highest collision I have seen while running this program in 5-6, which is more than good enough.
'''

def compare_arms(flake_i, flake_j, i, j , chirality):
    for n in range(SNOWFLAKE_ARMS):
        x = i + (n * chirality)
        y = j + n
        if not flake_i[x%SNOWFLAKE_ARMS] == flake_j[y%SNOWFLAKE_ARMS]:
            return False
    return True

def determine_possible_chirality(flake_i, flake_j, i, j):
    chirality =  -1
    if compare_arms(flake_i, flake_j, i , j, chirality):
        return True
    chirality = 1
    if compare_arms(flake_i, flake_j, i , j, chirality):
        return True
    return False

def compare_chiral(flake_i, flake_j):
    match = False
    j = 0
    arm_j = flake_j[j]
    for i, arm_i in enumerate(flake_i):
        if arm_j == arm_i:
            match = determine_possible_chirality(flake_i, flake_j, i, j)
            break
    if match:
        return True
    else:
        return False

def compare_flakes(snow_flakes):
    for i, flake_i in enumerate(snow_flakes):
        for j in range(i + 1, len(snow_flakes)):
            flake_j = snow_flakes[j]
            if compare_chiral(flake_i, flake_j):
                print(f'flake i {flake_i}, flake j {flake_j}')
                return True
    return False

def get_sum(array):
    summation = 0
    for entry in array:
        summation += entry 
    return summation

def get_product(array, max_size):
    product = 1
    for entry in array:
        product = (product * entry) % max_size
    return product

def bin_snow_flakes(flakes, hash_size):
    bins = [[] for _ in range(hash_size)]
    for flake in flakes:
        flake_sum =  get_sum(flake)
        flake_multiple = get_product(flake, hash_size)
        flake_value = (flake_sum + flake_multiple) % hash_size
        bin = bins[flake_value]
        bin.append(flake)
        bins[flake_value] = bin
    return bins

def find_matches(hash_size):
    rand_int_min = MIN_ARM_SIZE
    rand_int_max = MAX_ARM_SIZE
    num_of_rand_flakes = MAX_SNOWFLAKES
    flakes = []
    print('Generating Snow Flakes')
    for flake in range(num_of_rand_flakes):
        random_flake = random.sample(range(rand_int_min, rand_int_max), SNOWFLAKE_ARMS)
        flakes.append(random_flake)
    print('Start Binning')
    start_time = time.time()
    bins = bin_snow_flakes(flakes, hash_size)
    match = False
    total_flakes = 0
    print('Starting Comparison')
    for flakes in bins:
        length = len(flakes)
        total_flakes += length
        if length < 2:
            continue
        if compare_flakes(flakes):
            print('A match was found')
            match = True
            break 
    if not match:
        print('No matches found')
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, total_flakes

def main():
    hash_table_size = HASH_TABLE_SIZE
    hash_divisor = HASH_DIVISOR
    time, total_flakes = find_matches(hash_table_size)
    print(f'Time to complete {time}')
    print(f'hash divisor = {hash_divisor}')
    print(f'hash size = {hash_table_size}')
    print(f'Total checked Flakes {total_flakes}')
main()