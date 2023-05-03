N= int(input())
db =[]
for i in range(N):
  c = list(map(int, input().split()))
  db.append(c)

for i in range(N):
  if (db[i][0] > 240 and db[i][0] < 300) and\
      (db[i][1] > 160 and db[i][1] < 180) and\
      (db[i][2] >=240 and db[i][2] <=275) and\
      (db[i][3] <= 50):

        a = True
        b = db[i][4]
        break

else:
     a = False
if a:
  print(b)
else:
  print("NO DISPONIBLE")
