def finalValueAfterOperations(operations):
    x = 0
    for op in operations:
        if op == "X--" or op == "--X":
            x-=1
        else:
            x+=1
    return x

test = ["--X","X++","X++"]
print(finalValueAfterOperations(test))