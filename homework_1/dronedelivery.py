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

    #get the number of routes as n
    n = int(input().strip())

    #get the routes and save to list
    route_input = input().split()
    distances = []
    A = []

    for i in range(n):
        A.append(float(route_input[i]))

    B = A

    for a in A:
        for b in B:
            distances.append(a+b)

    sorted_distances = mergesort(distances, n**2)

    unique_distances = 1
    for i in range(1, n**2):
        if sorted_distances[i] != sorted_distances[i-1]:
            unique_distances += 1
    
    print(unique_distances)


if __name__ == "__main__":
    main()