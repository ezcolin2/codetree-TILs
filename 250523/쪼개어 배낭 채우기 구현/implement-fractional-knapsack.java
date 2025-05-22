import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

class Jewel implements Comparable<Jewel>{
    int weight;
    int value;

    public Jewel(int weight, int value){
        this.weight = weight;
        this.value = value;
    }

    @Override
    public int compareTo(Jewel jewel){
        // 가격/무게 기준으로 내림차순 정렬
        double difference = (double)(jewel.value/jewel.weight) - (double)(this.value/this.weight);
        if (difference > 0){
            return 1;
        } else if (difference == 0){
            return 0;
        } else{
            return -1;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 보석 정보
        Jewel[] jewels = new Jewel[n];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());
            jewels[i] = new Jewel(weight, value);
        }

        // greedy
        double result = 0;
        Arrays.sort(jewels);
        for (int i=0; i<n; i++){
            // 만약 남은 가방의 크기보다 작다면
            if (m >= jewels[i].weight){
                m -= jewels[i].weight;
                result += jewels[i].value;
            } else{
                result += (double)m/jewels[i].weight*jewels[i].value;
                break;
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.format("%.3f", result));
        bw.close();

    }
}