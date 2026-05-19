a = input("Enter the DNA sequence to stimulate protein translation: ").upper()
valid = True
translation = []
dictionary_codons = {"ATG": "Methionine",
                        "TAA": "Stop",
                        "TAG": "Stop",
                        "TGA": "Stop",

                        "TTT": "Phenylalanine",
                        "TTC": "Phenylalanine",

                        "TTA": "Leucine",
                        "TTG": "Leucine",
                        "CTT": "Leucine",
                        "CTC": "Leucine",
                        "CTA": "Leucine",
                        "CTG": "Leucine",

                        "ATT": "Isoleucine",
                        "ATC": "Isoleucine",
                        "ATA": "Isoleucine",

                        "GTT": "Valine",
                        "GTC": "Valine",
                        "GTA": "Valine",
                        "GTG": "Valine",

                        "TCT": "Serine",
                        "TCC": "Serine",
                        "TCA": "Serine",
                        "TCG": "Serine",
                        "AGT": "Serine",
                        "AGC": "Serine",

                        "CCT": "Proline",
                        "CCC": "Proline",
                        "CCA": "Proline",
                        "CCG": "Proline",

                        "ACT": "Threonine",
                        "ACC": "Threonine",
                        "ACA": "Threonine",
                        "ACG": "Threonine",

                        "GCT": "Alanine",
                        "GCC": "Alanine",
                        "GCA": "Alanine",
                        "GCG": "Alanine",

                        "TAT": "Tyrosine",
                        "TAC": "Tyrosine",

                        "CAT": "Histidine",
                        "CAC": "Histidine",

                        "CAA": "Glutamine",
                        "CAG": "Glutamine",

                        "AAT": "Asparagine",
                        "AAC": "Asparagine",

                        "AAA": "Lysine",
                        "AAG": "Lysine",

                        "GAT": "Aspartic Acid",
                        "GAC": "Aspartic Acid",

                        "GAA": "Glutamic Acid",
                        "GAG": "Glutamic Acid",

                        "TGT": "Cysteine",
                        "TGC": "Cysteine",

                        "TGG": "Tryptophan",

                        "CGT": "Arginine",
                        "CGC": "Arginine",
                        "CGA": "Arginine",
                        "CGG": "Arginine",
                        "AGA": "Arginine",
                        "AGG": "Arginine",

                        "GGT": "Glycine",
                        "GGC": "Glycine",
                        "GGA": "Glycine",
                        "GGG": "Glycine"
                        }

start = False
start_pos = 0

for i in a:
    if i not in "AGTC":
        valid = False
if not valid:
    print("Invalid sequence.")
else:
    for i in range(0, len(a) - 3 + 1):
        splt = a[i : i + 3]
        h = dictionary_codons.get(splt)
        if splt == "ATG":
            start = True
            print(f"Start codon found at {i}\n")
            start_pos = i
            break
        else:
            print(f"Start codon not found in {i} checking next position.\n")
    if start:
        for i in range(start_pos, len(a) - 3 + 1, 3):
            splt = a[i : i + 3]
            h = dictionary_codons.get(splt)
            if splt == "TAA" or splt == "TGA" or splt == "TAG":
                print(f"Stop codon found at the {i} position. Stopping translation.")
                break
            else:
                translation.append(h)
if valid:
    print("The translation of given sequence is: ", " - ".join(translation))
