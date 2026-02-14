def insertionsort(values, n):
    # running in O(n^2) time
    for i in range(n): 
        val = values[i] # get the current value being looked at to be sorted in
        j = i - 1 # start at value directly left of current value
        # loop throgh elements from 0 to i-1
        while(values[j] >= val and j >= 0):
            # if the left value is greater then the right value, swap with vals position
            values[j + 1] = values[j]
            values[j] = val # swap it with j
            j -= 1 # decrease j
    return values

def merge(arr1, arr2):
    output = [] #output array is len(arr1) + len(arr2) size
    i, j, k = 0, 0, 0 # initialize variables
    while (i < len(arr1) and j < len(arr2)): #while one of the arrays is not empty
        
        # add first arrays smaller value
        if (arr1[i] <= arr2[j]):
            output.append(arr1[i])
            i += 1

        # add second arrays smaller value
        else:
            output.append(arr2[j])
            j += 1
        k += 1 # k is not actually needed to be incremented but in the pseudocode from the slides it was used, since list don;t need predefined size like array in java, it isnt needed
    
    #append the rest of the remaining array
    if i < len(arr1):
        output.extend(arr1[i:])
    elif j < len(arr2):
        output.extend(arr2[j:])
    return output


def mergesort(values, n):
    #trying insertion sort for slightly larger base case to speed things up to meet time limit
    if n<=20: # base case, it is length of 1
        return insertionsort(values, n)
    else:
        mid = n//2  # get middle index
        arr1 = mergesort(values[:mid], mid) # call merge sort on left
        arr2 = mergesort(values[mid:], n - mid) # call mergesort on right
        values = merge(arr1, arr2) # merge them back together
        return values
    

def main():

    # parse the input

    # Get first two integers n and m
    first = input().strip().split()
    n = int(first[0])
    m = int(first[1])

    # get n integers
    crabs = mergesort([int(x) for x in input().strip().split()], n) # get the crabs and sort them

    # m integers of empty shell sizes
    shells = mergesort([int(x) for x in input().strip().split()], m) #get the empty shells and sort them

    c = n - 1  # index for the largest crab to fit
    s = m - 1 # index the largest shell
    
    
    while c > 0 and s > 0: # while there are still crabs left to assign and possible shells to assign
        if shells[s] > crabs[c]: #if current shell is bigger than current crabs size
            # assign this shell to this crab
            shells.pop() # remove the shell just used
            shells.append(crabs[c]) # add the emptied shell to end
            c -= 1 # go to next smaller crab
            # s = len(shells) - 1 # point shell pointer to the last shell
        else:
            # shell too small--> try next shell
            s -= 1

    print("YES" if c == 0 else "NO")

if __name__ == "__main__":
    main()


    #need to add leftshell back to the list