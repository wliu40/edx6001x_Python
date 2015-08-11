def uniqueValues(aDict):
    repeated = {}
    res = []
    for i in aDict:
        if aDict[i] in repeated:
            repeated[aDict[i]] += 1
        else:
            repeated[aDict[i]] = 0
    for i in aDict:
        for j in repeated:
            if repeated[aDict[i]] == 0 and i not in res:
                res.append(i)
    
    return sorted(res)
