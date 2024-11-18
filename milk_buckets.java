import java.util.ArrayList;
import java.util.Scanner;

class Cow {
    int m, i;

    public Cow(int m, int i) {
        this.m = m;
        this.i = i;
    }
}

public class milk_buckets {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] cows = new int[n];
        for (int i = 0; i < n; i++) {
            cows[i] = sc.nextInt();
        }

        // 1. rotate the list so the smallest element is last
        cows = rotate(cows, findMinIndex(cows) + 1);

        // 5. sum the milk at the start
        int milkSum = sumArray(cows);

        ArrayList<Cow> shortest = new ArrayList<>();
        shortest.add(new Cow(cows[n - 1], n - 1));

        int[] dm = new int[n + 1];

        // 2. Go backwards through the list, similar to binary search logic
        for (int i = n - 2; i >= 0; i--) {
            Cow cc = new Cow(cows[i], i);

            if (cc.m > shortest.get(shortest.size() - 1).m) {
                shortest.add(cc);
            } else if (cc.m < shortest.get(shortest.size() - 1).m) {
                while (shortest.size() > 0 && cc.m < shortest.get(shortest.size() - 1).m) {
                    shortest.remove(shortest.size() - 1);
                }
                shortest.add(cc);
            } else {
                shortest.get(shortest.size() - 1).i = i;
            }

            // 6. Calculate delta milk at the correct index
            int current = cows[i];
            int si = i;
            for (int z = shortest.size() - 1; z >= 0; z--) {
                Cow zCow = shortest.get(z);
                dm[zCow.i - si] += zCow.m - current;
                current = zCow.m;
            }
        }

        // 7. Calculate and print the final milk sums
        for (int e = 1; e < n; e++) {
            milkSum += dm[e];
            System.out.println(milkSum);
        }

        System.out.println(milkSum);

        sc.close();
    }

    // 1. Rotate the array
    public static int[] rotate(int[] arr, int n) {
        int[] rotated = new int[arr.length];
        int index = 0;
        for (int i = n; i < arr.length; i++, index++) {
            rotated[index] = arr[i];
        }
        for (int i = 0; i < n; i++, index++) {
            rotated[index] = arr[i];
        }
        return rotated;
    }

    // Find index of the minimum element in the array
    public static int findMinIndex(int[] arr) {
        int minIndex = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }
        return minIndex;
    }

    // Sum the elements of the array
    public static int sumArray(int[] arr) {
        int sum = 0;
        for (int value : arr) {
            sum += value;
        }
        return sum;
    }
}
