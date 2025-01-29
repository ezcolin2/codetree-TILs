import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.lang.Math;
public class Main {

    // L -> 0 반환
    // R -> 1 반환
    public static int getIndexOfCrystalLocation(char crystalLocation){
        if (crystalLocation == 'L'){
            return 0;
        }
        return 1;
    }

    // 엘라가 수집할 수 있는 수정의 최대 개수 반환
    public static int getMaxCrystal(String crystal, int k){
        // 변수 1 : 현재 생성될 수정
        // 뱐수 2 : 남은 움직일 수 있는 횟수
        // 변수 3 : 현재 샘터 위치 (L, R)

        // dp[i][j][k]
        // i번째 수정까지 고려했을 때 
        // 현재 샘터 위치가 j이고
        // 남은 움직일 수 있는 횟수가 k일 때 수집할 수 있는 수정의 최대 개수 
        int n = crystal.length();
        int[][][] dp = new int[n+1][k+1][2];
        for (int i=1; i<=n; i++){
            // 생성될 수정 위치
            int crystalLocation = getIndexOfCrystalLocation(crystal.charAt(i-1));

            
            for (int j=0; j<=k; j++){
                // 수정을 수집하는 경우
                // 1. 이전에도 남은 횟수가 같았고 같은 방향 (수정을 수집하기 위해 이동하지 않음)
                // 2. 이전에 남은 횟수가 하나더 있었고 다른 방향 (수정을 수집하기 위해 이동)
                if (j<k){
                    dp[i][j][crystalLocation] = Math.max(
                        dp[i-1][j][crystalLocation]+1, 
                        dp[i-1][j+1][(crystalLocation+1)%2]+1                
                    );
                }
                else{
                    dp[i][j][crystalLocation] = dp[i-1][j][crystalLocation]+1;   
                }
                

                // 수정을 수집하지 않는 경우
                // 1. 이전에도 남은 횟수가 같았고 같은 방향 (수정을 수집하지 않기 위해 이동하지 않음)
                dp[i][j][(crystalLocation+1)%2] = dp[i-1][j][(crystalLocation+1)%2];

            }
        }
        int res = 0;
        for (int j=0; j<=k; j++){
            res = Math.max(res, Math.max(dp[n][j][0], dp[n][j][1]));
        }
        return res;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputString = br.readLine();
        StringTokenizer st = new StringTokenizer(inputString);
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        String crystal = br.readLine();

        System.out.println(getMaxCrystal(crystal, k));

    }
}