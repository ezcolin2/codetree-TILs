const fs = require('fs');

    const input = fs.readFileSync(0).toString().trim().split('\n');
    const [n, k, u, d] = input[0].trim().split(' ').map(Number);
    
    const arr = input.slice(1).map((item)=>item.trim().split(' ').map(Number));
    // 동서남북
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    function canGo(x, y){
        return 0<=x && x<n && 0<=y && y<n;
    }

    const list = []; // 갈 수 있는 도시 정보011131021
    for (let i=0;i<n;i++){
        for (let j=0;j<n;j++){
            let cnt = 0; // 갈 수 있는 도시
            for (let m=0;m<4;m++){
                const [nx, ny] = [i+dx[m], j+dy[m]];
                // 거리
                
                if (canGo(nx, ny) ){
                    const distance = Math.abs(arr[nx][ny] - arr[i][j]);
                    if (u<=distance && distance<=d){
                        cnt+=1;
                    }
                    
                }
            }
            list.push(cnt);
        }
    }
    list.sort((a, b)=>b-a); // 역순 정렬
    let res = 0;
    for (let i=0;i<k;i++){
        res+=list[i];
    }
    console.log(res);