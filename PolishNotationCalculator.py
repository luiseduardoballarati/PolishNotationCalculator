def evaluatePNExpression(input):
    try:
        for i in range(0, len(input)):
            try:
                input[i] = int(input[i])
                if input[i] > 300 or input[i] < -300:
                    return None
            except:
                pass
        k = 2
        res = 0
        while len(input) > 1:
            if k == len(input) and type(input[k-1]) == int:
                if input[k-3] == '+':
                    res = input[k-1] + input[k-2]
                if input[k-3] == '-':
                    res = input[k-1] - input[k-2]
                if input[k-3] == '*':
                    res = input[k-1] * input[k-2]
                if input[k-3] == '/':
                    res = input[k-1] // input[k-2]
                    if res == 0:
                        return None
                input.pop(k-1)
                input.pop(k-2)
                input[k-3] = res
                k = 2
            if len(input) == 1:
                if int(input[0]) or input[0] == 0:
                    return input[0]
                    break
                else:
                    return None
                    break
            if type(input[k-1]) is int and type(input[k]) is int:
                if input[k-2] == '+':
                    res = input[k-1] + input[k]
                if input[k-2] == '-':
                    res = input[k - 1] - input[k]
                if input[k-2] == '*':
                    res = input[k - 1] * input[k]
                if input[k-2] == '/':
                    res = input[k - 1] // input[k]
                input.pop(k-2)
                input.pop(k-2)
                input[k-2] = res
                k = 2
            if len(input) == 1:
                if int(input[0]) or input[0] == 0:
                    return input[0]
                    break
                else:
                    return None
                    break
            k += 1
    except:
        return None