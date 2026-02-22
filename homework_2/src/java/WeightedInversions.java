import java.util.Scanner;

public class WeightedInversions {
    //needed to make in long so sum would work
    //getting the sum of everthing after current number
    static long[] getEndSums(int[] arr, int low, int mid){
        int len = mid - low + 1;
        
        //building the suffix array
        long[] inv_sums = new long [len];

        inv_sums[len - 1] = arr[mid];
        
        for (int i = len-2; i>=0; i--){
            inv_sums[i] = arr[low + i] + inv_sums[i+1]; //add current val and everything after it
            //access time for these sums is O(1) for later
        }
        return inv_sums;
        
    }

    static long mergeAndCount(int[] array, int[] temp, int low, int mid, int high){
        
        //o(n) to get the end sums in here
        long[] left_sums = getEndSums(array, low, mid);

        //building the end sums array
        int i = low;
        int j = mid + 1;
        int k = low;
        long total = 0;

        while (i <= mid && j <= high) {
            //there is no inversion
            if (array[i] <= array[j]) {
                temp[k++] = array[i++];
            } else {
                //tohere is an inversion!!!
                temp[k++] = array[j]; //swap for emrging

                int remaining = mid - i + 1;

                total += (long) array[j] * remaining; //get the remaining sum using long arithmetic
                total += left_sums[i - low]; //use left sums to get the total of other part

                j++;
            }
        }
        //copy remaining like in merge of mergsort
        while (i <= mid) {
            temp[k++] = array[i++];
        }

        while (j <= high) {
            temp[k++] = array[j++];
        }

        // copy merged segment back
        for (int t = low; t <= high; t++) {
            array[t] = temp[t];
        }
        return total;

    }

    static long mergeSortCount(int[] array, int[] temp, int low, int high) {
        if (low >= high) {
            return 0;
        }
        
        //int n = values.length; //get length of values to sort
        int mid = (low + high) / 2;

        //recurse! get left part, right part, and then sum between the two
        long leftSum = mergeSortCount(array, temp, low, mid);
        long rightSum = mergeSortCount(array, temp, mid + 1, high);
        long interSum = mergeAndCount(array, temp, low, mid, high);

        return leftSum + rightSum + interSum;

    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //scan in length of the array
        int n = sc.nextInt();
        int[] array = new int[n];
        int[] temp = new int[n];

        //scan in the actually array A
 
        for (int i = 0; i < n; i++) array[i] = sc.nextInt();


        long result = mergeSortCount(array, temp, 0, n - 1);

        //return output
        
        System.out.println(result);
        sc.close();
    }
}
