def winner(game):
    result=0
    pos1=game[1]
    pos2=game[2]
    pos3=game[3]
    pos4=game[4]
    pos5=game[5]
    pos6=game[6]
    pos7=game[7]
    pos8=game[8]
    pos9=game[9]
    if pos1=="X" and pos2=="X" and pos3=="X":
        result=1
    elif pos1=="X" and pos5=="X" and pos9=="X":
        result=1
    elif pos1=="X" and pos4=="X" and pos7=="X":
        result=1
    elif pos2=="X" and pos5=="X" and pos8=="X":
        result=1
    elif pos3=="X" and pos6=="X" and pos9=="X":
        result=1
    elif pos7=="X" and pos8=="X" and pos9=="X":
        result=1
    
    if pos1=="O" and pos2=="O" and pos3=="O":
        result=0
    elif pos1=="O" and pos5=="O" and pos9=="O":
        result=0
    elif pos1=="O" and pos4=="O" and pos7=="O":
        result=0
    elif pos2=="O" and pos5=="O" and pos8=="O":
        result=0
    elif pos3=="O" and pos6=="O" and pos9=="O":
        result=0
    elif pos7=="O" and pos8=="O" and pos9=="O":
        result=0
    if result==0:
        result1="The winner is O's."
    if result==1:
        result1="The Winner is X's."
    else:
        result1="There is no winner."
    return result1
list1=[0,"X",0,0,"X",0,0,"X",0,0]
print(winner(list1))


