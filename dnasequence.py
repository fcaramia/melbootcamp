class DNASequence:
       
    def __init__(self, sequence):
        self.sequence = sequence
        self.dict = {'A':'T', 'T':'A','G':'C','C':'G'}
    def base_count(self, base):
        return self.sequence.count(base)
    
    def gc_content(self):
        return (self.base_count('G') + 
            self.base_count('C')) / float(len(self.sequence))
    
    def complement(base):
        return self.dict[base]
    
        
    # extra credit
    def reverse_complement(self):
        # reverse the sequence,
        # then change G<->C, A<->T
        rev = self.sequence[::-1]
        return ''.join(map(rev,self.complement))
       
        

