import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;
import java.util.HashMap;
import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        for (int i=0; i<n; i++){
            arr[i] = br.readLine();
        }

        // 각 문자열마다 '('와 ')'의 개수 구하기
        Map<String, int[]> countMap = new HashMap();
        for (int i=0; i<n; i++){
            // 만약 key가 없으면 생성
            if (!countMap.containsKey(arr[i])){
                countMap.put(arr[i], new int[2]);
            }

            // 문자열 길이
            int length = arr[i].length();

            // 문자열 모두 확인하면서 개수 구하기
            for (int j=0; j<length; j++){
                if (arr[i].charAt(j) == '('){
                    countMap.get(arr[i])[0] += 1;
                }
                else{
                    countMap.get(arr[i])[1] += 1;
                }
            }
        }

        Arrays.sort(arr, new Comparator<String>(){
            @Override
            public int compare(String a, String b){
                // 우선 a가 앞으로 왔을 때 새로 생기는 쌍 구하기
                int newPairA = countMap.get(a)[0] * countMap.get(b)[1];

                // b가 앞으로 왔을 때 새로 생기는 쌍 구하기
                int newPairB = countMap.get(b)[0] * countMap.get(a)[1];

                return Integer.compare(newPairB, newPairA);
            }
        });

        // 정렬된 문자열들 하나로 합치기
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++){
            sb.append(arr[i]);
        }

        // countLeftArr[i] : totlalString의 i 인덱스 문자 포함해서 왼 쪽에 존재하는 '('의 개수
        // countRightArr[i] : totlalString의 i 인덱스 문자 포함해서 오른 쪽에 존재하는 ')'의 개수
        String totalString = sb.toString();

        int totalLength = totalString.length();
        int[] countRightArr = new int[totalLength];

        if (totalString.charAt(totalLength-1) == ')'){
            countRightArr[totalLength-1] = 1;
        } 
        // 누적 합 계산
        for (int i=1; i<totalString.length(); i++){
            char currentRightChar = totalString.charAt(totalLength-i-1);

            if (currentRightChar == '('){
                countRightArr[totalLength-1-i] = countRightArr[totalLength-i];
            } else{
                countRightArr[totalLength-1-i] = countRightArr[totalLength-i] + 1;
            }
        }
        
        int res = 0;
        // 이제 순회하면서 점수 구하기
        for (int i=0; i<totalLength; i++){
            // ')'면 스킵
            if (totalString.charAt(i) == ')'){
                continue;
            } else{
                res += countRightArr[i];
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(res));
        bw.close();

    }
}