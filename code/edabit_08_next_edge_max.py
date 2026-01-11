# 삼각형의 성립 조건
# |AB| < |BC| + |CA|
# 가장 긴 변  < 다른 두 변의 합 
# 최댓값 = side1  + side2 -1 


def next_edge(side1, side2):
    return side1 + side2 - 1

print(next_edge(3,5))