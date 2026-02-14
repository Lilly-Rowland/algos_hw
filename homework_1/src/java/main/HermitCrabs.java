import java.util.Scanner;

/**
 * HermitCrabs.java
 * I had to write this in java because the python version was timing out for the last two, so
 * that is why this is in java and the rest of the assignments are in Python...
 */
public class HermitCrabs {

    /**
     * Merges the arrays together (mergesort heloer).
     *
     * @param arr1 first sorted array
     * @param arr2 second sorted array
     * @return cmerged array
     */
    static int[] merge(int[] arr1, int[] arr2) {

        //merged arr has length of the two combined
        int[] merged_arr = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0; //insitialize variuables

        //while neither arrays are empty
        while (i < arr1.length && j < arr2.length) {
            //if the element in first array is smaller, add that
            if (arr1[i] <= arr2[j]) merged_arr[k++] = arr1[i++];
            else merged_arr[k++] = arr2[j++]; //o.w. add the second array elemnt
        }
        
        //add the rest of the non-empty array to the merged_Array at the end
        while (i < arr1.length){ merged_arr[k++] = arr1[i++];}
        while (j < arr2.length) {merged_arr[k++] = arr2[j++];}

        return merged_arr;
    }

    /**
     * mergesort sorts and array in nlogn time
     *
     * @param values array to sort
     * @return sorted array
     */
    static int[] mergeSort(int[] values) {
        int n = values.length; //get length of values to sort

        //base case, if it is length 1 then return
        if (n <= 1) {
            return values;
        }

        //split it up
        int mid = n / 2;

        //get new array of proper lengths
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        // copy the first and seocnd half into the right array
        for (int i = 0; i < mid; i++) left[i] = values[i];
        for (int i = mid; i < n; i++) right[i - mid] = values[i];

        //call merge sort on each side
        left = mergeSort(left);
        right = mergeSort(right);

        //merger together
        return merge(left, right);
    }

    /**
     * main program for hermit crabs
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //scan in the number of crabs and shells
        int n = sc.nextInt();
        int m = sc.nextInt();

        //get the crabs list and sort it
        int[] crabs = new int[n];
        for (int i = 0; i < n; i++) crabs[i] = sc.nextInt();
        crabs = mergeSort(crabs);

        //get the shells list and sort it
        int[] shells = new int[m];
        for (int i = 0; i < m; i++) shells[i] = sc.nextInt();
        shells = mergeSort(shells);

        //get starting idx for each list
        int c = n - 1;
        int s = m - 1;

        //while not at the start of the array
        while (c > 0 && s > 0) { 
            //if shell is bigger
            if (shells[s] > crabs[c]) {
                // overwrite last element with the new shell
                shells[m - 1] = crabs[c];
                c--; //go to smaller crab
                // s stays the same because now pointing to next open shell
            } else {
                s--; //go to next shell sinice it doesnt fit :()
            }
        }

        //return output
        System.out.println(c == 0 ? "YES" : "NO");
        sc.close();
    }
}
