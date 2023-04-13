from random import randint
from datetime import datetime

pos_pl = 3
pos_com = 3

def main():
    print('・'*(pos_pl - 3) + 'P' + '・'*(30 - pos_pl) + 'GOAL')
    print('・'*(pos_com - 3) + 'C' + '・'*(30 - pos_com) + 'GOAL')

main()
print('双六で遊ぼう')
pt = datetime.now()

while True:
    print('あなたの出番です')
    input('ENTER')
    pos_pl += randint(1, 6)
    if pos_pl > 30:
        pos_pl = 30
    main()
    if pos_pl == 30:
        print('あなたの勝ち')
        et = datetime.now()
        print((et - pt).seconds)
        break
    print('COMの出番です')
    input('ENTER')
    pos_com += randint(1, 6)
    if pos_com > 30:
        pos_com = 30
    main()
    if pos_com == 30:
        print('COMの勝ち')
        et = datetime.now()
        print((et - pt).seconds)
        break
    










































