#program to find permutations of a given string

from itertools import permutations

# def functions
def allPermutations (str):

    #get allpermmutations of str
    permlist = permutations(str)

    #print all permuatations
    for perm in list (permlist):
        print(''. join(perm))

#driver code
if __name__ == "__main__":
    str = "NMIMS"
    allPermutations(str)