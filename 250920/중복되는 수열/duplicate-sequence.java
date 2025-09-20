import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    private static TrieNode root = new TrieNode();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++){
            insertNode(br.readLine());
        }
        boolean result = isExist();
        bw.write(result ? "0" : "1");
        bw.close();
    }

    private static boolean isExist(){
        Queue<TrieNode> queue = new LinkedList();
        queue.add(root);
        while(!queue.isEmpty()){
            TrieNode node = queue.remove();
            for (int i=0; i<10; i++){
                // 존재한다면 큐에 넣기 
                if (node.nextIntegers[i] != null){
                    queue.add(node.nextIntegers[i]);
                    // 그런데 현재 것이 마지막이라면? 가능
                    if (node.isEnd){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private static void insertNode(String sequence){
        TrieNode node = root;
        for (int i=0; i<sequence.length(); i++){
            int number = (int)(sequence.charAt(i)-'0');
            // number가 없다면 추가
            if (node.nextIntegers[number] == null){
                node.nextIntegers[number] = new TrieNode();
            }
            // number가 있든 없든 이동
            node = node.nextIntegers[number];
        }
        node.isEnd = true;
    }

    static class TrieNode{
        
        TrieNode[] nextIntegers = new TrieNode[10];
        boolean isEnd = false;
        TrieNode(){

        }
    }
}