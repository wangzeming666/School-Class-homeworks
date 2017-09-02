def myrange(*argu):
    i = 0
    step = 1
    stop = argu[1]
    if len(argu) == 0:
        raise TypeError
    elif len(argu) == 1:
        stop  = argu[0]
    elif len(argu) == 2:
        if argu[0] == 0:pass   
        else:
            i = argu[0]
            stop = argu[1]
    else:
        i = argu[0]
        step = argu[2]
    while i < stop:
        yield i
        i += step
        
