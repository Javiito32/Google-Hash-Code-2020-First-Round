def solveHashCode(fileName):
    f = open(fileName + ".txt", "r")
    f = f.read().split("\n")
    line1 = f[0].split()
    TotalDays = int(line1[2])

    line2 = f[1].split()
    BookScores = line2

    fileLines = len(f)-1

    libraries = []
    solutions = []
    order = []

    class library:
        def __init__ (self, books, signIn, perDay, libNum):
            self.books = books
            self.signIn = signIn
            self.perDay = perDay
            self.signed = False
            self.signing = False
            self.libNum = libNum
            self.points = 0
            self.rate = 0

        def setBooksList(self):
            _books = self.books.copy()
            Fbooks = {}
            c = 0
            for i in _books:
                Fbooks.update({int(i): int(BookScores[int(i)])})
                c += 1
            Fbooks = {k: v for k, v in sorted(Fbooks.items(), key=lambda item: item[1], reverse=True)}
            self.books = Fbooks.copy()
            Fbooks = {}

        def setPoints(self, pastDays):
            _x = 0
            _books = self.books.copy()
            bookcount = TotalDays-pastDays
            bookcount += 1
            for x in list(_books)[0:bookcount]:
                _x += int(BookScores[x])
            self.points = _x

    c = 0

    for i in range(2, fileLines-1, 2):
        data = f[i].split()
        libraries.append(library(f[i+1].split(), int(data[1]), int(data[2]), c))
        libraries[c].setBooksList()
        solutions.append([])
        c += 1

    #for k in libraries[0].books.keys():
    #    print("Clave: " + str(k) + "Valor: " + str(libraries[0].books[k]))

    #dayCounter = 0
    #GlobalSignIn = False
    #SignInTimer = 0
    #librarySigning = -1
    pastDays = 0
    signTimes = {}
    def reOrder(passedDays):
        _signTimes = {}
        for i in libraries:
            if i.signed == False:
                i.setPoints(passedDays)
                exp = TotalDays-passedDays
                exp -= i.signIn
                i.rate = i.points*exp
                _signTimes.update({i.libNum: i.rate})

        _signTimes = {k: v for k, v in sorted(_signTimes.items(), key=lambda item: item[1], reverse=True)}
        return _signTimes
        
    
    signTimes = reOrder(pastDays)

    while len(signTimes) > 0:
        signTimes = reOrder(pastDays)
        if signTimes != {}:
            k = next(iter(signTimes))
            libraries[k].signed = True
            pastDays += libraries[k].signIn
            if pastDays <= TotalDays:
                order.append(k)
                qtty = (libraries[k].perDay*(TotalDays-pastDays))+libraries[k].perDay
                qtty += 1
                for x in list(libraries[k].books)[0:qtty]:
                    solutions[k].append(x)
            else:
                break


    #while dayCounter <= TotalDays+1:
    #    for i in range(0, len(libraries)):
    #        if libraries[i].signed == True:
    #            counter = libraries[i].perDay
    #            for g in range(counter):
    #                if libraries[i].books != {}:
    #                    k = next(iter(libraries[i].books))
    #                    del libraries[i].books[k]
    #                    solutions[libraries[i].libNum].append(k)
    #
    #    if GlobalSignIn == False and _signTimes != {}:
    #        k = next(iter(_signTimes))
    #        del _signTimes[k]
    #        librarySigning = k
    #        SignInTimer = libraries[k].signIn
    #        GlobalSignIn = True
    #        order.append(k)
    #        
    #    elif GlobalSignIn and SignInTimer <= 2:
    #        GlobalSignIn = False
    #        libraries[librarySigning].signed = True
    #        SignInTimer -= 1
    #        librarySigning = -1
    #        if _signTimes != {}:
    #            k = next(iter(_signTimes))
    #            del _signTimes[k]
    #            librarySigning = k
    #            SignInTimer = libraries[k].signIn
    #            GlobalSignIn = True
    #            order.append(k)
    #            
    #    if GlobalSignIn == False:
    #        print(GlobalSignIn)
    #    
    #    SignInTimer -= 1
    #
    #    dayCounter+=1

    sol = open("out/" + fileName + ".out", "w")
    sol.write(str(len(order)) + "\n")
    for i in order:
        sol.write(str(i) + " " + str(len(solutions[i])) + "\n")
        _x = ""
        for x in solutions[i]:
            _x += str(x) + " "
        sol.write(_x + "\n")
    sol.close()

files = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]

for A in files:
    solveHashCode(A)