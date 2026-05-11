def store_gene():
    a = input("Enter the name of the gene: ")
    b = input("Enter the healthy expression level: ")
    c = input("Enter cancer expression level: ")

    with open("gene_exp.csv", "a") as file:
        #valid = True
        d = b.isdigit()
        e = c.isdigit()
        if d == False or e == False:
            print("Invalid input")
            return
        else:
            file.write(f"{a},{b},{c}\n")
            print("\nFile stored successfully\n")
def count_genes():
    with open("gene_exp.csv", "r") as file:
        c = 0
        for i in file:
            c = c+1
        org_count = c - 1
        if c == 0:
            print("The count of genes present in the file is: 0")
        else:
            print("The count of genes present in the file is: ", org_count)
def find_high_expressed_gene():
    with open("gene_exp.csv", "r") as file:
        highest_healthy = ""
        highest_healthy_value = 0
        highest_cancer = ""
        highest_cancer_value = 0
        next(file)
        for i in file:
            clean = [item.strip() for item in i.strip().split(",")]
            gene_name = clean[0]
            healthy = int(clean[1])
            cancer = int(clean[2])
            if healthy > highest_healthy_value:
                highest_healthy_value = healthy
                highest_healthy = gene_name
            if cancer > highest_cancer_value:
                highest_cancer_value = cancer
                highest_cancer = gene_name
        print("The highest expressed healthy gene is: \n","name:",highest_healthy,"\n", "value:",highest_healthy_value)
        print("\nThe highest expressed cancer gene is: \n","name:",highest_cancer,"\n", "value:",highest_cancer_value)
def find_low_expressed_gene():
    with open("gene_exp.csv","r") as file:
        next(file)
        new_line = next(file)
        cleaned = new_line.strip().split(",")
        low_healthy_value = int(cleaned[1])
        low_cancer_value = int(cleaned[2])
        cancer_gene_name = cleaned[0]
        healthy_gene_name = cleaned[0]
        for i in file:
            clean = [item.strip() for item in i.strip().split(",")]
            gene_name = clean[0]
            healthy = int(clean[1])
            cancer = int(clean[2])
            if healthy < low_healthy_value:
                low_healthy_value = healthy
                healthy_gene_name = gene_name
            if cancer < low_cancer_value:
                low_cancer_value = cancer
                cancer_gene_name = gene_name
        print("The lowest expressed healthy gene is: \n","name:",healthy_gene_name,"\n", "value:",low_healthy_value)
        print("\nThe lowest expressed cancer gene is: \n","name:",cancer_gene_name,"\n", "value:",low_cancer_value)
def find_avg_expressed_gene():
    with open("gene_exp.csv", "r") as file:
        next(file)
        #second = file(next)
        healthy_total = 0
        cancer_total = 0
        total_genes = 0
        for i in file:
            cleaned = [items.strip() for items in i.strip().split(",")]
            heal = int(cleaned[1])
            canc = int(cleaned[2])
            healthy_total = healthy_total + heal
            cancer_total += canc
            total_genes += 1
        if total_genes == 0:
            print("On average, healthy genes are expressed at: 0")
            print("On average, cancer genes are expressed at: 0")
        else:
            avg_heal_expression = healthy_total/total_genes
            avg_canc_expression = cancer_total/total_genes
            print("On average, healthy genes are expressed at: ", str(avg_heal_expression))
            print("On average, cancer genes are expressed at: ", str(avg_canc_expression))
def search_for_gene():
    a = input("Enter the name of the gene you want to search: ")
    found = False
    with open("gene_exp.csv", "r") as file:
        next(file)
        for i in file:
            cleaned = [items.strip() for items in i.strip().split(",")]
            search = cleaned[0]
            if a.lower() == search.lower():
                found = True
                print("The gene is found and the expressions are: \n[Gene,Healthy,Cancer]","\n",cleaned)
    if found == False:
        print("The gene is not present in the file.")
def sort_genes():
    with open("gene_exp.csv", "r") as file:
        healthy = {}
        next(file)
        for i in file:
            clean = [items.strip() for items in i.strip().split(",")]
            gene_name = clean[0]
            healthy_num = int(clean[1])
            healthy[gene_name] = healthy_num
        sorted_list_asending = sorted(healthy.items(), key=lambda item : item[1])
        sorted_list_desending = sorted(healthy.items(), key=lambda item : item[1], reverse= True)
        print("The sorted list in asending order is: \n", sorted_list_asending,"\n")
        print("The sorted list in desending order is: \n", sorted_list_desending,"\n")
def search_for_gene1(a):
    found = False
    with open("gene_exp.csv", "r") as file:
        next(file)
        for i in file:
            cleaned = [items.strip() for items in i.strip().split(",")]
            search = cleaned[0]
            if a.lower() == search.lower():
                found = True
                print("The gene is found and the expressions are: \n[Gene,Healthy,Cancer]","\n",cleaned)
                return cleaned
    if found == False:
        return False
def compare():
    b = input("Enter the name of the gene you want to compare: ")
    a = search_for_gene1(b)
    if a == False:
        print("No matching Gene found in the file.\n")
    else:
        healthy = int(a[1])
        cancer = int(a[2])
        if healthy > cancer:
            print("Healthy genes are expressed at high level.\n")
        elif cancer > healthy:
            print("Cancer genes are expressed at high level.\n")
        else:
            print("Both genes are expressed at the same level\n")  
def upregulated():
    b = input("Enter the name of the gene you want to search: ")
    a = search_for_gene1(b)
    if a == False:
        print("No matching Gene found in the file.\n")
    else:
        healthy = int(a[1])
        cancer = int(a[2])
        if healthy > cancer:
            print("downregulated.\n")
        elif cancer > healthy:
            print("upregulated.\n")
        else:
            print("same expression\n")
import matplotlib.pyplot as plt
import numpy as np
def graph_visualization():
    gene_name = []
    healthy_expression = []
    cancer_expression = []
    with open("gene_exp.csv", "r") as file:
        next(file)
        for i in file:
            cleaned = [items.strip() for items in i.strip().split(",")]
            gene_name.append(cleaned[0])
            healthy_expression.append(int(cleaned[1]))
            cancer_expression.append(int(cleaned[2]))
    x = np.arange(len(gene_name))
    width = 0.35

    fig, ax = plt.subplots()

    ax.bar(x - width/2, healthy_expression, width, label='Healthy', color = 'skyblue')
    ax.bar(x + width/2, cancer_expression, width, label='Cancer', color = 'red')

    ax.set_ylabel('Expression level')
    ax.set_title("Gene expression: healthy vs cancer")
    ax.set_xticks(x)
    ax.set_xticklabels(gene_name)
    ax.legend()
    plt.show()
def threshold_filter():
    a = input("What expression you want to find threshold for (enter 1 for healthy 2 for cancer): ")
    
    if a == "1":
        b = input("Enter the threshold value: ")
        c = b.isdigit()
        if c == False:
            print("Invalid input")
        else:
            fil_list = []
            with open("gene_exp.csv", "r") as file:
                next(file)
                for i in file:
                    cleaned = [items.strip() for items in i.strip().split(",")]
                    healthy = int(cleaned[1])
                    if healthy > int(b):
                        fil_list.append(cleaned)
            if len(fil_list) == 0:
                print("No genes cross the threshold\n")
            else:
                print(fil_list)
    elif a == "2":
        b = input("Enter the threshold value: ")
        c = b.isdigit()
        if c == False:
            print("Invalid input")
        else:
            fil_list = []
            with open("gene_exp.csv", "r") as file:
                next(file)
                for i in file:
                    cleaned = [items.strip() for items in i.strip().split(",")]
                    cancer = int(cleaned[2])
                    if cancer > int(b):
                        fil_list.append(cleaned)
            if len(fil_list) == 0:
                print("No genes cross the threshold\n")
            else:
                print(fil_list)
    else:
        print("invalid input\n")

while True:
    print("Count genes(1)\n" \
    "Find highest expressed gene(2)\n" \
    "Find lowest expressed gene(3)\n"\
    "Find average expression(4)\n" \
    "Search for a gene(5)\n" \
    "Sort genes by expression(6)\n"\
    "Show expression graph(7)\n" \
    "Compare healthy vs cancer(8)\n" \
    "Detect upregulated genes(9)\n"\
    "Threshold filtering(10)\n" \
    "Store genes(11)\n"\
    "exit function(12)")
    i = input("Enter the number of which function you want to do(1/2/3/4.../12): ")
    if i == "1":
        count_genes()
    elif i == "2":
        find_high_expressed_gene()
    elif i == "3":
        find_low_expressed_gene()
    elif i == "4":
        find_avg_expressed_gene()
    elif i == "5":
        search_for_gene()
    elif i == "6":
        sort_genes()
    elif i == "7":
        graph_visualization()
    elif i == "8":
        compare()
    elif i == "9":
        upregulated()
    elif i == "10":
        threshold_filter()
    elif i == "11":
        store_gene()
    elif i == "12":
        break
    else:
        print("Invalid choice")
