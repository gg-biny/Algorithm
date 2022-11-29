'''
Input : A, I
A = 앨범에 수록된 곡의 개수
I = 평균값 (앨범 속 저작권 있는 멜로디 개수/ A 를 올림한 것)
Output : 저작권 있는 멜로디의 최소값
'''

A, I = map(int,input().split())
print(A*(I-1)+1)