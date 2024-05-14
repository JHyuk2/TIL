# D3 치고 굉장히 쉬운 문제...

for t in range(int(input())):
    L, U, X = map(int, input().split())
    answer = 0 if X <= U else -1

    if not answer:
        answer = 0 if X >= L else (L-X)
    print(f'#{t+1} {answer}')