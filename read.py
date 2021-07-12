data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 10000 == 0:
            print(len(data))

for d in data:
    sum_len += len(d)
print('平均留言長度為', sum_len / len(data), '個字')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
