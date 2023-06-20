def arrayRankTransform(arr):
    sort_arr = sorted(list(set(arr)))
    hashmap = {}
    for i,element in enumerate(sort_arr):
        hashmap[element] = i+1
    return [hashmap[i] for i in arr]