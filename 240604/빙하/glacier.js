/*
dfs 동작 과정
1. arr를 복사해서 copiedArr를 만듦
2. copiedArr를 기준으로 상하좌우 탐색 시작
3. copiedArr를 방문하면 isVisited를 true로 변경
4. copiedArr에서 1(빙하) 만난다면 원본 arr의 해당 위치를 0(물)으로 바꾸고 isVisited를 true로 바꾸지만 해당 위치로 이동하지는 않음
5. count를 1 증가
*/

const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, m] = input[0].trim().split(' ').map(Number);
const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number));
const isVisited = Array(n).fill(0).map(()=>Array(m).fill(false));

function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<m;
}

// 동서남북
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

// dfs를 호출할 때 visited를 true로 만들기
let melted=0;
function dfs(x, y){
    // 원본 2차원 배열 복사
    const copiedArr = arr.map((item)=>[...item]);
    for (let i=0;i<4;i++){
        const [nx, ny] = [x+dx[i], y+dy[i]];
        // 갈 수 있고 방문하지 않았다면 
        if (canGo(nx, ny) && !isVisited[nx][ny]){
            // 빙하라면?
            if (copiedArr[nx][ny] == 1 && arr[nx][ny] == 1){
                // isVisited를 true 만들지만 방문하지는 않음
                isVisited[nx][ny] = true;
                // 원본 2차원 배열을 물로 만듦
                arr[nx][ny] = 0;
                melted++;
            }
            // 물이라면?
            else{
                // isVisited를 true 만들고 방문
                isVisited[nx][ny] = true;
                dfs(nx, ny);
            }
        }
    }
}

// 시작
let count = 0;
for (let i=0;i<n;i++){
    for (let j=0;j<m;j++){
        // 방문하지 않았고 물이라면 탐색 시작
        if (!isVisited[i][j] && arr[i][j] == 0){
            isVisited[i][j] = true;
            dfs(i, j);
            count++;
        }
    }
}
console.log(count, melted);