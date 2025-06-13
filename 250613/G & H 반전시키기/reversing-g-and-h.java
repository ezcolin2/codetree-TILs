import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String a = sc.next();
        String b = sc.next();
        int res = 0;
        int cnt = 0;
        for (int i=0; i<n; i++){
            // 같다면? cnt 증가
            if (a.charAt(i) == b.charAt(i)){
                res += cnt;
                cnt = 0;
            }
            // 다르다면?
            else{
                cnt = 1;
                if (i == n-1){
                    res += cnt;
                }
            }
        }
        System.out.println(res);
    }
}

