number_list = []
num = 1
while num < 1000:
    number_list.append(str(num ** 3))
    num += 2

num_sum = 0

for i in number_list:
    num = 0
    for j in range(0, len(i)):
        num += int(i[j])
    if (num % 7) == 0:
        num_sum += int(i)
print(num_sum)
