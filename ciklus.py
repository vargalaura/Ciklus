#feladat: Kérjünk be 5 egész számot és vizsgáljuk meg, hogy páros vagy páratlan!
for x in range(1,6,1):
  szam=int(input("Kérem a számot"))
  if szam % 2 == 0:
      print("Páros")
  else:
      print("Páratlan")
