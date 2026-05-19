# Mini-projects

Trying to relearn python and other stuff after long break.

## 1. DNA sequence analyzer program:
- inputs a dna sequence.
- checks if it is correct.
- gives length, DNA compliment seq, RNA complement seq, GC content, and amount of each bases seperately.

## 2. FASTA file analyzer:
- inputs a dna sequence name and description
- stores it in a fasta file in this format:

```fasta
>BRCA1 Homo sapiens breast cancer susceptibility gene
ATGCGTACGTTAGCTAGCTAGCTA
```
- user can search for a name
- it doesnt allow duplicates
- it also analyzes data (implemented from first project)

## 3. Gene expression analyzer in a csv:
- This is a gene expression analyzer program. This program can do these tasks:
  - store genes
  - count genes
  - find highest expressed gene
  - find lowest expressed gene
  - average expression
  - search for a gene
  - sort genes by expression         
  - cancer vs healthy expression graph
  - compare healthy vs cancer
  - detect upregulated genes
  - threshold filtering

## 4. DNA Pattern & Motif Finder:
- This program inputs a DNA sequence and do various functions:
  - find motif/pattern
  - Detect palindromic sequences
  - Find repeats
  - Search codons
  - Identify restriction sites

## 5. Protein Translation Simulator:
- This program inputs a DNA sequence and simulates protein translation:
  - start the translation only after finding start codon
  - stops the function if stop codon is found
  - for searching start codon it uses seperate searching system, where sliding window method is used mimicking original biology
  - after findng start codon the program uses search by 3 step increment
  - gives the final protein like this:
  - ```
    The translation of given sequence is:  Methionine - Phenylalanine - Glycine - Glutamic Acid - Histidine
    ```
