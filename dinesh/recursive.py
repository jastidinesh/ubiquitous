def funcRecursive(numArg):
    if(numArg > 0):
        result = numArg + funcRecursive(numArg-1)
        print(' If block result: ', result)
    else:
        result = 0
        print(' Else block result: ', result)
    return result

funcRecursive(4)


