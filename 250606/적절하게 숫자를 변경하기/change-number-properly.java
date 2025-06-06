// dp[i][j][k] : i번째까지 고려했을 때, i번째 숫자가 j일 때, 인접한 두 숫자가 다른 횟수가 k일 때, 가장 높은 유사ㄷ
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int IMPOSSIBLE_STATE = -1;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] seq = new int[N+1];
        for (int i = 1; i <= N; i++) {
            seq[i] = sc.nextInt();
        }

        int[][][] dp = new int[N+1][5][M+1];

        // 우선 전부 -1로 초기화
        for (int i=0; i<=N; i++){
            for (int j=0; j<5; j++){
                for (int k=0; k<=M; k++){
                    dp[i][j][k] = IMPOSSIBLE_STATE;
                }
            }
        }

        // 첫 번째 초기화
        for (int i=1; i<=4; i++){
            // 만약 seq와 똑같다면
            if (seq[1] == i){
                dp[1][i][0] = 1;
            } else{
                dp[1][i][0] = 0;
            }
            
        }

        // 시작
        for (int i=1; i<N; i++){
            for (int j=1; j<=4; j++){
                for (int k=0; k<=M; k++){
                    // 만약 불가능한 경우라면 스킵
                    if (dp[i][j][k] == IMPOSSIBLE_STATE){
                        continue;
                    }
                    // i+1에 넣을 숫자 선택하기
                    for (int p=1; p<=4; p++){
                        // 만약 이전 것(j)와 같다면? (k 그대로)
                        if (j==p){
                            // 만약 seq[i+1]과 p가 같다면? (유사도 증가)
                            if (seq[i+1] == p){
                                dp[i+1][p][k] = Math.max(dp[i+1][p][k], dp[i][j][k]+1);
                            }
                            // 다르다면? 유사도 그대로
                            else{
                                dp[i+1][p][k] = Math.max(dp[i+1][p][k], dp[i][j][k]);
                            }
                        }
                        // 다르다면? (k 증가)
                        else{
                            // 만약 seq[i+1]과 p가 같다면? (유사도 증가)
                            if (seq[i+1] == p && k+1 <= M){
                                dp[i+1][p][k+1] = Math.max(dp[i+1][p][k+1], dp[i][j][k]+1);
                            }
                            // 다르다면? 유사도 그대로
                            else if (k+1 <= M){
                                dp[i+1][p][k+1] = Math.max(dp[i+1][p][k+1], dp[i][j][k]);
                            }
                        }
                    }
                }
            }
        }

        // 순회하면서 인접한 두 숫자가 다른 횟수가 M번이하인 것들 중 유사도가 가장 높은 것 구하기
        int res = 0;
        for (int i=1; i<=4; i++){
            for (int j=0; j<=M; j++){
                res = Math.max(res, dp[N][i][j]);
            }
        }
        System.out.println(res);
    }
}