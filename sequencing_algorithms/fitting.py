#!/usr/bin/env python3 
import needman as nm

def fitting (seq1, seq2, sm, g):
    S = [[0]]
    T = [[0]]
    for j in range(1, len(seq2)+1):
        S[0].append(g*j)
        T[0].append(3)
    for i in range(1, len(seq1)+1): 
        S.append([0])
        T.append([2])
    for i in range(0, len(seq1)):
        for j in range(0, len(seq2)):
            s1 = S[i][j] + nm.score_pos (seq1[i], seq2[j], sm,g);
            s2 = S[i][j+1] + g
            s3 = S[i+1][j] + g
            S[i+1].append(max(s1,s2,s3))
            T[i+1].append(nm.max3t(s1,s2,s3))
    return (S,T) 

def max_mat(S,seq1,seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    maxrow = int(-2)
    for i in range(0,len1-1):
        if S[i][len2]>maxrow:
            maxrow = S[i][len2]
            imax = i 
    maxcol = len2
    return (imax, maxcol)

def alignment_recovery(S,T,seq1, seq2,imax,maxcol):
    res = ["",""]
    i = len(seq1)
    j = len(seq2)
    #print(S[imax][maxcol])
    while T[i][j]>0:
        if i>imax:
            res[0] = seq1[i-1] + res[0]
            res[1] = "-" + res[1]
            i -= 1
        else:

            if T[i][j] == 1:
            #if diagonal
                res[0] = seq1[i-1] + res[0]
                res[1] = seq2[j-1] + res[1]
                i -= 1
                j -= 1
            elif T[i][j] == 3:
                # if horizontal
                res[0] = "-" + res[0]
                res[1] = seq2[j-1] + res[1]
                j -= 1 
            else:
                # if vertical
                res[0] = seq1[i-1] + res[0]
                res[1] = "-" + res[1]
                i -= 1

    return res
def test_fitting():
    sm = nm.create_submat(1,0,"ACGT")
    #seq1 = "ACGTCGACGC"
    seq1 = "GAGTGGCACGAT"
    seq2 = "CAC"
    g = int(-2)
    res = fitting(seq1, seq2, sm, g) 
    (S,T) = fitting(seq1, seq2, sm,g)
    #mat = S
    #mat1 = T
    #nm.print_mat(mat1)
    #nm.print_mat(mat)
    (imax,maxcol) = max_mat(S,seq1,seq2)
    #print(maxrow)
    #print(maxcol)
    alignment = alignment_recovery(S, T, seq1, seq2,imax,maxcol)
    #print(S)
    print(alignment[0])
    print(alignment[1])
test_fitting()
