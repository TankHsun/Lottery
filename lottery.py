import random
a = int(input('請選擇 [0] 頭獎 [1] 貳獎 [2] 參獎 [3] 肆獎:'))
point_all = 12 - a
awards = ['頭獎', '貳獎', '參獎', '肆獎']
print('中了', awards[a], '停止')

def lotto():
  ticket = set()
  while len(ticket) < 6:
    ticket.add(random.randint(1,49))
  return ticket

prize = lotto()
print('開獎前六碼:', prize)
while True:
  special = random.randint(1,49)
  if not special in prize:
    break
print('特別號:', special)

times = 0
while True:
  lottery = lotto()
  times += 1
  same = lottery.intersection(prize)
  point = len(same) * 2
  if special in lottery:
    point += 1
  if point >= point_all:
    break
print('中了的彩券:', lottery) 
print('中了的數字:', same) 
print('特別號有無中:', special in lottery) 
print('買了', times, '張才中了', awards[12- point])