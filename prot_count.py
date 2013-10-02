f = open("uniprot_sprot.fasta")
count = 0 
for l in f:
    if l[0]=='>' and "OS=Homo sapiens" in l:
        count +=1
        
print "Num of Prots:", count
