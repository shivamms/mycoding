
#incomeplete
def longestDiverseString(a: int, b: int, c: int) -> str:
    alen,blen,clen = math.ceil(a / 2.0), math.ceil(b / 2),math.ceil(c / 2.0)
    sizelist = sorted([a,b,c], reverse=True)
    sizelistdic = {}
    sizelistdic["a"] = a
    sizelistdic["b"] = b
    sizelistdic["c"] = c
    lenlist = [alen,blen,clen]
    largest = max(lenlist)
    chardic = {"a":alen, "b": blen, "c": clen}
    sortedcharlist = sorted(chardic, key=chardic.get, reverse=True)
    largestchar = sortedcharlist[0]
    lastdonelargest = False
    lastdonenonlargest = sortedcharlist[2]
    sortedchardic = {c:chardic[c] for c in sortedcharlist}
    result = ""
    i = 0
    print()
    while i < largest:
        for key, val in sortedchardic.items():
            print(key,lastdonelargest,lastdonenonlargest,sizelistdic[key])
            if sizelistdic[key] > 0:
                if (key == largestchar and lastdonelargest == False) or (key != largestchar and lastdonelargest == True and key != lastdonenonlargest):
                    result += "".join(key * (math.ceil(val/2)))
                    sizelistdic[key] -= math.ceil(val/2)
                    if key != largestchar:
                        lastdonenonlargest = key
                        lastdonelargest = False
                if key == largestchar:
                    lastdonelargest = True
                    
            print(result)
        i += 1
        
    return result
    
a = 1
b = 1
c = 7
a = 2
b = 2
c = 1
print(longestDiverseString(a, b, c))