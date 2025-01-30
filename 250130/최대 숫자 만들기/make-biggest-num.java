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
                return Integer.parseInt(b+a) - Integer.parseInt(a+b);
            }
        });
        String res = "";
        for (int i=0; i<n; i++){
            res += arr[i];
        }
        System.out.println(res);
    }
}