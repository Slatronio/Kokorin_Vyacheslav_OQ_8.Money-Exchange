for l in range(0,14):
    a = 'input' + str(l+1) + '.txt'
    b = 'output' + str(l+1) + '.txt'
    f = open(a)
    fb = open(b)
    line = f.readline().split()
    n1 = list(map(int, line))
    line = f.readline().split()
    k1 = list(map(int, line))
    line = f.readline().split()
    n2 = list(map(int, line))
    line = f.readline().split()
    k2 = list(map(int, line))
    line = f.readline().split()
    c = list(map(int, line))
    
    for i in range(len(c)):
        #if i != len(c)-1:
        #    c[i] *= n1[i+1]
        for j in range(k1[0]):
            if c[i] > k1[j+1]:
                c[i] -= 1
        if i != len(c)-1:
            c[i] *= n1[i+1]
    
    t = sum(c)
    c = []
    m = n2[0]-1
    del n2[0]
    n2 = sorted(n2)
    for i in range(m):
        c.insert(0, t%n2[i])
        t = t//n2[i]
    c.insert(0, t)
    for i in range(len(k2)-1):
        for j in range(len(c)):
            if c[j] > k2[i+1]:
                c[j] += 1
    line = list(map(int, fb.readline().split()))
    if c == line:
        print(str(l+1) + '. True')
    else:
        print(str(l+1) + '. False')
    
