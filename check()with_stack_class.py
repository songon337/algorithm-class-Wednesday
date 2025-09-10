#괄호 검사 프로그램
from stack_class import ArrayStack

def checkBrackets(statment):
    #여는 괄호는 push,다는 괄호가 나오면 스택의 맨 위와 짝이 맞는지 확인 후 pop-> lifo 이용

    pairs = {')':'(', ']':'[', '{':'}'}
    openings = set(pairs.values())
    stack = ArrayStack(len(statment))

    for ch in statment: # 입력 문자열 순회
        if ch in openings: #여는 괄호이면 스택에 push
            stack.push(ch) 
        elif ch in pairs: #닫힌괄호
            if stack.is_empty(): #조건2위반:짝이맞지않음
                return False
            if stack.peek() != pairs[ch]: # 조건 3 위반 : 짝이 맞지 않음
                return False
            stack.pop()
        else:
            pass    #괄호가 아니면 무시

    return stack.is_empty() # True -> 검사 성공, false: 조건1이 위반

# 테스트하기
def test_brackets():
    tests = [
        "{A[(i+1)]=0;}",
        "if((x<0) && (y<3))"
        ,"while(n<8)){n++;}",
        "arr[i+1)=0",
    ]
    for t in tests:
        print(t,"->",checkBrackets(t))

if __name__ == "__main__":
    test_brackets()