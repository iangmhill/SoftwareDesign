# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Ian Hill
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
from load import load_seq

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    aminoacid = ""
    for n in range(0,len(dna),3):
        for m in range(len(codons)):
            if dna[n:n+3] in codons[m]:
                aminoacid = aminoacid + aa[m]
    return aminoacid
                 

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    testinputs = ["ATGATCCTC","ATGCAAGAA","GGTCGCTGG"]
    testresults = ["MIL", "MQE","GRW"]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n] + " Expected output: " + testresults[n] + " Actual output: " + coding_strand_to_AA(testinputs[n]))

def get_complement(nuc):
    """ Takes a character input nuc representing a nucleotide and 
        returns that nucleotides complementary nucleotide 
    """
    if nuc == 'T':
        return 'A'
    elif nuc == 'A':
        return 'T'
    elif nuc == 'G':
        return 'C'
    elif nuc == 'C':
        return 'G'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """   
    revcom = ""
    for n in range(len(dna)):
        revcom += get_complement(dna[-1-n])
    return revcom
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    testinputs = ["ATGATCCTC","ATGCAAGAA","GGTCGCTGG"]
    testresults = ["GAGGATCAT", "TTCTTGCAT","CCAGCGACC"]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n] + " Expected output: " + testresults[n] + " Actual output: " + get_reverse_complement(testinputs[n]))

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    for n in range(0,len(dna),3):
        if dna[n:n+3] == "TAG" or  dna[n:n+3] == "TGA" or dna[n:n+3] == "TAA":
            return dna[:n]
    return dna

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    testinputs = ["ATGATCCTCTAGGTGACACC","ATGCAATAAAGATCAGCT","GGTCGCTGGTGAGTACGTAGCTAGCTGATCGGTGCAT","ATGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"]
    testresults = ["ATGATCCTC", "ATGCAA","GGTCGCTGG","ATGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n] + " Expected output: " + testresults[n] + " Actual output: " + rest_of_ORF(testinputs[n]))

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs_oneframe = []
    n = 0
    while n <= (len(dna)-3):
        if dna[n:n+3] == "ATG":
            all_ORFs_oneframe.append(rest_of_ORF(dna[n:]))
            n += len(all_ORFs_oneframe[-1])
        else:
            n += 3
            
    return all_ORFs_oneframe       
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    testinputs = ["ATGCATGAATGTAGATAGATGTGCCC","ATGCATGAATGTAGATAGATGTGCCCCTAGATG"]
    testresults = [['ATGCATGAATGTAGA', 'ATGTGCCC'],['ATGCATGAATGTAGA', 'ATGTGCCCC','ATG']]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n])
        print (" Expected output: ")
        print (testresults[n])
        print (" Actual output: ")
        print (find_all_ORFs_oneframe(testinputs[n]))

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    return find_all_ORFs_oneframe(dna[0:]) + find_all_ORFs_oneframe(dna[1:]) + find_all_ORFs_oneframe(dna[2:])

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    testinputs = ["ATGCATGAATGTAG","ATGCATTAATGTAGATAGATCATCCC"]
    testresults = [['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG'],['ATGCAT', 'ATG']]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n])
        print (" Expected output: ")
        print (testresults[n])
        print (" Actual output: ")
        print (find_all_ORFs(testinputs[n]))

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    testinputs = ["ATGCATGAATGTAG","ATGCATTAATGTAGATAGATCATCCC","TGCAATGTTAGATATATCTGCTAACCATCTG"]
    testresults = [['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG', 'ATGCAT'],['ATGCAT', 'ATG', 'ATGATCTATCTACAT', 'ATGCAT'],['ATGGTTAGCAGATATATC', 'ATGTTAGATATATCTGCTAACCATCTG']]
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n])
        print ("Reverse Complement: " + get_reverse_complement(testinputs[n]))
        print (" Expected output: ")
        print (testresults[n])
        print (" Actual output: ")
        print (find_all_ORFs_both_strands(testinputs[n]))

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    max_length = 0
    max_index = 0
    ORFs = find_all_ORFs_both_strands(dna)
    for n in range(len(ORFs)):
        if len(ORFs[n]) > max_length:
            max_length = len(ORFs[n])
            max_index = n
    if len(ORFs) > 0:
        return ORFs[max_index]
    else:
        return []

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    testinputs = ["ATGCATGAATGTAG","ATGCATTAATGTAGATAGATCATCCC","TGCAATGTTAGATATATCTGCTAACCATCTG"]
    testresults = ['ATGCATGAATGTAG','ATGATCTATCTACAT','ATGTTAGATATATCTGCTAACCATCTG']
    for n in range(0,len(testinputs)):
        print ("Input: " + testinputs[n])
        print (" Expected output: ")
        print (testresults[n])
        print (" Actual output: ")
        print (longest_ORF(testinputs[n]))

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    max_length = 0

    for n in range(num_trials):
        #print(n),
        dna_list = list(dna)
        shuffle(dna_list)
        dna_shuffled = collapse(dna_list)       
        length = len(longest_ORF(dna_shuffled))
        if length > max_length:
            max_length = length
    return max_length

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    aminoacidsequences = []
    ORFs = find_all_ORFs_both_strands(dna)
    for n in range(len(ORFs)):
        if len(ORFs[n]) > threshold:
            aminoacidsequences.append(coding_strand_to_AA(ORFs[n]))
    return aminoacidsequences


dna = load_seq("./data/X73525.fa")
#print(longest_ORF_noncoding(dna,1500))
print(gene_finder(dna,849))