// dp[i][j][0] : i번 숫자까지 고려했을 때, j 개의 구간을 선택했을 때, i번 숫자가 마지막 그룹에 포함되지 않을 때, 최대 값
// dp[i][j][1] : i번 숫자까지 고려했을 때, j 개의 구간을 선택했을 때, i번 숫자가 마지막 그룹에 포함될 때, 최대 값
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }
        int[][][] dp = new int[n+1][m+1][2];
        // -1로 초기화
        for (int i=0; i<=n; i++){
            for (int j=0; j<=m; j++){
                dp[i][j][0] = -Integer.MAX_VALUE;
                dp[i][j][1] = -Integer.MAX_VALUE;
            }
        }

        // 구간 0개 선택은 모두 0으로 초기화
        for (int i=0; i<=n; i++){
            dp[i][0][0] = 0;
        }
        dp[1][1][1] = arr[1];

        for (int i=1; i<n; i++){
            for (int j=0; j<=m; j++){
                if (dp[i][j][0] != -Integer.MAX_VALUE){
                    // 다음 숫자를 새로운 그룹의 시작으로 추가하는 경우
                    // 그룹 수 증가
                    if (j+1 <= m){
                        dp[i+1][j+1][1] = Math.max(dp[i+1][j+1][1], dp[i][j][0] + arr[i+1]);
                    }
                    // 다음 숫자를 추가하지 않는 경우 
                    // 그룹 수 그대로
                    dp[i+1][j][0] = Math.max(dp[i+1][j][0], dp[i][j][0]);
                }
                if (dp[i][j][1] != -Integer.MAX_VALUE){
                    // 다음 숫자를 마지막 그룹의 끝에 추가하는 경우
                    // 그룹 수는 그대로
                    dp[i+1][j][1] = Math.max(dp[i+1][j][1], dp[i][j][1] + arr[i+1]);
                    // 다음 숫자를 추가하지 않는 경우 
                    // 그룹 수 그대로
                    dp[i+1][j][0] = Math.max(dp[i+1][j][0], dp[i][j][1]);
                }
            }
        }
        System.out.println(Math.max(dp[n][m][0], dp[n][m][1]));
    }
}