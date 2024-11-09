# Problem
# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

# Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25.

# Given
# Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return
# The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Probabilidades de que a prole tenha pelo menos um alelo dominante

P_Aa_Aa = 3/4
P_Aa_aa = 1/2
P_aa_aa = 0

from itertools import combinations_with_replacement

def open_file(path):
    with open(path, "r") as f:
        return f.read()
    
def convert_int(file):
    s = file.split()
    return [int(x) for x in s]

def conditional_probability(p1, p2):
    if p1 == "AA" and p2 == "AA":
        return 1
    elif (p1 == "AA" and p2 == "Aa") or (p1 == "Aa" and p2 == "AA"):
        return 1
    elif (p1 == "AA" and p2 == "aa") or (p1 == "aa" and p2 == "AA"):
        return 1
    elif p1 == "Aa" and p2 == "Aa":
        return 3/4
    elif (p1 == "Aa" and p2 == "aa") or (p1 == "aa" and p2 == "Aa"):
        return 1/2
    elif p1 == "aa" and p2 == "aa":
        return 0
    
def selection_probability(p1, p2, total, prob_p):
    if p1 == p2:
        return (prob_p[p1] / total) * ((prob_p[p1] - 1) / (total- 1))
    else:
        return ((prob_p[p1] / total) * (prob_p[p2] / (total - 1))) + ((prob_p[p2] / total) * (prob_p[p1] / (total - 1)))

def probability(path):
    s = convert_int(path)
    
    k, m, n = s
    total = sum(s)
    prob_p = {'AA': k, 'Aa': m, 'aa': n}
    probability = 0

    for p1, p2 in combinations_with_replacement(['AA', 'Aa', 'aa'], 2):
        probability += selection_probability(p1, p2, total, prob_p) * conditional_probability(p1, p2)
   
    print(f"{probability:.5f}")
    
path = "src/IPRB/rosalind_iprb.txt"
probability(open_file(path))