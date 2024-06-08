const fs = require('fs');

const n = Number(fs.readFileSync(0).toString().trim());
const isVisited = Array(n+1).fill(false);

// currIdx 위치에 선택할 숫자
const perm = [];
function dfs(currIdx){
    if (currIdx == 3){
        console.log(perm.join(' '));
        return
    }
    for (let i=1;i<=n;i++){
        // 방문하지 않았다면 선택
        if (!isVisited[i]){
            perm.push(i);
            isVisited[i] = true;
            dfs(currIdx+1);
            perm.pop();
            isVisited[i] = false;
        }
    }
}
dfs(0);