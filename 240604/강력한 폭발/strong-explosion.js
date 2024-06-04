/*
1. 2차원 배열에서 1을 찾아서 터질 공간을 탐색한다.
2. 백트래킹으로 모든 경우의 수 시도
 */
const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0].trim());
const arr = input.slice(1).map((item) => item.trim().split(' ').map(Number));

// 1, 2, 3번 폭탄 순서
const dx = [
    [-2, -1, 0, 1, 2], // 위 -> 아래
    [0, 0, 0, 1, -1], // 동서남북
    [-1, -1, 0, 1, 1] // 위왼오 아래왼오
]
const dy = [
    [0, 0, 0, 0, 0],
    [1, -1, 0, 0, 0],
    [-1, 1, 0, -1, 1]
]
const isVisited = Array(n).fill(0).map(() => Array(n).fill(0));
// 터질 영역이 겹칠 수 있기 때문에 이미 방문한 곳도 방문
function canGo(x, y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}
// 백트래킹
let currentCnt = 0;
let res = []; // 모든 경우의 수에 대한 터질 폭탄의 수
function dfs(cur) {
    
    if (cur == coordinates.length) {
     
       res.push(currentCnt);
    }
    else {
        const [originX, originY] = coordinates[cur];
        for (let j = 0; j < 3; j++) {
            let [x, y] = [originX, originY];
            for (let i = 0; i < 5; i++) {
                const [nx, ny] = [x + dx[j][i], y + dy[j][i]];
                if (canGo(nx, ny)) {
                    
                    // 방문하지 않았다면 currentCnt 증가
                    if (isVisited[nx][ny]==0) {
                        currentCnt += 1;
                    }
                    isVisited[nx][ny]++;
                }
            }
            dfs(cur + 1);
            // 끝났으면 전부 false로
            // 폭탄 범위를 모두 false로 만듦
            [x, y] = [originX, originY];
            for (let i = 0; i < 5; i++) {
                const [nx, ny] = [x + dx[j][i], y + dy[j][i]];
                if (canGo(nx, ny)) {

                    // 방문했다면 currentCnt 감소
                    if (isVisited[nx][ny]==1) {
                        currentCnt -= 1;
                    }
                    isVisited[nx][ny]--;
                }

            }
        }
    }

}

// 폭탄이 존재하는 모든 좌표
let coordinates = []
for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
        if (arr[i][j] == 1) {
            coordinates.push([i, j])
        }
    }
}
dfs(0)
res.sort((a, b)=>b-a);
console.log(res[0])