// dp로 해결
// dp[i][j] : i번째 폭탄까지 고려했을 때, j개 폭탄을 해제했을 때 점수 최대 값
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Bomb[] bombs = new Bomb[n+1];
        bombs[0] = new Bomb(-1, -1);
        for (int i = 1; i <= n; i++) {
            bombs[i] = new Bomb(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(bombs);

        int[][] dp = new int[n+1][n+1];
        // dp 초기화 
        for (int i=0; i<=n; i++){
            for (int j=0; j<=n; j++){
                dp[i][j] = -1;
            }
        }

        // 0번째까지 선택한 것은 무조건 0
        for (int i=0; i<n; i++){
            dp[0][i] = 0;
        }
        for (int i=1; i<=n; i++){
            for (int j=1; j<=i; j++){

                // i번째를 선택하는 경우
                // dp[i-1][j-1]이 가능한 경우이면서 시간이 지나지 않은 상태여야 함
                if (dp[i-1][j-1] != -1 && bombs[i].time >= j){
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + bombs[i].score);
                }

                // i번째를 선택하지 않는 경우
                if (dp[i-1][j] != -1){
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                }
            }
        }
        int res = 0;
        for (int i=0; i<=n; i++){
            res = Math.max(res, dp[n][i]);
        }
        System.out.println(res);
    }
}
class Bomb implements Comparable<Bomb>{
    int score;
    int time;
    public Bomb(int score, int time){
        this.score = score;
        this.time = time;
    }
    @Override
    public int compareTo(Bomb bomb){
        if (this.time == bomb.time){
            return Integer.compare(bomb.score, this.score);
        }
        return Integer.compare(this.time, bomb.time);
    }
}