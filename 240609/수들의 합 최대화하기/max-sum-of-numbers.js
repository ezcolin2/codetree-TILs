const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0].trim());
const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number));

// 열 방문 여부 
const isVisited = Array(n).fill(false);
// 최대값 
let maxValue = 0;

function dfs(currRow, sum){
    if (currRow == n){
        if (sum > maxValue){
            maxValue = sum;
        }
        return;
    }
    for (let i=0;i<n;i++){
        // 방문을 하지 않았을 때만 선택
        if (!isVisited[i]){
            isVisited[i] = true;
            dfs(currRow+1, sum+arr[currRow][i]);
            isVisited[i] = false;
        }
    }
}
dfs(0, 0);
console.log(maxValue);