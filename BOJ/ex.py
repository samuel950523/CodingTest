'''
안녕하세요.
제 코드를 봐주셔서 감사합니다.
부족한 점들은 양해 부탁드립니다.
'''

import sys
input = sys.stdin.readline

N = int(input())
if N%4 == 0:
    print("Even")
elif N%2 == 0:
    print("Odd")
else:
    print("Either")