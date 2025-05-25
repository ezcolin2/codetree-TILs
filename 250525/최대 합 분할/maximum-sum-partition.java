// dp[i][j] : i번째 수까지 확인했을 때, (A 그룹 합) - (B 그룹 합)이 j인 것이 가능할 때, (A 그룹 합) + (B 그룹 합)
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n+1];
        for(int i = 1; i <= n; i++){
            arr[i] = sc.nextInt();
        }
        int[][] dp = new int[n+1][200001];
        for (int i=0; i<=n; i++){
            for (int j=0; j<=200000; j++){
                dp[i][j] = -1;
            }
        }
        dp[1][100000-arr[1]] = arr[1]; // B 그룹 선택
        dp[1][100000+arr[1]] = arr[1]; // A 그룹 선택
        dp[1][100000] = 0; // C 그룹 선택
        for (int i=1; i<n; i++){
            for (int j=0; j<=200000; j++){
                if (dp[i][j] == -1){
                    continue;
                }
                // B 그룹 선택
                if (j-arr[i+1] >= 0){
                    dp[i+1][j-arr[i+1]] = Math.max(dp[i+1][j-arr[i+1]], dp[i][j]+arr[i+1]);
                }
                // A 그룹 선택
                if (j+arr[i+1] <= 200000){
                    dp[i+1][j+arr[i+1]] = Math.max(dp[i+1][j+arr[i+1]], dp[i][j]+arr[i+1]);
                }
                // C 그룹 선택
                dp[i+1][j] = Math.max(dp[i+1][j], dp[i][j]);
            }
        }
        System.out.println(dp[n][100000]/2);
    }
}