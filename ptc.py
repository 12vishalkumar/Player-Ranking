import math
import os
import random
import re
import sys

# Complete the 'climbingLeaderboard' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked.sort()
    ranked = list(reversed(ranked))
    s_rank = []
    for i in player:
        while(ranked and i >= ranked[-1]):
            ranked.pop()
        s_rank.append(len(ranked)+1)
    return s_rank
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()