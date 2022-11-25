'''
Input : 고유번호 5개 (띄어쓰기로 구분)
Output : 검증수 (각 고유번호의 제곱의 합을 10으로 나눈 나머지)
'''
A, B, C, D, E = map(int,input().split())
sum = A**2 + B**2 + C**2 + D**2 + E**2
result = sum%10

print(result)