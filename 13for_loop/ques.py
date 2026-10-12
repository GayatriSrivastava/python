str=input("engter a string:").strip().lower()
flag=False
count=0
for ch in str:
    if ch=="o" and flag==False:
        flag=True
        print("found")
if not flag:
    print("not found")