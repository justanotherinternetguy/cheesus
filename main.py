path = "./bible.txt"
out_path = "./out.txt"

with open(path, 'r') as f:
    bible = f.read().split()


print(bible)

# reformat
for i in range(len(bible)):
    if bible[i][:3].lower() == 'god':
        bible[i] = "Cheesus Christ"
    bible[i] += ' '

print(bible)



with open(out_path, 'a') as new_bible:
    new_bible.truncate(0);
    for i in bible:
        new_bible.write(i);
