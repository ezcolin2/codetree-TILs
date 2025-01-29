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
        for (int i=0; i<=n; i++){
            for (int j=0; j<=k; j++){
                dp[i][j][0] = 0;
                dp[i][j][1] = 0;
            }
        }
        
        for (int i=1; i<=n; i++){
            // 획득할 수정 위치
            int crystalLocation = getIndexOfCrystalLocation(crystal.charAt(i-1));
            for (int j=0; j<=k; j++){
                for (int p=0; p<2; p++){
                    // 같은 위치에 수정이 있으면
                    if (p == crystalLocation){
                        // 1. 바로 이전에 이동을 한 경우
                        // 2,. 바로 이전에 이동을 하지 않은 경우
                        
                        if (j < k){
                            dp[i][j][p] = Math.max(dp[i-1][j+1][(p+1)%2], dp[i-1][j][p])+1;
                        }
                        // 한 번도 이동하지 않았다면
                        else{
                            dp[i][j][p] = dp[i-1][j][p]+1;
                        }
                        
                        
                    }
                    // 다른 위치에 수정이 있으면
                    else{
                        // 1. 바로 이전에 이동을 한 경우
                        // 2,. 바로 이전에 이동을 하지 않은 경우
                        if (j < k){
                            dp[i][j][p] = Math.max(dp[i-1][j+1][(p+1)%2], dp[i-1][j][p]);
                        }
                        // 한 번도 이동하지 않았다면
                        else{
                            dp[i][j][p] = dp[i-1][j][p];
                        }
                        
                    }
                
                }
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