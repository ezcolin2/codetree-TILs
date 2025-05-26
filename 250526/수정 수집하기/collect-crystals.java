// dp[i][j][k]  : 최대 수정 개수
// i : 현재까지 고려한 수정 번호
// j : 현재 위치 0이면 L, 1이면 R
// k : 이동 횟수 
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        String s = sc.next();

        // L은 0으로, R은 1로 변환
        int[] locations = new int[s.length()+1];
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == 'L'){
                locations[i+1] = 0;
            }
            else{
                locations[i+1] = 1;
            }
        }
        int[][][] dp = new int[N+1][2][K+1];
        for (int i=0; i<=N; i++){
            for (int j=0; j<2; j++){
                for (int k=0; k<=K; k++){
                    dp[i][j][k] = -1;
                }
            }
        }
        // 처음에 왼쪽에서 수정 생성
        if (locations[1] == 0){
            dp[1][0][0] = 1; // 왼쪽에 있으면 수정 획득 O
            dp[1][1][1] = 0; // 이동해서 오른쪽에 있으면 수정 획득 X
        } else{
            dp[1][0][0] = 0;
            dp[1][1][1] = 1;
        }

        // dp 시작
        for (int i=1; i<N; i++){
            for (int j=0; j<2; j++){
                for (int k=0; k<=K; k++){
                    // 불가능한 경우는 스킵
                    if (dp[i][j][k] == -1){
                        continue;
                    }
                    // 이동하지 않았을 때
                    dp[i+1][j][k] = Math.max(dp[i+1][j][k], dp[i][j][k] + (j==locations[i+1] ? 1 : 0));
                    // 이동했을 때
                    if (k+1 <= K){
                        dp[i+1][(j+1)%2][k+1] = Math.max(dp[i+1][(j+1)%2][k+1], dp[i][j][k] + ((j+1)%2==locations[i+1] ? 1 : 0));
                    }
                }
            }
        }
        int res = 0;
        for (int i=0; i<2; i++){
            for (int j=0; j<=K; j++){
                if (dp[N][i][j] == -1){
                    continue;
                }
                res = Math.max(res, dp[N][i][j]);
            }
        }
        System.out.println(res);
    }
}