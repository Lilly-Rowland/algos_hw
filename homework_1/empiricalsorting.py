import numpy as np
import time
import math
import matplotlib.pyplot as plt

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

def insertionsort(values, n):
    # running in O(n^2) time
    start_time = time.perf_counter() # setting up timer to catch if it times out
    for i in range(n): 
        if i%1000 != 0: # check time at every 1000 values
            current_time = time.perf_counter()
            if current_time - start_time > 120: # if it has been going for more than 120 seocnds, time out
                return False
        val = values[i] # get the current value being looked at to be sorted in
        j = i - 1 # start at value directly left of current value
        # loop throgh elements from 0 to i-1
        while(values[j] >= val and j >= 0):
            # if the left value is greater then the right value, swap with vals position
            values[j + 1] = values[j]
            values[j] = val # swap it with j
            j -= 1 # decrease j
    return values

def bucketsort(values, n):
    start_time = time.perf_counter()
    buckets = [[] for _ in range(n)] # [[], [], []...] list of n lists
    bucket_lengths = [0]*n # get list of nbucekts lengths to use for insertion sort later

    # disrtubut values into the diff n buckets
    for val in values:
        bi = int(val*n) #math.floor(val*n)
        buckets[bi].append(val)
        bucket_lengths[bi] += 1 
    
    for i, bucket in enumerate(buckets):
        if i%1000 == 0: # check time at every 1000 values
            current_time = time.perf_counter()
            if current_time - start_time > 120: # if it has been going for more than 120 seocnds, time out
                return False
        insertionsort(bucket, bucket_lengths[i])

    concat_list = [val for bucket in buckets for val in bucket]
    return concat_list


def plot_data(time_data, sizes):

    plt.figure(figsize=(9,6))
    
    #unform is a solid line, gaussian is a dashed line
    # merge sort = blue
    plt.plot(sizes, time_data[0,:,0], '-', marker='o', color='blue', label='MergeSort') #uniform, all sizes, mergesort
    plt.plot(sizes, time_data[1,:,0], '--', marker='o', color='blue') #gaussian, all sizes, mergesort

    # InsertionSort = green
    plt.plot(sizes, time_data[0,:,1], '-', marker='o', color='green', label='InsertionSort') #uniform, all sizes, insertion
    plt.plot(sizes, time_data[1,:,1], '--', marker='o', color='green') #gaussian, all sizes, insertionsort

    # Bucketsort = red
    plt.plot(sizes, time_data[0,:,2], '-', marker='o', color='red', label='BucketSort') #uniform, all sizes, bucketsort
    plt.plot(sizes, time_data[1,:,2], '--', marker='o', color='red') #gaussian, all sizes, bucketsort

    # show it in log scale. 
    plt.xscale('log')
    plt.yscale('log')

    # setting up lablels
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Runtime vs n")

    # Main legend is for algorithms
    plt.legend(title="Algorithm")

    # legend for line styles
    plt.text(0.2, .9,
             "Solid = Uniform\nDashed = Gaussian",
             transform=plt.gca().transAxes, 
             fontweight='bold',
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="black"))

    plt.tight_layout()
    plt.savefig("sorting_plot.png")
    plt.show()
    




def main():

    # how data will be stored for plotting 
    size_names = ['n=100', 'n=1000', 'n=10000', 'n=100000'] # The "third dimension"
    distribution_names = ['Uniform', 'Gaussian'] # Row names
    sort_names = ['MergeSort', 'InsertionSort', 'BucketSort']
    input_data = np.empty((2, 4), dtype=object)

    sizes = [100, 1000, 10000, 100000]
    # sizes = [5,10,15,20]
    for i in range(len(sizes)):
        n = sizes[i]
        # samples = np.random.rand(n)
        input_data[0, i] = np.random.uniform(0, 1, n)  # uniform, size
        # if i set the scale to soemthing lower like 0.00001 then it looks more like what
        # is expected with gaussian distribtion (closer to insertion sort)
        gauss = np.random.normal(loc=0.5, scale=0.01, size=n) #gaussian
        gauss = np.clip(gauss, 0, 1)
        input_data[1, i] = gauss
    # shape of time data is uniform, sizes, sorting_type
    time_data = np.full((2,4,3), np.nan)
    for i in range(input_data.shape[0]): #gaussian or uniform?
        for j in range(input_data.shape[1]): #what size?
            n = sizes[j]
            values = input_data[i, j]
            
            # time the merge sort
            start_time = time.perf_counter()
            ms_out = mergesort(values.copy().tolist(), n)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            time_data[i, j, 0] = elapsed_time
            print(f"Mergesort with {size_names[j]} for {distribution_names[i]} took {elapsed_time:.2f} seconds")

            # time the insertionsort
            start_time = time.perf_counter()
            is_out = insertionsort(values.copy().tolist(), n)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            time_data[i, j, 1] = elapsed_time
            print(f"Insertionsort with {size_names[j]} for {distribution_names[i]} took {elapsed_time:.2f} seconds")

            #time the bucket sort
            start_time = time.perf_counter()
            bs_out = bucketsort(values.copy().tolist(), n)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            time_data[i, j, 2] = elapsed_time
            print(f"Bucketsort with {size_names[j]} for {distribution_names[i]} took {elapsed_time:.2f} seconds")
    # plot the results
    plot_data(time_data, sizes)


if __name__ == "__main__":
    main()