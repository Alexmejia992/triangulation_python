def sector(x  ,y):
    if(2<= x <=8 and 3<= y <=9):
        x = round(x)
        y = round(y)
        # Sector Lineas rojas
        if(x == 5 and y in range(7, 9+1)):
            print('Deniska está entre el Sector 1 y 2')
        elif(x == 5 and y in range(3,5+1)):
            print('Deniska está entre el Sector 3 y 4')
        elif(x in range(2,4+1) and y == 6):
            print('Deniska está entre el Sector 1 y 3')
        elif(x in range(6,8+1) and y == 6):
            print('Deniska está entre el Sector 2 y 4')
        # Sector donde se encuentra Deniska
        elif(x in range(1,4+1) and y in range(7,9+1)):
            print('S1')
        elif(x in range(6,8+1) and y in range(7,9+1)):
            print('S2')
        elif(x in range(2,4+1) and y in range(3,5+1)):
            print('S3')
        elif(x in range(6,8+1) and y in range(3,5+1)):
            print('S4')
        # Zona de antenas
        elif(x in range(2,8+1,3) and y in range(3,9+1,3)):
            pass  
    # Fuera de triangulación
    else:
        print('Deniska ha escapado')
    
sector(8.1, 9.1)