// dp[i][j] : i번째 퀘스트까지 고려했을 때, 퀘스트를 수행한 총 시간이 j일 때, 얻은 최고 경험치
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] exp = new int[n+1];
        int[] time = new int[n+1];
        for (int i = 1; i <= n; i++) {
            exp[i] = sc.nextInt();
            time[i] = sc.nextInt();
        }

        int[][] dp = new int[n+1][10001];
        // 초기화
        dp[0][0] = 0;
        for (int i=1; i<=10000; i++){
            dp[0][i] = -1;
        }

        // 처음부터 퀘스트 수행하기
        for (int i=0; i<n; i++){
            for (int j=0; j<=10000; j++){
                // 불가능한 건 스킵
                if (dp[i][j] == -1){
                    continue;
                }

                // i+1번째 퀘스트를 선택하는 경우
                int nextTime = j+time[i+1];
                if (nextTime <= 10000){
                    dp[i+1][nextTime] = Math.max(dp[i+1][nextTime] , dp[i][j] + exp[i+1]);
                }
                

                // i+1번째 퀘스트를 선택하지 않는 경우
                dp[i+1][j] = Math.max(dp[i+1][j], dp[i][j]);
            }
        }

        for (int i=0; i<=10000; i++){
            // 경험치가 M 이상인 것들 총 시간 최소
            if (dp[n][i] >= m){
                System.out.println(i);
                return;
            }
        }
        System.out.println(-1);
        
    }
}
