""" 1 2 3 4                   13 9   5  1
    5 6 7 8                   14 10  6  2
    9 10 11 12                15 11  7  3
    13 14 15 16               16 12  8  4
 """
"""     narr[0][0] = arr [3][0]
        narr[0][1] = arr [2][0]
        narr[0][2] = arr [1][0]
        narr[0][3] = arr [0][0]
        narr[1][0] = arr [3][1]
        narr[1][1] = arr [2][1] """

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def rotate(arr):
    narr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        # print(i)
        for n,x in zip(range(4),range(3,-1,-1)):
            # print('here')
            narr[i][n]=arr[x][i]
    return narr

def loop(arr,rotation=0,direction='kanan'):
    rot = rotation % 4 
    a=0
    if direction == 'kiri' and rot == 1:
        rot = 3
    elif direction == 'kiri' and rot == 3:
        rot = 1
    elif rot == 0:
        a = rot
    while a<rot:
        arr = rotate(arr)
        a +=1
    return arr

def out(arr):
    z=''
    for n in range(len(arr)):
        for i  in range(len(arr)):
            z += ' ' + str(arr[n][i]) + ' '
        z += '\n'
    return z


while True:
    print(out(arr))
    arah = input('Putar kanan atau kiri :')
    jumlah = input('Berapa kali :')
    arr = loop(arr,int(jumlah),arah)
    # arr = new_arr
    print(out(arr))
    next_=input('Tekan apa pun untuk lanjut; 1 untuk Keluar :')
    if next_ == '1':
        break




