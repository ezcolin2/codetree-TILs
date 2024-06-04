/*
dfs 동작 과정
1. arr를 복사해서 copiedArr를 만듦
2. copiedArr를 기준으로 상하좌우 탐색 시작
3. copiedArr를 방문하면 isVisited를 true로 변경
4. copiedArr에서 1(빙하) 만난다면 원본 arr의 해당 위치를 0(물)으로 바꾸고 isVisited를 true로 바꾸지만 해당 위치로 이동하지는 않음
5. count를 1 증가

주의사항 
1. 빙하를 녹일 때 녹인 빙하는 재방문 하지 않아야 함 (녹인 빙하 isVisited true)
2. 그리고 그 다음 탐색을 시작할 때 녹인 빙하부터 방문해야 함 (녹인 빙하 isVisited false)
=> 탐색을 진행중일 때 isVisited와 탐색을 시작할 때 isVisited를 분리
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
function dfs(x, y, copiedArr, copiedIsVisited){
    // 빙하 녹인 수
    let tempMelted = 0;
    // 원본 2차원 배열 복사
    
    for (let i=0;i<4;i++){
        const [nx, ny] = [x+dx[i], y+dy[i]];
        // 갈 수 있고 방문하지 않았다면 
        if (canGo(nx, ny) && !copiedIsVisited[nx][ny]){
            // 빙하라면?
            if (copiedArr[nx][ny] == 1){
                // isVisited를 true 만들지만 방문하지는 않음
                copiedIsVisited[nx][ny] = true;
                // 원본 2차원 배열을 물로 만듦
                arr[nx][ny] = 0;
                copiedArr[nx][ny] = 0;
                tempMelted++;
            }
            // 물이라면?
            else{
                // isVisited를 true 만들고 방문
                // isVisited[nx][ny] = true;
                copiedIsVisited[nx][ny] = true;
                tempMelted += dfs(nx, ny, copiedArr, copiedIsVisited);
            }
        }
    }
    return tempMelted;
}

// 시작
let melted = 0;
let count = 0;
for (let i=0;i<n;i++){
    for (let j=0;j<m;j++){
        // 방문하지 않았고 물이라면 탐색 시작
        if (!isVisited[i][j] && arr[i][j] == 0){
            isVisited[i][j] = true;
            const copiedArr = arr.map((item)=>[...item]);
            const copiedIsVisited = isVisited.map((item)=>[...item]);
            const res = dfs(i, j, copiedArr, copiedIsVisited);
            // 모두 녹였을 때도 탐색을 하게 되는데 이럴 때 count가 증가하지 않게
            if (res>0){
                count++;
                melted = res;
            }
        }
        isVisited[i][j] = true
    }
}
console.log(count, melted);