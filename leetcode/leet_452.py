def findMinArrowShots(points):
    if len(points) == 0:
        return 0
    points.sort(key=lambda x: x[0])    # sort according to x[0]
    res = 1          # result
    for i in range(1,len(points)):
        if points[i-1][1] < points[i][0]:
            res+=1
        else:
            points[i][1] = min(points[i][1],points[i-1][1])
    return res

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))


