def conv(n, sir):
    conv=""
    length=len(sir)
    while n>0:
        rest=n%length
        conv=sir[rest]+conv
        n//=length
    return conv

print(conv(21, "abcd"))
