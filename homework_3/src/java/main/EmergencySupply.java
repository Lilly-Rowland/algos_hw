import java.util.Scanner;

public class EmergencySupply {

    static void insertion_sort(int[] arr, int lo, int hi) {
        for (int i = lo + 1; i <= hi; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= lo && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static int median(int[] arr, int start, int end, int k){
        int N = end - start + 1;
        
        if (N <= 5){
            insertion_sort(arr, start, end);
            //get middle index
            return arr[start+k];
        }

        // partition into subsets of 5 elements each
        // get median for each group of 5 an dbuild median array
        int num_groups = (N+4) / 5; //this gets ceiling(n/5)
        int[] medians = new int[num_groups];

        int i = 0;
        for (int gStart = start; gStart <= end; gStart += 5) {
            int gEnd = Math.min(gStart + 4, end);
            insertion_sort(arr, gStart, gEnd);
            int medIndex = gStart + (gEnd - gStart) / 2;
            medians[i++] = arr[medIndex];
        }

        //get the pivot
        int pivot = median(medians, 0, medians.length-1, medians.length/2);
        
        // first pass to get the sizes
        int llen=0; int elen=0; int glen = 0;

        for (i = start; i <=end; i++){
            int val = arr[i];
            if (val < pivot) llen++;
            else if (val > pivot) glen++;
            else elen++;
        }

        //Make new arrays
        int[] L = new int[llen];
        int[] E = new int[elen];
        int[] G = new int[glen];

        //get the arrays
        int li=0; int ei=0; int gi =0;

        for (i = start; i <=end; i++){
            int val = arr[i];
            if (val < pivot) L[li++] = val;
            else if (val > pivot) G[gi++] = val;
            else E[ei++] = val;
        }

        //recusion depends on what k
        if (k < llen) return median(L, 0, llen-1, k);
        else if (k < llen+elen) return pivot;
        else return median(G, 0,glen-1, k-llen-elen);

    }
    public static void main(String[] args) {
        //scan in the inputs!
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }
        sc.close();
        
        int x = median(xs, 0, n-1, n/2);
        int y = median(ys, 0, n-1, n/2);

        System.out.println(x + ", " + y); //print(x,y)

    }
}
