// dp[i][j][k] : i번째까지 고려했을 때, T가 j번 나오고 B가 연속 k번 나왔을 때, 경우의 수
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][][] dp = new int[n+1][3][3];
        // 초기화
        dp[1][0][0] = 1; // G
        dp[1][1][0] = 1; // T
        dp[1][0][1] = 1; // B

        // dp 시작
        for (int i=1; i<n; i++){
            for (int j=0; j<=2; j++){
                for (int k=0; k<=2; k++){
                    // G 받음
                    // T 그대로
                    // B 끊김
                    dp[i+1][j][0] += dp[i][j][k];
                    dp[i+1][j][0]%=1000000007;
                    // T 받음
                    // G 그대로
                    // B 끊김
                    if (j<2){
                        dp[i+1][j+1][0] += dp[i][j][k]%1000000007;
                        dp[i+1][j+1][0]%=1000000007;
                    }
                    
                    // B 받음
                    // T 그대로
                    // G 그대로
                    if (k<2){
                        dp[i+1][j][k+1] += dp[i][j][k]%1000000007;
                        dp[i+1][j][k+1]%=1000000007;
                    }
                    
                }
            }
        }
        int res = 0;
        for (int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                res += dp[n][i][j];
                res%=1000000007;
            }
        }
        System.out.println(res);
    }
}