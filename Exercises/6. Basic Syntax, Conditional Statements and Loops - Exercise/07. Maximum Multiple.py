# 7.	Maximum Multiple
# Given a Divisor and a Bound, find the largest integer N, such that:
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The divisor and bound are only positive values. It's guaranteed that a divisor is found

divisor = int(input())
bound = int(input())

for i in range(bound, 0, -1):
    if i % divisor == 0:
        print(i)
        break