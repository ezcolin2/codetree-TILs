const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, m, c] = input[0].trim().split(' ').map(Number);
const arr = input.slice(1).map((item) => item.trim().split(' ').map(Number));
function dfs(tempArr, res, currIdx) {
    /*
        arr : 탐색할 배열
        res : 결과를 담을 배열 [무게의 합, 가치 합, 최대값]
        currIdx : 인덱스 currIdx에 위치한 물건을 훔칠건지
     */
    // 끝에 도달
    if (currIdx == tempArr.length) {
        // 물건을 들 수 있다면 maxValue 갱신
        // 가치가 maxValue보다 크다면 갱신
        res[2] = res[1] > res[2] ? res[1] : res[2];
        return;
    }

    // arr[currIdx]를 선택
    if (res[0] + tempArr[currIdx] <= c) {
        res[0] += tempArr[currIdx];
        res[1] += tempArr[currIdx] ** 2;
        dfs(tempArr, res, currIdx + 1);
        res[0] -= tempArr[currIdx];
        res[1] -= tempArr[currIdx] ** 2;
    }


    // arr[currIdx]를 선택 X
    dfs(tempArr, res, currIdx + 1);
}
const list = [8, 1];
const res = [0, 0, 0];
dfs(list, res, 0);

let maxVal = 0;
// 모든 조합
// 첫 번째 도둑
for (let i = 0; i < n; i++) {
    for (let j = 0; j <= n - m; j++) {
        // j j+m-1 q q+m-1
        // 두 번째 도둑
        for (let p = i; p < n; p++) {
            for (let q = 0; q <= n - m; q++) {
                // 겹치면 패스
                if (p == i) {
                    if ((q <= j + m - 1 && j + m - 1 <= q + m - 1) || (q <= j && j <= q + m - 1) || (j <= q && q <= j + m - 1) || (j <= q + m - 1 && q + m - 1 <= j + m - 1)) {
                        continue;
                    }
                }
                // 첫 번째 도둑이 선택한 물건
                const firstArr = [];
                const firstRes = [0, 0, 0];
                for (let k = 0; k < m; k++) {
                    firstArr.push(arr[i][j + k]);
                }

                // 선택한 연속된 물건들 중 가치 합 최대값 구함
                dfs(firstArr, firstRes, 0);
                // 두 번째 도둑이 선택한 물건
                const secondArr = [];
                const secondRes = [0, 0, 0];
                for (let t = 0; t < m; t++) {
                    secondArr.push(arr[p][q + t]);
                }

                // 선택한 연속된 물건들 중 가치 합 
                dfs(secondArr, secondRes, 0);
                if (firstRes[2]+secondRes[2] >maxVal) {
                    maxVal = firstRes[2]+secondRes[2];
                }

            }
        }
    }
}
console.log(maxVal);