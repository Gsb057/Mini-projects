def find_pattern():
    seq = input("Enter the DNA sequence: ")
    pat = input("Enter the pattern you want to find: ")
    a = seq.upper()
    b = pat.upper()
    l=[]
    valid = True
    for i in a:
        if i not in "AGCT":
                valid = False
    for i in b:
        if i not in "AGCT":
                valid = False
    if valid:
        length = len(b)
        for i in range(len(a) - length + 1):
            stringy = a[i:length+i]
            if stringy == b:
                l.append(i)
        if len(l) == 0:
             print("No match found")
        else:
            print("The pattern is found in the sequence in these positions: ", l)
    else:
        print("Invalid input")

def find_palindrom():
    seq = input("Enter the DNA sequence: ")
    a = seq.upper()
    valid = True
    for i in a:
        if i not in "AGCT":
            valid = False
    if not valid:
        print("Invalid DNA sequence.")
        return
    try:
        length = int(input("Enter the length of the palindroms you want or 0 for every palindrom present: "))
    except:
        print("Invalid length")
        return
    if length < 0:
        print("Invalid length")
    elif length > len(a):
        print("Invalid length.")
    elif length % 2 != 0:
        print("DNA palindromes are usually even length")
    elif length == 0:
        l = []
        for j in range(4,9,2):
            legan = j
            for i in range(len(a) - legan + 1):
                comp = ""
                striped = a[i : i + legan]
                for j in striped:
                    if j == "A":
                        comp += "T"
                    elif j == "T":
                        comp += "A"
                    elif j == "G":
                        comp += "C"
                    elif j == "C":
                        comp += "G"
                reverse_comp = comp[::-1]
                if reverse_comp == striped:
                    l.append((i,striped))
        if len(l) == 0:
            print("No palindroms found")
        else:
            print("Palindromes found at: ", l)
    else:
        l = []
        
        for i in range(len(a) - length + 1):
            comp = ""
            striped = a[i : i + length]
            for j in striped:
                if j == "A":
                    comp += "T"
                elif j == "T":
                    comp += "A"
                elif j == "G":
                    comp += "C"
                elif j == "C":
                    comp += "G"
            reverse_comp = comp[::-1]
            if reverse_comp == striped:
                l.append((i, striped))
        if len(l) == 0:
            print("No palindroms found")
        else:
            print("Palindromes found at: ", l)

def find_repeats():
    seq = input("Enter the DNA sequence: ")
    repeat = input("Enter the repeating unit you want to find: ")
    a = seq.upper()
    b = repeat.upper()
    if b == "":
        print("Invalid input")
        return
    valid = True
    l = []
    occurances = 0
    for i in a:
        if i not in "AGTC":
            valid = False
    for i in b:
        if i not in "AGTC":
            valid = False
    if valid == False:
        print("Invalid sequence.")
        return
    else:
        for i in range(len(a) - len(b) + 1):
            split = a[i : i + len(b)]
            if split == b:
                occurances += 1
                l.append(i)
    print("The repeats are found at: ", l)
    print("Occurances: ", occurances)

def search_codons():
    seq = (input("Enter the sequence you want to search codons for: ")).upper()
    valid = True
    for i in seq:
        if i not in "AGTC":
            valid = False
    if not valid:
        print("Invalid input")
        return
    else:
        start_codons = "ATG"
        stop_codons = ("TAA", "TAG", "TGA")
        for i in range(len(seq) - 2, 3):
            split = seq[i:i+3]
            if split == start_codons:
                print("Start codon found at: ", i)
            elif split in stop_codons:
                print("Stop codon found at: ", i)

def identify_restriction_sites():
    seq = input("Enter the sequence you want to find restriction sites for: ").upper()
    valid = True
    enzymes = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT"
    }
    l = []
    for i in seq:
        if i not in "AGTC":
            valid = False
    if not valid:
        print("Invalid input.")
        return
    else:
        for i in range(len(seq) - 6 + 1):
            split = seq[i : i + 6]
            for k,v in enzymes.items():
                if split == v:
                    l.append((k,i))
        print(f"The restriction sites found are: {l}")

while True:
    a = input("Enter which function you want to use\n" \
    "1 for Finding a specific pattern in a DNA\n" \
    "2 for Finding a palindrom in a DNA\n" \
    "3 for Finding repeats\n" \
    "4 for Finding codons\n" \
    "6 for finding restriction sites\n" \
    "0 for exit :\n")
    b = a.isdigit()
    if b == False:
        print("Invalid input")
        break
    if a == "1":
        find_pattern()
    elif a == "2":
        find_palindrom()
    elif a == "3":
        find_repeats()
    elif a == "4":
        search_codons()
    elif a == "6":
        identify_restriction_sites()
    elif a == "0":
        print("exiting...")
        break
    else:
        print("invalid input")
