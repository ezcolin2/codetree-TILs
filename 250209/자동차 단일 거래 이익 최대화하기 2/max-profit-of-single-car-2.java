import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.lang.Math;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 시작 점
        int start = 0;
        int maxBenefit = 0;
        
        for (int i=0; i<n; i++){
            // 시작보다 값이 작아지면 갱신
            if (arr[start] > arr[i]){
                start = i;
                continue;
            }

            // 크다면 maxBenefit 갱신
            maxBenefit = Math.max(maxBenefit, arr[i]-arr[start]);
        }
        bw.write(String.valueOf(maxBenefit));
        bw.close();

    }
}