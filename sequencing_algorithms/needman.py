#!/usr/bin/env python3 
# creating the substution matrix 
## scoring matrix
## the axes has the two sequences 
## we start with bottom up appraoch, where the first value is 0. and every time we go diagonal. there can three possible values. 
## value from the side bix is always 0, and value from bottom/top box is 1 and then match = +2, mismatch = -1 and gap = 0. then we compare all the three values and keep the largest value
## initiation point has the 1st column and 1st row is -2, -4, -6 and -8.. 
def create_submat (match, mismatch, alphabet):
    """Function to assign score for match and mismatch""" 
    
    sm = {}
    for c1 in alphabet:
        for c2 in alphabet:
            if (c1 == c2):
                sm[c1+c2] = match
            else:
                sm[c1+c2] = mismatch
    return sm

# function to calculate the score for each position 
def score_pos (c1, c2, sm, g):
    """This function calculates the score for each position"""
    if c1 == "-" or c2 == "-":
        ## if a space is foung g = -2 should be return
        return g
    else:
        ## else the match or mismatch is to be returned
        return sm[c1+c2]

def print_mat (mat):
    """This function generates the scoring matrix for the len of mat with both the sequence lengths"""
    for i in range(0,len(mat)):
        for j in range(len(mat[i])):
            print('{0:4d}'.format(mat[i][j]),end = '')
        print()
    print()


def needleman_Wunsch (seq1, seq2, sm, g):
    """This function prints all the scores for the whole matrix"""
    S = [[0]]
    T = [[0]]
    for j in range(1, len(seq2)+1):
        ## Since first value is 0 we start with the second position
        ## and first add the -2 i.e gaps for the whole sequence so the first column
        S[0].append(g*j)
        T[0].append(3)
    for i in range(1, len(seq1)+1):
        ## Repeat the same for the second sequence 
        S.append([g*i])
        T.append([2])
    for i in range(0, len(seq1)):
        for j in range(len(seq2)):
            ## now we iterate through the whole list use score pos to provide the nts for that position and the scoring matrix for ATGC which is sm 
            s1 = S[i][j] + score_pos(seq1[i], seq2[j], sm, g)
            ## this adds the gap penalties for each of the positions
            s2 = S[i][j+1] + g
            s3 = S[i+1][j] + g
            ## After this we add the max value to the matrix 
            S[i+1].append(max(s1,s2,s3))
            ## and we add which one gave the max value using the below function
            T[i+1].append(max3t(s1, s2,s3))
    return (S,T)
# function for max3t 
def max3t (v1,v2,v3):
    if max(v1,v2,v3) == v1: return 1
    if max(v1,v2,v3) == v2: return 2
    if max(v1,v2,v3) == v3: return 3

#recovering the alignment of the DNA sequences with the help of T matrix 
def recover_alignment (T,seq1,seq2):
    """ We use the top down approach to recover the alignment using the max value and where it came from which is the T matrix"""
    res = ["",""]
    i = len(seq1)
    j = len(seq2)
    while i>0 or j>0:
        if T[i][j] == 1:
            ## if the value came from the 1st box then we add the matching value to the sequnce
            res[0] = seq1[i-1] + res[0]
            res[1] = seq2[j-1] + res[1]
            i-=1
            j-=1
        elif T[i][j] == 3:
            ## if its 3 then we add a gap to which ever the sequence has the gap
            res[0] = "-" + res[0]
            res[1] = seq2[j-1] + res[1]
            j -= 1
        else:
            ## same as above
            res[0] = seq1[i-1] + res[0]
            res[1] = "-" + res[1]
            i -= 1
    return res

import sys                
def test_global ():
    sm  = create_submat(1, 0, "ACGT")
    seq1 = "ACGTCGAT"
    seq2 = "ACGCGTCGA"
    g = int(-2)
    res =needleman_Wunsch(seq1, seq2, sm, g)
    (S,T) = needleman_Wunsch (seq1, seq2, sm , g)
    alignment = recover_alignment (T, seq1, seq2)
    print(alignment[0])
    print(alignment[1])
    #print(S)
if __name__ == "__main__":
    test_global()
   

