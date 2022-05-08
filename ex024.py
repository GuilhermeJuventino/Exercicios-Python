cidade = str(input("Em que cidade você nasceu? ")).lower().strip()

print("O nome de sua cidade começa com Santo? {}".format(cidade[:5] == "santo"))
