import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String currentString = br.readLine();
        String goalString = br.readLine();
        int left = 0;
        int right = 0;
        int res = 0;
        while(right<n){
            // 만약 right번째가 같다면
            if (currentString.charAt(right) == goalString.charAt(right)){
                // 다시 조사 지금까지 구한 구간이 있다면 추가
                if (left < right){
                    res++;
                }
                right++;
                left = right;
            }

            // 만약 right번째가 다르다면
            else{
                right++;
                // 그런데 구간이 4개가 되었거나 마지막에 도달 했다면 더이상 못 늘리니까 구간 종료
                if (right-left == 3 || right == n){
                    res++;
                    right++;
                    left = right;
                } 
            }
        }
        System.out.println(res);
    }
}