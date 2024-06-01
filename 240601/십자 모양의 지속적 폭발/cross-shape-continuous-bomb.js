const fs = require('fs')

const input = fs.readFileSync(0).toString().trim().split('\n')
const [n, m] = input[0].trim().split(' ').map(Number)
const arr = input.slice(1, n+1).map((item)=>item.trim().split(' ').map(Number))
const columns = input.slice(n+1, n+m+1).map(Number)
// 동서남북
const dx = [0, 0, 1, -1]
const dy = [1, -1, 0, 0]

// 입력받은 열 중 가장 위에 있는 것
function findRow(col){
    for (let i=0;i<n;i++){
        if (arr[i][col]!=0){
            return i
        }
    }
    // 없으면 -1 반환
    return -1
}

// [x][y] 위치로 갈 수 있는지 판단
function can_go(x, y){
    return 0<=x && x<n && 0<=y && y<n
}
// [0][col] 좌표에서 폭탄 터뜨리는 함수
function explode(col){
    col-=1
    let row = findRow(col)
    // 터뜨릴 곳이 없으면 끝
    if (row == -1){
        return 
    }
    const count = arr[row][col]
    arr[row][col] = 0
    for (let i = 0;i<4;i++){
        let [x, y] = [row, col]
        // count 만큼 해당 방향으로 없앰
        for (let j=0;j<count-1;j++){
            const [nx, ny] = [x+dx[i], y+dy[i]]
            if (can_go(nx, ny)){
                arr[nx][ny] = 0
                x = nx
                y = ny
            }
        }
    }
    // 터뜨리고 나면 중력으로 이동
    for (let i=0;i<n;i++){
        // 새로운 배열 만들어서 0이 아닐때마다 넣기
        // 편의를 위해 temp에는 방향을 거꾸로 넣음
        const temp = []
        for (let j=n-1;j>=0;j--){
            if (arr[j][i]!=0){
                temp.push(arr[j][i])
            }
        }
        const len = temp.length
        for (let j=0;j<n-len;j++){
            temp.push(0)
        }
        temp.reverse()
        // temp를 바탕으로 다시 넣음
        for (let j=n-1;j>=0;j--){
            arr[j][i] = temp[j]
        }
    }
}
for (let i = 0;i<m;i++){
    explode(columns[i])
}
arr.map((item)=>console.log(item.join(' ')))