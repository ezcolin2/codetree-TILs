import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        
        // dp 정의
        // dp[i][j] = i번째까지 고려했을 때, 서로의 차이가 j인것이 가능하면 1, 아니면 0
        int[][] dp = new int[n+1][100001];

        // i가 1일 때 초기화
        dp[1][arr[0]] = 1;

        // 시작
        for(int i=1; i<n; i++){
            for (int j=0; j<=100000; j++){
                // 불가능하면 스킵
                if (dp[i][j] == 0){
                    continue;
                }
                dp[i+1][Math.abs(j-arr[i])] = dp[i][j];
                dp[i+1][j+arr[i]] = dp[i][j];
            }
        }

        // 가능한 경우 판단
        System.out.println(dp[n][0] == 1 ? "Yes" : "No");

    }
}