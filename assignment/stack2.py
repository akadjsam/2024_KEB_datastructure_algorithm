
txt = []
test = ""
f = open("stack2.txt", 'r',encoding='UTF8')
while True:
    line = f.readline()
    if not line:
        break
    txt.append(line)
f.close()

f = open("stack2.txt", 'w',encoding='UTF8')
for i in range(len(txt)):
    test = txt.pop()
    f.write("".join(reversed(test)))
f.close()