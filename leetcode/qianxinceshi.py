import math

def GetAvgArr(number_list, arr_num):
    avg_arrays = []
    if len(number_list) == 0 or len(number_list) < arr_num:
        return avg_arrays
    sum_value = 0
    mean_value = 0
    number_list_float = []
    for num in number_list:
        number_list_float.append(float(num))
        sum_value += float(num)
    mean_value = sum_value / float(arr_num)
    number_list_float.sort(reverse=True)
    for cnt in range(0, arr_num):
        arr = []
        if cnt == arr_num - 1:
            avg_arrays.append(transFloatToIntList(number_list_float))
            break
        if len(number_list_float) > 0 and number_list_float[0] >= mean_value:
            arr = [number_list_float[0]]
            avg_arrays.append(transFloatToIntList(arr))
            sum_value = sum_value - number_list_float[0]
            mean_value = sum_value / float(arr_num - len(avg_arrays))
        else:
            arr, _ = getList(number_list_float, mean_value, math.pow(mean_value, 2))
            avg_arrays.append(transFloatToIntList(arr))
        number_list_float = removeFromFloatList(number_list_float, arr)

    return avg_arrays
def transFloatToIntList(float_list):
    res = []
    for item in float_list:
        res.append(int(item))

    return res
def removeFromFloatList(original_list, remove_nums):
    res = []
    start = 0
    for remove in remove_nums:
        for i in range(start, len(original_list)):
            if original_list[i] == remove:
                res.extend(original_list[start:i])
                start = i + 1
                break

    res.extend(original_list[start:])
    return res
def getList(arr, delta, distance):
    res = []
    if len(arr) == 0:
        return res, -1
    for i in range(0, len(arr) - 1):
        if delta == arr[i]:
            res.append(arr[i])
            return res, 0
        elif delta < arr[i]:
            continue
        elif delta > arr[i]:
            if i == 0:
                res.append(arr[i])
                delta = delta - arr[i]
                distance = math.pow(delta, 2)
                tmp, d = getList(arr[i + 1:], delta, distance)
                res.extend(tmp)
                return res, d
            else:
                dis1 = math.pow(arr[i - 1] - delta, 2)
                dis2 = math.pow(delta - arr[i], 2)
                if dis1 > dis2:
                    res.append(arr[i])
                    delta = delta - arr[i]
                    tmp, d = getList(arr[i + 1:], delta, dis2)
                    res.extend(tmp)
                    return res, d
                else:
                    tmp, d = getList(arr[i:], delta, dis2)
                    if dis1 > d:
                        res.extend(tmp)
                        return res, d
                    res.append(arr[i - 1])
                    return res, dis1
    dis = math.pow(delta - arr[len(arr) - 1], 2)
    if dis < distance:
        return arr[len(arr) - 1:], dis
    return [], -1
partition_list = [1,2,3,6,5,4,7,8,9]
arrays = GetAvgArr(partition_list, 4)
print(arrays)
