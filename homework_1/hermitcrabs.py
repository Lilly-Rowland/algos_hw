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
    if n<=1: # base case, it is length of 1
        return values
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
            shells.insert(s, crabs[c]) #add new emptied shell to the list
            # shells = shells[:-1] # dont need to actually pop of the last shell since moving pointer works for this
            c -= 1 #go to next smaller crab
            # shell pointer is now pointing to the shell that was just emptied
        else:
            # shell too small--> try next shell
            s -= 1

    print("YES" if c == 0 else "NO")

if __name__ == "__main__":
    main()


    #need to add leftshell back to the list