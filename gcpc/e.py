s = input().lower()

if "sss" in s:
    print(s.replace("sss", "sB"))
    print(s.replace("sss", "Bs"))
    print(s.replace("sss", "sss"))
elif "ss" in s:
    print(s.replace("ss", "B"))
    print(s.replace("ss", "ss"))
else:
    print(s)