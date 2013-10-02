from dnasequence import DNASequence


a = DNASequence('ACCTGGGTAAACCC')
print a.base_count('C')
print a.gc_content()
print a.reverse_complement()
