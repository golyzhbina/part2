with open("ikea.txt", "r", encoding="utf-8") as out:
   data = list(map(lambda x: x.strip().split(), out.readlines()))

