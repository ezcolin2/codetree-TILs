import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 누적 합
        int[] sum_arr = new int[n+1];
        sum_arr[0] = 0;
        for (int i=1; i<=n; i++){
            sum_arr[i] = sum_arr[i-1]+arr[i-1];
        }

        // greedy 사용
        int result = Integer.MIN_VALUE;
        int left = 1;
        int right = 1;
        while (right<=n){
            // 부분 수열 합 구하기
            int sum = sum_arr[right] - sum_arr[left-1];
            result = Math.max(result, sum);
            // 만약 음수면 left를 right+1로 초기화\
            if (sum<0){
                left = right+1;
                right = left;
            } else{
                right += 1;
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(result));
        bw.close();
    }
}