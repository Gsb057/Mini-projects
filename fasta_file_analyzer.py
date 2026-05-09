
def store_data():
    sequence_name = input("\nEnter your name of the sequence: ")
    sequence_des = input("Enter the description of the seq: ")
    sequence = input("Enter the sequence: ")
    valid = True
    sequence = sequence.upper()
    found = False
    with open("seq.fasta", "r") as file:
        for line in file:
            if line.startswith(">"):
                c = line.removeprefix(">")
                cleaned_line = c.strip()
                l = cleaned_line.split()
                name  = l[0]
                if name.lower() == sequence_name.lower():
                    found = True
                    
                    break
    if found == False:
        for i in sequence:
            if i not in "AGCT":
                valid = False
                break
        if valid:
            with open("seq.fasta", "a") as file:
                file.write(">" + sequence_name)
                file.write(" " + sequence_des + "\n" )
                file.write(sequence + "\n" )
                print("Sequence stored successfully\n")
        else:
            print("wrong sequence data")
    else:
        print("Name already found try with different name")
def search_data():
    search = input("Enter the name of the file you want to search: ")
    found = False
    with open("seq.fasta", "r") as file:
        for line in file:
            if line.startswith(">"):
                c = line.removeprefix(">")
                cleaned_line = c.strip()
                l = cleaned_line.split()
                name  = l[0]
                if name.lower() == search.lower():
                    found = True
                    print("Match found: ", cleaned_line)
    if found == False:
        print("No match found")
def analyze_data():
    search = input("Enter the name of the file you want to analyze: ")
    found = False
    with open("seq.fasta", "r") as file:
        for line in file:
            if line.startswith(">"):
                c = line.removeprefix(">")
                cleaned_line = c.strip()
                l = cleaned_line.split()
                name  = l[0]
                if name.lower() == search.lower():
                    found = True
                    saq = file.readline()
                    god = saq.strip()
                    print(god)
                    length = len(god)
                    print("Length of the DNA seq is: ", length , "\n")
                    A = 0
                    T = 0
                    G = 0
                    C = 0
                    for i in god:
                        if i == "A":
                            A += 1
                        elif i == "G":
                            G += 1
                        elif i == "C":
                            C += 1
                        elif i == "T":
                            T += 1
                    print("A: ", A,"\n",
                          "G: ", G,"\n",
                          "C: ", C,"\n",
                          "T: ", T,"\n",)
                    GC = ((G+C)/length) * 100
                    print("GC content is: ", GC,"%\n")
                    comp = ""
                    for i in god:
                        if i == "A":
                            comp += "T"
                        elif i == "T":
                            comp += "A"
                        elif i == "G":
                            comp += "C"
                        elif i == "C":
                            comp += "G"
                    rev = comp[::-1]
                    print("Reverse complement of the seq is: ", rev,"\n")
    if found == False:
        print("No match found")

while True:
    print("Store data(1)\n" \
    "analyze data(2)\n" \
    "search data(3)\n"\
    "exit function(4)")
    i = input("Enter the number of which function you want to do(1/2/3/4): ")
    if i == "1":
        store_data()
    elif i == "2":
        analyze_data()
    elif i == "3":
        search_data()
    elif i == "4":
        break
    else:
        print("Invalid choice")
