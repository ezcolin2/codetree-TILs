import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i=0; i<n; i++){
            String line = br.readLine();
            for (int j=0; j<n; j++){
                arr[i][j] = (int) line.charAt(j) - '0';
            }
        }
        int res = 0;
        // 우측 하단부터 누른다.
        for (int i=n-1; i>=0; i--){
            for (int j=n-1; j>=0; j--){
                if (arr[i][j] == 1){
                    press(arr, i, j);
                    res+=1;
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(res));
        bw.close();
    }
    public static void press(int[][] arr, int row, int column){
        for (int i=0; i<=row; i++){
            for (int j=0; j<=column; j++){
                if (arr[i][j] == 0){
                    arr[i][j] = 1;
                } else{
                    arr[i][j] = 0;
                }
            }
        }
    }
}