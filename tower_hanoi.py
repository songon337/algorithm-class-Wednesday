# 하노이 탑 문제: 재귀적으로 문제 해결

def tower_hanoi(n,start,tmp,target):
    # 1. 재귀 호출 종료 (base case)
    if n == 1:
        print("원판 %d : %s -> %s" % (n,start,target))
     # 재귀 분할 호출
    else:
        # 위의 n-1개 원판을 start ->tmp로 옮김 (target막대를 보조 막대)
        tower_hanoi(n-1,start,target,tmp) #왼쪽 서브트리 순회

        # 가장큰 1개 원판을 start 에서 target 으로 이동 출력
        print("원판 {n} :  {start} -> {target}")

        #tmp에 있는 n-1개 원판을 tmp 에서 target으로 옮김
        tower_hanoi(n-1,tmp,start,target) # 오른쪽 서브 트리 재귀 순회


if __name__ == "__main__":
    n= int(input("원판의 개수를 입력해주세요"))
    tower_hanoi(n,'A','B','C')

    total = ( 1 << n ) - 1
    print("\n총 이동 횟수 : " (2^{n}-1))