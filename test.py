import pyperclip
words = []
with open('word.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

print(words)
while True:
    choice = input('Type: ')
    if choice == "l":
        # substring = pyperclip.paste().lower()
        substring = input()
        ans = [word for word in words if substring in word]
        ans.sort(key=len, reverse=True)
        pyperclip.copy(ans[0])
    elif choice == "m":
        # substring = pyperclip.paste().lower()
        substring = input()
        ans = [word for word in words if substring in word]
        ans.sort(key=len)
        pyperclip.copy(" ".join(ans)[:2000])