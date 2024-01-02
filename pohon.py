tes = 10
p = 3

for a in range (1, tes-3):
    c= tes - a
    for b in range (c,):
        print (" ",  end="")
    for d in range (1, 2*a):
        print ( "*", end= "")
    print ()

for a in range (4, tes+1):
    c= tes - a
    for b in range (c):
        print (" ",  end="")
    for d in range (1, 2*a):
        print ( "*", end= "")
    print ()

for a in range (5, tes+1):
    c= tes - a
    for b in range ( c):
        print (" ",  end="")
    for d in range (1, 2*a):
        print ( "*", end= "")
    print ()

for j in range (p, 0, -1):
    print ("      "  + '*' * ((p - 3 + 2)) + '*' * ((p - 1 + 3)))
