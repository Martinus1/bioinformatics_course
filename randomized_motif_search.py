# import the random package here
import random


# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs_Quizz():
    # place your code here.
    randomMotifs = []

    randomMotifs.append("CCA")
    randomMotifs.append("CCT")
    randomMotifs.append("CTT")
    randomMotifs.append("TTG")

    return randomMotifs


# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch_Quizz(Dna, k, t):
    # insert your code here

    M = RandomMotifs_Quizz(Dna, k, t)
    BestMotifs = M

    Profile = ProfileWithPseudocounts(M)
    M = Motifs(Profile, Dna)
    print(M)

    print(Score(M))
    print(Score(BestMotifs))

    return


import sys

# 3. Assume we are given the following strings Dna:
DNA1 = "AAGCCAAA"
DNA2 = "AATCCTGG"
DNA3 = "GCTACTTG"
DNA4 = "ATGTTTTG"

Dna = [DNA1, DNA2, DNA3, DNA4]

# Then, assume that RandomizedMotifSearch begins by randomly choosing the following 3-mers Motifs of Dna:
"""
CCA
CCT
CTT
TTG
"""

# What are the 3-mers after one iteration of RandomizedMotifSearch?
# In other words, what are the 3-mers Motifs(Profile(Motifs), Dna)?
# Please enter your answer as four space-separated strings.


# set t equal to the number of strings in Dna and k equal to 3
k = 3
t = 4
RandomizedMotifSearch_Quizz(Dna, k, t)