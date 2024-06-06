const fs = require('fs');

const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, m] = input[0].trim().split(' ').map(Number);
const arr = input.slice(1).map((item) => item.trim().split(' ').map(Number));
// b를 기준으로 정렬
arr.sort((a, b) => a[1] - b[1])

// start부터 시작해서 내려가는 함수
function goDown(start, idx, combination) {
    if (idx == combination.length) {
        return start;
    }
    const [a, b] = combination[idx];
    if (start == a) {
        return goDown(start + 1, idx + 1, combination);
    } else if (start == a + 1) {
        return goDown(start - 1, idx + 1, combination);
    } else {
        return goDown(start, idx + 1, combination);
    }
}

function getRes(comb) {
    // 모든 세로줄에서 시작한 결과 담을 배열
    const firstArr = [];
    for (let i = 1; i <= n; i++) {
        firstArr.push(goDown(i, 0, comb));
    }
    // 처음 결과
    return firstArr.join(' ');
}

// 처음 결과
const firstRes = getRes(arr);

// 최소 가로줄 수
let minRes = m;

// 조합
const combination = [];

// 조합 생성 함수
function makeCombination(currIdx, cnt) {
    // 끝까지 조사하면 끝
    if (currIdx == m) {
        // 모든 경우에 대해서 가 봄
        if (cnt >= 0) {
            const tempRes = getRes(combination);
            if (tempRes == firstRes) {
                if (combination.length < minRes) {
                    minRes = combination.length;
                }

            }
        }
        return;
    }

    // currIdx에 해당하는 가로줄을 선택
    combination.push(arr[currIdx]);
    makeCombination(currIdx + 1, cnt + 1);
    combination.pop();

    // currIdx에 해당하는 가로줄을 선택하지 않음
    makeCombination(currIdx + 1, cnt);
}

makeCombination(0, 0);
console.log(minRes);