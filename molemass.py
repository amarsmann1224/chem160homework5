Dict={"H":1.0079,"C":12.0107,"N":14.0067,"O":15.9994,"P":30.9738,"S":32.0660,"K":39.0983,"F":18.9984}
def molemass(word):
    mass=0
    for i in word:
        mass += Dict[i]
    return mass