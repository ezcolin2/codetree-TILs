const fs = require('fs');

class Queue{
    constructor(){
        this.items={};
        let head=0;
        let tail=0;
    }

    push(item){
        this.items[this.tail] = item;
        this.tail++;
    }

    pop(){
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;
    }

    isEmpty(){
        return this.head == this.tail;
    }
}

const input =fs.readFileSync(0).toString().trim().split('\n');
const [n, m] = input[0].trim().split(' ').map(Number);
const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number));

// 방문 여부 체크
const isVisited = Array(n).fill(0).map(()=>Array(m).fill(false));
// 동서남북
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

// 갈 수 있는지 여부
function canGo(x, y){
    return 0<=x && x<n && 0<=y && y<m && arr[x][y]!=0
}
function bfs(i, j){
    isVisited[i][j] = true;
    const queue = new Queue();
    queue.push([i, j])

    // 큐가 빌 때까지 반복
    while (!queue.isEmpty()){
        const [x, y] = queue.pop();
        for (let k=0;k<4;k++){
            const [nx, ny] = [x+dx[k], y+dy[k]];
            // 갈 수 있고 방문하지 않았다면 큐에 넣음
            if (canGo(nx, ny)&& !isVisited[nx][ny]){
                // 도착했다면 1 반환
                if (nx==n-1 && ny==m-1){
                    return 1;
                }
                queue.push([nx, ny]);
                isVisited[nx][ny] = true;
            }
        }
    }
    return 0;
}
console.log(bfs(0, 0));