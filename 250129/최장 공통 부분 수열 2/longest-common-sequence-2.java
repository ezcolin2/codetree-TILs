import java.lang.Math;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Main {
    public static String getMaxLengthOfSequence(String a, String b){
        // 길이
        int lengthA = a.length();
        int lengthB = b.length();
        
        // 아무것도 없는 0번째 추가
        String[][] dp = new String[lengthA+1][lengthB+1];
        for (int i=0; i<=lengthA; i++){
            for (int j=0; j<=lengthB; j++){
                dp[i][j] = "";
            }
        }
        
        // dp 시작
        for (int i=1; i<=lengthA; i++){
            for (int j=1; j<=lengthB; j++){
                // 같을 경우 길이 1 추가
                if (a.charAt(i-1) == b.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1]+a.charAt(i-1);
                }

                // 같지 않을 경우
                else{
                    // 더 긴 쪽으로
                    if (dp[i-1][j].length() > dp[i][j-1].length()){
                        dp[i][j] = dp[i-1][j];
                    } else{
                        dp[i][j] = dp[i][j-1];
                    }
                }
            }
        }
        return dp[lengthA][lengthB];
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        String res = getMaxLengthOfSequence(a, b);
        System.out.println(res);
    }
}