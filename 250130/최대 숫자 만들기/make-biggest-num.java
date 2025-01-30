import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Comparator;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String[] arr = new String[n];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = st.nextToken();
        }
        Arrays.sort(arr, new Comparator<String>(){
            @Override
            public int compare(String a, String b){
                String bigIntA = a+b;
                String bigIntB = b+a;
                int length = bigIntA.length();
                // overflow에 대비하여 하나씩 비교한다.
                for (int i=0; i<length; i++){
                    if (bigIntA.charAt(i) > bigIntB.charAt(i)){
                        return -1;
                    }
                    else if (bigIntA.charAt(i) < bigIntB.charAt(i)){
                        return 1;
                    }
                }
                return 0;
            }
        });
        StringBuilder sb = new StringBuilder();
        for (String num : arr) {
            sb.append(num);
        }
        System.out.println(sb.toString());
    }
}