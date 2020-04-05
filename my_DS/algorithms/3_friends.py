## 친구
friend_list = []

n = int(input("입력받을 친구 수:"))
for _ in range(n):
    friend = input("친구 이름을 입력해주세요: ")
    friend_list.append(friend)

print(friend_list)