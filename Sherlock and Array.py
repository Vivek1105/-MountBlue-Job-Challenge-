def main(argv = None):
    if argv is None:
        argv = sys.argv

    T = int(input())

    for t in range(0, T):
        N = int(input())
        nums = list(map(int, input().split(" ")))

        found = 0

        pivot = 0
        left = 0
        right = reduce(lambda x, y: x+y, nums[pivot+1:N+1], 0)
        found = (left == right)

        while (not found) and (pivot < N-1):
            left = left + nums[pivot]
            right = right - nums[pivot+1]
            pivot = pivot + 1
            found = (left == right)
            if found:
                break

        if found:
            print("YES")
        else:
            print("NO")


# Invoking the program entry point
if __name__ == "__main__":
    sys.exit(main())
    
    
 JAVA CODE /
 
 import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution
{
    public static void main(String[] args)
    {
        final Scanner in = new Scanner(System.in);
        final int numberOfTests = in.nextInt();

        final List<Boolean> containWatsonSum = new ArrayList<>(numberOfTests);

        for (int i = 0; i < numberOfTests; i++)
        {
            final int numberOfArrayElements = in.nextInt();

            containWatsonSum.add(
                    containsWatsonSum(
                            IntStream
                                    .generate(in::nextInt)
                                    .limit(numberOfArrayElements)
                                    .toArray()));
        }

        containWatsonSum
                .stream()
                .map(contains -> contains ? "YES" : "NO")
                .forEach(System.out::println);
    }

    private static boolean containsWatsonSum(int[] array)
    {
        int leftSum = 0;
        int rightSum = IntStream.of(array).skip(1).sum();

        for (int i = 0; i < array.length - 1; i++)
        {
            if (leftSum == rightSum)
            {
                return true;
            }
            else
            {
                leftSum += array[i];
                rightSum -= array[i + 1];
            }
        }

        return leftSum == 0;

    }
}
