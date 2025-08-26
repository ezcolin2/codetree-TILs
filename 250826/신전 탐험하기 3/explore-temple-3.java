import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] board = new int[n][m];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // dp[i][j]: i층에서 j번째 방에 들어갔을 때 획득 가능 최대 보물
        int[][] dp = new int[n][m];
        for (int i=0; i<m; i++){
            dp[0][i] = board[0][i];
        }
        // 시작
        for (int i=0; i<n-1; i++){
            for (int j=0; j<m; j++){
                if (dp[i][j] == 0){
                    continue;
                }
                for (int k=0; k<m; k++){
                    if(j==k){
                        continue;
                    }
                    dp[i+1][k] = Math.max(dp[i+1][k], dp[i][j]+board[i+1][k]);
                }
            }
        }
        int res = 0;
        for (int i=0; i<m; i++){
            res = Math.max(res, dp[n-1][i]);
        }
        bw.write(String.valueOf(res));
        bw.close();
    }
}