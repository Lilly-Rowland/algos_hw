import java.util.Arrays;
import java.util.Scanner;

public class WeightedInversions {
    static class Output {
        int sum;
        int[] array;
        
        Output(int sum, int[] array){
            this.sum = sum;
            this.array = array;
        }
    }
    
    static int[] getEndSums(int[] arr){
        //building the suffix array
        int[] inv_sums = new int [arr.length];
        int N = arr.length - 1;

        inv_sums[N] = arr[N];
        N--;

        for (int i = N; i>=0; i--){
            inv_sums[i] = arr[i] + inv_sums[i+1]; //add current val and everything after it
            //access time for these sums is O(1) for later
        }
        return inv_sums;
        
    }

    static Output mergeAndCount(Output left, Output right){
        //building the suffix array
        int[] L = left.array;
        int[] R = right.array;

        int[] left_sums = getEndSums(left.array);
        int[] merged = new int[L.length + R.length];
        int i = 0, j = 0, k, total= 0;

        for (k = 0; k<merged.length && i < L.length && j < R.length; k++){
            if (L[i] <= R[j]){
                merged[k] = L[i];
                i++;
            }
            else {
                //it is an inversion!!!
                merged[k] = R[j];

                total += R[j] * (L.length - i);
                total += left_sums[i];
                j++;
            }
        }
        //copy remaining like in merge of mergsort
        while (i < L.length) {
            merged[k++] = L[i++];
        }

        while (j < R.length) {
            merged[k++] = R[j++];
        }
        return new Output(total, merged);

    }

    static Output mergeSortCount(int[] array, int n) {
        //int n = values.length; //get length of values to sort
        if (n<=1) {
            return new Output(0, array);
        }
        int mid = n/2; //n is midle value
        //get the arrays to return in left and right
        int[] arr1  = Arrays.copyOfRange(array, 0, mid);
        int[] arr2 = Arrays.copyOfRange(array, mid, n);
        //recurse on left and right side
        Output left = mergeSortCount(arr1, mid);
        Output right = mergeSortCount(arr2, n-mid);
        Output merged = mergeAndCount(left, right);

        return new Output(left.sum + right.sum + merged.sum, merged.array);

    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //scan in length of the array
        int n = sc.nextInt();

        //scan in the actually array A
        int[] array = new int[n];
        for (int i = 0; i < n; i++) array[i] = sc.nextInt();

        Output output = mergeSortCount(array, n);

        //return output
        System.out.println(output.sum);
        sc.close();
    }
}
