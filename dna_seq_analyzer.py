p = input("\nInsert your DNA seq here: ")
p = p.upper()
print("Your sequence is:", p)
valid = True
if p == "":
    valid = False
for i in p:
    if i not in "ATGC":
        valid = False
        break
if valid:
    k = len(p)
    print("The length of the DNA sequence is: ", k)
    A = 0
    G = 0
    C = 0
    T = 0
    for i in p:
        if i == "A":
                A+=1
        elif i == "G":
            G+= 1
        elif i == "C":
            C+= 1
        else:
            T+=1
    print("\n A:", A,
            "\nG:", G,
            "\nC:", C,
            "\nT:", T)
    GC = ((G + C)/k) * 100
    print("GC content: ", GC,"%")
    comp = ""
    for i in p:
        if i == "A":
            comp += "T"
        elif i == "T":
            comp += "A"
        elif i == "G":
            comp += "C"
        elif i == "C":
            comp += "G"
    print("Complementary sequence is: ", comp)
    rna_comp = ""
    for i in comp:
        if i == "T":
            rna_comp += "U"
        else:
            rna_comp += i
    print("RNA complimentary seq is: ", rna_comp)
else:
    print("Wrong DNA sequence")



