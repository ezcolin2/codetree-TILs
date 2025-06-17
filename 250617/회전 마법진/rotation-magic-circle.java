import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] currentState = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        int[] goalState = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        
        int MAX_VALUE = Integer.MAX_VALUE;
        // dp[i][j] : i번 마법진 맞췄는데 j번 반시계 회전할 때 최소한 회전 수
        int[][] dp = new int[n][10];
        for (int i=0; i<n; i++){
            for (int j=0; j<10; j++){
                dp[i][j] = MAX_VALUE;
            }
        }

        // 회전 수 고정한 채로 초기 값 세팅
        for (int i=0; i<10; i++){
            // 회전 횟수 구하기
            // 먼저 i번 반시계 회전했을 때 값 구하기 
            int currentNumber = counterclockwiseRotate(currentState[0], i);

            // 여기서 숫자를 맞추기 위해 필요한 시계 방향 회전 수를 구한다.
            int clockwiseRoateCnt = currentNumber - goalState[0];
            if (clockwiseRoateCnt < 0){
                clockwiseRoateCnt += 10;
            }

            // 반시계 회전 횟수 + 시계 회전 횟수
            dp[0][i] = i + clockwiseRoateCnt;
        }

        // 순회 시작
        for (int i=0; i<n-1; i++){
            for (int j=0; j<10; j++){
                if (dp[i][j] == MAX_VALUE){
                    continue;
                }
                // 먼저 i+1번째 마법진의 현재 숫자를 구한다. (j번 반시계 회전)
                int currentNumber = counterclockwiseRotate(currentState[i+1], j);

                // 이 마법진이 목표에 도달하기 위해 필요한 시계 방향 회전 수를 구한다. (반시계 회전수는 고정되어 있기 때문에 고려할 필요 없다.)
                // 여기서 숫자를 맞추기 위해 필요한 시계 방향 회전 수를 구한다.
                int clockwiseRoateCnt = currentNumber-goalState[i+1];
                if (clockwiseRoateCnt < 0){
                    clockwiseRoateCnt += 10;
                }

                dp[i+1][j] = dp[i][j] + clockwiseRoateCnt;
            }
        }

        // 최소 회전 수 구하기
        int res = MAX_VALUE;
        for (int i=0; i<10; i++){
            res = Math.min(res, dp[n-1][i]);
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(res));
        bw.close();

    }
    public static int counterclockwiseRotate(int number, int cnt){
        number += cnt;
        if (number >= 10){
            number-=10;
        }
        return number;
    }
}