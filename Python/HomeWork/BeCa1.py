

try:
    m = int(input("Nhap m:"))
    n = int(input("Nhap n:"))
except Exception as e:
    print(e)
    raise Exception ("Ban nhap sai dinh dang")
print(m*(n+1))
