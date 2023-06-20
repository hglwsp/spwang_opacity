def reconstructQueue(people):
    # 渔（套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，
    # 根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。


    res = []
    people.sort(key = lambda x:(-x[0],x[1]))
    # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    for item in people:
        res.insert(item[1], item)
    return res
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
