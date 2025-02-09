import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int INF = 100001;
        int n = Integer.parseInt(br.readLine());
        // dp 배열 생성
        int[] dp = new int[n+1];
        for (int i=0; i<=n; i++){
            dp[i] = INF;
        }
        if (n>=2){
            dp[2] = 1;
        }
        if (n>=5){
            dp[5] = 1;
        }


        // 시작 
        for (int i=2; i<=n; i++){
            // 만들 수 없으면 스킵
            if (dp[i] ==INF){
                continue;
            }

            if (i+2 <= n){
                dp[i+2] = Math.min(dp[i+2], dp[i]+1);
            }
            if (i+5 <= n){
                dp[i+5] = Math.min(dp[i+5], dp[i]+1);
            }
        }
        int res = dp[n];
        if (res == INF){
            res = -1;
        }
        bw.write(String.valueOf(res));
        bw.close();
    }
}