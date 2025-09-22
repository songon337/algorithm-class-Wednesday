## 반복과 재귀 팩토리얼 구현
import time 

def factorial_iter(n):
    result = 1
    if n < 0:
        raise ValueError
    else:
        for i in range(2,n+1):
            result = result * i

    return result


def factorial_rec(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:   
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n):
    start = time.perf_counter()
    v = func(n)
    t = time.perf_counter() - start
    return v, t

if __name__ == '__main__':
    print("팩토리얼 계산기 (반복,재귀)\n")
    print("==============Factorial Tester================\n")
    print("1) 반복법으로 n!계산\n")
    print("2) 재귀법으로 n!계산\n")
    print("3) 두방식 모두계산후 결과 시간 비교\n")
    print("4) 준비된 테스트 데이터 일괄실행\n")
    print("q) 종료\n")
    print("==============================================\n")

  

    data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

        
    while True:
        menu = input("선택: \n").strip()
        if menu == ("1"):
            raw = int(input("반복-정수 n>=0 을 입력하시오"))
            print(factorial_iter(raw))
        elif menu == ("2"):
            raw =  int(input("재귀-정수 n>=0 을 입력하시오"))
            print(factorial_rec(raw))
        elif menu == "3":
            raw = int(input("-정수 n>=0 을 입력하시오"))
            a_val, a_t = run_with_time(factorial_iter, raw)
            try:
                b_val, b_t = run_with_time(factorial_rec, raw)
                same = (a_val == b_val)
            except RecursionError:
                b_val, b_t, same = None, None, False
                print("재귀 계산에서 RecursionError 발생")

            print(f"반복 시간: {a_t:.6f}초")
            if b_t is not None:
                print(f"재귀 시간: {b_t:.6f}초")
                print(f"결과 일치 여부: {same}")
            print("n! 값(반복):", a_val)
        elif menu == "4":
            data1, data2 = [], []
            for i in data:
                a_val, a_t = run_with_time(factorial_iter, i)
                data1.append(a_val)
                try:
                    b_val, b_t = run_with_time(factorial_rec, i)
                    data2.append(b_val)
                    same = (a_val == b_val)
                    print(f"n={i} | 반복 {a_t:.6f}s, 재귀 {b_t:.6f}s, 일치:{same}")
                except RecursionError:
                    data2.append(None)
                    print(f"n={i} | 반복 {a_t:.6f}s, 재귀: RecursionError")
            if data1 == data2:
                print("결과값이 일치합니다")
            print("반복은:", data1)
            print("재귀는:", data2)

        elif menu == ("q"):
            print("종료합니다")
            break
        else:
            print("정수를 입력하시오")