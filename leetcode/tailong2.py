def split(value, n):
    value.sort(reverse=True)
    group = []
    s = sum(value)
    for i in range(len(value)+1):
        if i == len(value)+1:
            return group
        else:
            temp = 0
            if group == []:
                group.append([value[i]])
            else:
                temp = 0
                for i in range(len(group)):
                    temp+=sum(group[i])
                avg = s - temp/l




value = [100, 10, 23, 23, 12, 34, 67, 135, 5, 39, 60, 204]
# groups = {'a':100, 'b':10, 'c':23, 'd':23, 'e':12, 'f':34, 'g':67, 'h':135, 'i':5, 'j':39, 'k':60, 'l':204}
n = 4
print(split(groups,n))
