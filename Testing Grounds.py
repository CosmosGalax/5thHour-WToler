Var = "I"
BackUpVar = "I"
C = 0
for _ in range(100):
    C = C + 1
    if C == 20:
        Var = "IIII"
    if C == 40:
        Var = "IIII"

    if C == 60:
        Var = "IIII"

    if C == 80:
        Var = "IIII"

    if C == 100:
        Var = "IIII"
        Var = BackUpVar
    if C % 2:
        Var = BackUpVar
        BackUpVar = BackUpVar + "II"
        Var = Var + "II"
        print(Var)
    elif True:
        print(Var)