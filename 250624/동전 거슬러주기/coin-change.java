import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] coin = new int[n];
        for (int i = 0; i < n; i++)
            coin[i] = sc.nextInt();
        int[] dp = new int[Math.max(6, m+1)];
        for (int i=0; i<=m; i++){
            dp[i] = Integer.MAX_VALUE;
        }
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        dp[4] = 1;
        dp[5] = 1;
        for (int i=6; i<=m; i++){
            dp[i] = Math.min(dp[i], dp[i-1]+1);
            dp[i] = Math.min(dp[i], dp[i-4]+1);
            dp[i] = Math.min(dp[i], dp[i-5]+1);
        }
        System.out.println(dp[m] == Integer.MAX_VALUE ? -1 :dp[m]);
    }
}