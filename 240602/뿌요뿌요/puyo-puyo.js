const fs = require('fs')

const input = fs.readFileSync(0).toString().trim().split('\n')
const n = Number(input[0])
const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number))

// 방문 여부 체크
const isVisited = Array(n).fill(0).map(()=> Array(n).fill(false))
// 동서남북
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]

let cnt = 0
function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<n
}
function dfs(x, y){
    isVisited[x][y] = true
    cnt+=1
    for (let i=0;i<n;i++){
        for (let j=0;j<n;j++){
            // 방문하지 않았다면 방문
            for (let k=0;k<4;k++){
                const [nx, ny] = [i+dx[k], j+dy[k]]
                if (canGo(nx, ny) && !isVisited[nx][ny] && arr[x][y]==arr[nx][ny]){
                    dfs(nx, ny)
                }
            }

        }
    }
}
let number = 0;
let maxNum = 0;
for (let x=0;x<n;x++){
    for (let y=0;y<n;y++){
        cnt = 0
        dfs(x, y)
        if (cnt>=4){
            number+=1
            if (cnt > maxNum){
                maxNum = cnt
            }
        }
    }
}
console.log(number, maxNum)