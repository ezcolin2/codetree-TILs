const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

let res = Number.MAX_SAFE_INTEGER;
function dfs(idx, cnt){
    if (idx==n-1){
        if (cnt < res){
            res = cnt;
        }
    }

    if (idx==-1){

    }
    
    // 최대 점프 가능 횟수
    const maxJump = arr[idx];
    
    // 갈 수 있는 곳 모두 가기
    for (let i=1;i<=maxJump;i++){
        dfs(idx+i, cnt+1);
    }
}
dfs(0, 0);
console.log(res);