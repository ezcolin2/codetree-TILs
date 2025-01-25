import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Main {
    // dp[i][j] : 문자열 s를 i까지 고려하고 문자열 p를 j까지 고려했을 때 패턴 일치 여부
    public static boolean[][] dp;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = '&'+br.readLine();
        String p = '&'+br.readLine();

        // 초기화
        dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        dp[1][0] = true;

        // dp 시작
        for (int i=1; i<=s.length(); i++){
            for (int j=1; j<=p.length(); j++){
                // .이고 dp[i-1][j-1]이 패턴 일치하면 무조건 패턴 일치
                if (p.charAt(j-1) == '.' && dp[i-1][j-1]){
                    dp[i][j] = true;
                }

                if (p.charAt(j-1) == '*'){
                    // 0개일 경우
                    if (dp[i][j-2]){
                        dp[i][j] = true;
                    }
                    // 1개일 경우


                    // 2개 이상일 경우
                    if (dp[i-1][j] && (s.charAt(i-1) == p.charAt(j-2) || p.charAt(j-2) == '.')){
                        dp[i][j] = true;
                    }
                }

                if (p.charAt(j-1) != '.' && p.charAt(j-1) != '*'){
                    if (dp[i-1][j-1] && s.charAt(i-1) == p.charAt(j-1)){
                        dp[i][j] = true;
                    }
                }

            }
        }
        System.out.println(dp[s.length()][p.length()]);
    }
}