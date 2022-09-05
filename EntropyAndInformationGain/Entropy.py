from math import log2 as log2

# function to calculate the Entropy for 2 classes
def Entropy(p1, p2):
    return [-p1 * log2(p1) - p2 * log2(p2)]
# works on list of probabilties
def multi_Entropy(P):
    E = 0
    for i in range(len(P)):
        E += -P[i] * log2(P[i])
    return E


'''
#test cases for our functions
print(Entropy(7/12, 5/12))
print(multi_Entropy([7/12, 5/12]))
'''
# a container for the Entropy of each class
EEE = []

# let's use them
p_species = [14/24, 10/24]
print("Entropy for Speacies : ", multi_Entropy(p_species))
EEE.append(multi_Entropy(p_species))
p_color = [10/24, 8/24, 6/24]
print("Entropy for colors : ", multi_Entropy(p_color))
EEE.append(multi_Entropy(p_color))
# length is a Continues data so can't be calculaed the same way
# so I divided them into periods
# period 1 = [11.6==>15.6] frequency = 7
# period 2 = [15.6==>19.6]   frequency = 9
# period 3 = [19.6==> 23.6]     frequency = 6
# period 4 = [23.6==> 27.6]        frequency = 2
p_length = [7/24, 9/24, 6/24, 2/24]
print("Entropy for Length : ", multi_Entropy(p_length))
EEE.append(multi_Entropy(p_length))
print(EEE)
#information gain
