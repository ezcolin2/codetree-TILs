import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.lang.Comparable;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Meeting[] meetingArr = new Meeting[n];
        StringTokenizer st;
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            meetingArr[i] = new Meeting(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        Arrays.sort(meetingArr);
        int res = 0;
        int end = 0;
        for (int i=0; i<n; i++){
            if (end <= meetingArr[i].start){
                end = meetingArr[i].end;
                res += 1;
            }
            
        }
        System.out.println(n-res);

    }
}

class Meeting implements Comparable<Meeting>{
    public int start;
    public int end;
    
    Meeting(int start, int end){
        this.start =  start;
        this.end = end;
    }

    @Override
    public int compareTo(Meeting meeting){
        // end가 같을 경우에는 큰 상관이 없으나 일단 start 기준 오름차순
        if (this.end == meeting.end){
            return Integer.compare(this.start, meeting.start);
        }

        // end 기준 오름차순
        return Integer.compare(this.end, meeting.end);
    }

}