matrica = [[0]*5 for i in range(3)]


def determinanta(stupac_1, stupac_2, stupac_3, stupac_4, stupac_5):

    d1 = matrica[0][stupac_1]*matrica[1][stupac_2]*matrica[2][stupac_3]
    d2 = matrica[0][stupac_2] * matrica[1][stupac_3] * matrica[2][stupac_4]
    d3 = matrica[0][stupac_3] * matrica[1][stupac_4] * matrica[2][stupac_5]
    d4 = matrica[2][stupac_1] * matrica[1][stupac_2] * matrica[0][stupac_3]
    d5 = matrica[2][stupac_2] * matrica[1][stupac_3] * matrica[0][stupac_4]
    d6 = matrica[2][stupac_3] * matrica[1][stupac_4] * matrica[0][stupac_5]
    d = d1 + d2 + d3 - (d4 + d5 + d6)
    return d


for i in range(3):
    for j in range(4):
        print("Unesite element u ", i+1, ". redu i ", j+1, ". stupcu: ")
        a = int(input())
        matrica[i][j] = a

for i in matrica:
    print(i)

det = determinanta(0, 1, 2, 0, 1)
detx = determinanta(3, 1, 2, 3, 1)
dety = determinanta(0, 3, 2, 0, 3)
detz = determinanta(0, 1, 3, 0, 1)

print("x: ", detx/det)
print("y: ", dety/det)
print("z :", detz/det)
