print("=" * 38)
print("\033[32:4m10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA\033[m")
print("=" * 38)

pt = int(input("Primeiro termo: "))
rz = int(input("Razão: "))

for i in range(pt, pt + 10 * rz, rz):
    print("{}".format(i), end=" > ")
print("FIM")
