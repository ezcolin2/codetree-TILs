import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] coin = new int[n];
        for (int i = 0; i < n; i++)
            coin[i] = sc.nextInt();
        int[] dp = new int[100001];
        for (int i=0; i<=m; i++){
            dp[i] = Integer.MAX_VALUE;
        }
        for (int i=0; i<n; i++){
            dp[coin[i]] = 1;
        }
        for (int i=1; i<=m; i++){
            for (int j=0; j<n; j++){
                if (i-coin[j] > 0 && dp[i-coin[j]] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i-coin[j]]+1);
                }
                
            }
            

        }
        System.out.println(dp[m] == Integer.MAX_VALUE ? -1 :dp[m]);
    }
}