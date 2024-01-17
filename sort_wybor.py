#SORTOWANIE PRZEZ WYBÓR

def sortowanieWybor(zbior):

    for przejscie in range(len(zbior)):
        mindex = przejscie

        for i in range(przejscie + 1, len(zbior)):
            if zbior[i] < zbior[mindex]:
                mindex = i

        zbior[przejscie], zbior[mindex] = zbior[mindex], zbior[przejscie]
        print(zbior)
    print("")
    return zbior


zbior = [3,7,2,4,5,10,1,3]

print(zbior)
print(sortowanieWybor(zbior))