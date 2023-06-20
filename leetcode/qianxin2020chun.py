# 1
# def AttendMeetings(times):
#     n = len(times)
#     times.sort(key=lambda x: (x[0],-x[1]))
#     count,end = 0,0
#     for i in range(0,n):
#         if end <= times[i][0]:
#             count+=1
#             end = times[i][1]
#     return count
#
# count = [[8,9],[9,10],[9,12],[14,16],[15,16]]
# print(AttendMeetings(count))

# 2

x = int(input().strip())
m = int(input().strip())
numsum = list(map(int, input().strip().split()))
curprice = list(map(int, input().strip().split()))
nxtprice = list(map(int, input().strip().split()))
pricemake = []
for i in range(m):
    pricemake.append(nxtprice[i]-pricemake[i])
dp = [[0]*(x+1) for _ in range(numsum+1)]
for j in range(1,numsum+1):
    if numsum[j] > x:


