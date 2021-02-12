def findOddManOut(numbers):
    numbers = list(map(int,list(numbers.split(" "))))
    if  1 <= len(numbers) <=2:
        return 1
    pos = {"odd":1,"even":1}
    oddcount = 0
    evencount = 0
    for i , n in enumerate(numbers):
        if (oddcount > evencount and evencount == 1):
            return pos["even"]
        elif (evencount > oddcount and oddcount == 1):
            return pos["odd"]
        if n % 2 == 0:
            evencount += 1
            pos["even"] = i + 1
        else:
            oddcount += 1
            pos["odd"] = i + 1
    if (oddcount > evencount and evencount == 1):
            return pos["even"]
    elif (evencount > oddcount and oddcount == 1):
            return pos["odd"]    
    return None

# print(iq_test("2 4 7 8 10"))
# print(iq_test("1 2 1 1"))
# print(iq_test("2 1 1 1"))
# print(iq_test("1 2 2 2"))
# print(iq_test("1 2 2 3 4"))
# print(iq_test('17 35 13 17 52 37 11 45 43 47 49 41 3 43 17 5 37 13 11 3 41 9 21 39 9 41 27 5 15 5 33 21 29 21 7 15 27 45 29 21 33 45 31'))