import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[] a = sc.next().toCharArray();
        char[] b = sc.next().toCharArray();
        int cnt = 0;
        // 영향이 적은 뒤에서부터 바꾼다.
        for (int i=n-1; i>=0; i--){
            // 똑같으면 바꿀 필요 없음
            if (a[i] == b[i]){
                continue;
            }

            // 같으면 앞에거까지 모두 바꾸기
            for (int j=i; j>=0; j--){
                if(a[j] == 'H'){
                    a[j] = 'G';
                } else{
                    a[j] = 'H';
                }
                
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}