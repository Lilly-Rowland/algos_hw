import java.util.Scanner;

public class MaxRectangle {

    static int largest_rectangle(int[] heights, int n){
        
        //initialize left and right arrays
        int[] left = new int[n];
        int[] right = new int[n];

        //create the stack from scratch
        int[] stack = new int[n];
        int top = -1; //top of the stack

        //get nearest smallest left = NSL
        for (int i = 0; i<n; i++){
            //pop from the stack while the current bar <=
            while (top >= 0 && heights[stack[top]] >= heights[i]){
                top--;
            }

            //if the stack is empty, then there are no smaller elements
            if (top < 0) left[i] = -1;
            else left[i] = stack[top];

            //add current index to the stack

            stack[++top] = i;
        }
        //clear stack
        top = -1;

        //Find nearest smallest right = NSR
        for (int i = n-1; i>=0; i--){

            //pop off (slay!!) while current bar is <=
            while (top>=0 && heights[stack[top]] >= heights[i]){
                top--;
            }

            //if the top is -1, stack is empty and NSR is right most bar =n
            if (top <0) right[i] = n;
            else right[i] = stack[top];

            stack[++top] = i; //addcurrent idx to the stack
        }

        //get the max area!!
        int max_area = 0;
        for (int i = 0; i<n; i++){
            //width is the distance between nsl and nsr while height is current height = y val
            int width = right[i] - left[i] -1;
            int height = heights[i];
            int area = width * height;
            if (area > max_area) max_area = area; //update max are if needed s
        }

        return max_area;

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

        //format into heights
        int minX = xs[0];
        int maxX = xs[n-1];
        int[] heights = new int[maxX - minX]; //lenth of heights = range of x values

        //set up hieghts where it is array giving heights of each x value in range to make shape
        for (int i = 1; i < n; i++){
            int x2 = xs[i];
            int y2 = ys[i];
            int x1 = xs[i-1];
            int y1 = ys[i-1];

            //if they are the same t vlaue, update the next bar height
            if (y1==y2){
                for (int j = x1; j < x2; j++){
                    heights[j - minX] = y1; //upfate bar height, make sure it us offset with minx in case first x isnt 0
                }
            }
        }
        
        int max_area = largest_rectangle(heights, heights.length);

        System.out.println(max_area);

    }


}
