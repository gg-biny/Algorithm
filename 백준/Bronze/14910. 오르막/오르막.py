import sys
num_list = list(map(int,sys.stdin.readline().split()))
sort_list = sorted(num_list)
if num_list == sort_list:
    print("Good")
else:
    print("Bad")