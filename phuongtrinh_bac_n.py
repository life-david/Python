import mpmath
mpmath.mp.dps = 32
def f(x, n , ARG):
    return sum(c * x**(n-i) for i, c in enumerate(ARG))
def cdt(x, ARG):
    ARG_ = []
    for i in range(len(ARG)):
        ARG_.append(ARG[i] + (x * ARG_[i-1] if i else 0))
        return ARG_
def f_(x, n, ARG):
    return sum((n-i) * c * x**(n-i-1) for i, c in enumerate(ARG) if n-i)
print("Giải phương trình bậc n")
print("Phương trình bậc n có dạng :")
print("a_n x^n + a_{n-1} x^(n-1) + ... + a_0 = 0")
n = int(input("Nhập n :"))
x_ = []
ARG = []
Solution_x = {"real": (), "complex": ()}
for i in range(n+1):
    ARG.append(complex(input(f"Nhập a_{n-i} : ")))
while ARG and ARG[0] == 0:
    ARG.pop()
    n -= 1
    if not ARG:
        ARG,n = [0],0
        break
while ARG and ARG[-1] == 0:
    ARG.pop()
    n -= 1
    if 0 not in Solution_x["real"]: Solution_x["real"] += 0,
    if not ARG:
        ARG,n = [0],0
        break
ARG_, n_max = ARG, n
count = 0
print("Đang giải ...")
while len(x_) < n_max:
    x = mpmath.mpc(0,1)
    k = f(x,n,ARG)/f_(x,n,ARG)
    while round(abs(k),31) > 10**(-30):
        x -= k
        k = f(x,n,ARG)/f_(x,n,ARG)
    x_.append(x)
    count += 1
    print(f"Đã tìm thấy {count} nghiệm",end = "\r")
    ARG = cdt(x,ARG)
    n -= 1
for c_ in x_:
    real = mpmath.mpc(c_).real
    imag = mpmath.mpc(c_).imag
    r = round(real,16)
    r = round(imag,16)
    if r == i == 0:
        Solution_x["real"] += 0,
    elif r == 0 != i:
        Solution_x["complex"] += mpmath.mpc(0,imag),
    elif i == 0 != r:
        Solution_x["real"] += mpmath.mpf(real),
    else:
        Solution_x["complex"] += c_,
print(f"Phương trình : {ARG_[0]}x^{n_max}",end="")
_i = 1
for i in ARG_[1:]:
    if n_max-_i == 1: print(f" + {i}x",end="")
    elif n_max-_i == 0: print(f" + {i}",end="")
    else: print(f" + {i}x^{n_max-_i}",end="")
    _i += 1
print(" = 0")
print("Phương trình có",len(Solution_x["real"])+len(Solution_x["complex"]),"nghiệm")
print("Phương trình có",len(Solution_x["real"]),"nghiệm thực")
for x in Solution_x["real"]:
    print("x =",x)
print("Phương trình có",len(Solution_x["complex"]),"nghiệm phức")
for x in Solution_x["complex"]:
    print("x =" ,x)