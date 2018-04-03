# 统计西游记中每个字出现的频率次数

fr = open('../../../files/西游记.txt', 'r', encoding='utf-8')

character = []
stat = {}

for line in fr:
    line = line.strip()

    if len(line) == 0:
        continue

    line = str(line)

    for x in range(0, len(line)):
        if not line[x] in character:
            character.append(line[x])

        if line[x] not in stat:
            stat[line[x]] = 0
        stat[line[x]] += 1

# print(len(character))
# print(len(stat))

stat = sorted(stat.items(), key=lambda d: d[1], reverse=True)  # 按照值来对整个词典进行排序
# print(type(stat))

f2 = open('../../../files/xyj_count.txt', 'w', encoding='utf-8')
for each in stat:
    f2.write(str(each[0])+','+str(each[1])+'\n')

f2.close()

print('统计完毕...')
