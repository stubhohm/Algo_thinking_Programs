import time
'''
This program is for optimization. 
The goal is to take three inputs, each numbers. Find the maximum number of times the first two numbers could go into the last number favoring the smallest remainder.
'''
SIZE = 100000


def solve_t(m, n, t, memo):
    if memo[t] != -2:
        return memo[t]
    if t == 0:
        memo[t] = 0
        return memo[t]
    print(f't {t}, m {m}, n {n}')
    if t >= m:
        first = solve_t(m, n, t-m, memo)
    else:
        first = -1
    if t >= n:
        second = solve_t(m, n, t-n, memo)
    else:
        second = -1
    print(f'first{first}, second {second}, t {t}')
    if first == -1 and second == -1:
        memo[t] = -1
        return memo[t]
    else: 
        max_value = max(first, second) + 1
        memo[t] = max_value
        print(f'Max value: {max_value} at {t} minutes')
        return memo[t]
    

def solve_recursive(m, n, t):
    memo = [-2]*SIZE
    result = solve_t(m, n, t, memo)
    print(f'rec memo {memo[:t]}')
    if result >= 0:
        print(f'rec {result} burgers eaten with no time drinking beer.')
    else:
        i = 1
        t = t - i
        result = solve_t(m, n, i, memo)
        
        while result < 0:
            result = solve_t(m, n, i, memo)
            i += 1
        print(f'rec {result} burgers eaten with {i - 1} minutes drinking beer')


def solve_dynamic_programing(m, n ,t):
    dp = [-2]*SIZE
    dp[0] = 0
    for minutes in range(1, t):
        if minutes >= m:
            first = dp[minutes - m]
        else:
            first = -1
        if minutes >=n:
            second = dp[minutes - n]
        else:
            second = -1
        if first == -1 and second == -1:
            dp[minutes] = -1
        else:
            maximum = max(first, second) + 1
            dp[minutes] = maximum
    
    result = dp[t]
    print(result)
    if result >=0:
        print(f'dp {result} burgers eaten with no time drinking beer.')
    else:
        i = 1
        while result < 0:
            result = dp[t-i]
            i +=1
        print(f'dp {result} burgers eaten with {i - 1} minutes drinking beer')
    
def main():
    m = 3
    n = 13
    t = 50
    solve_recursive(m, n, t)
    solve_dynamic_programing(m, n, t)

main()