import getpass
import os
import time
import sys

#bagian awal
def header():
    os.system("cls")
    delay_print2("Tic Tac Toe V1.2\n")
    time.sleep(0.5)
    input("Press Enter to continue...")
    os.system("cls")
    print("Loading")
    delay_print1("==============================")
    time.sleep(0.5)
    os.system("cls")
    print("Loading berhasil")
    time.sleep(1)
    os.system("cls")

def delay_print1(x):
    for a in x:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.05)

def delay_print2(x):
    for a in x:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.15)



#menampilkan angka dan lokasi
def howto():
    print(" 7 || 8 || 9 ")
    print("=============")
    print(" 4 || 5 || 6 ")
    print("=============")
    print(" 1 || 2 || 3 \n")
    print("Hafalkan angka dan lokasinya")



#memanggil fungsi header
header()
#menampilkan how to
howto()


pertanyaan2 = input("Siap bermain? Y/N = ").upper()

if (pertanyaan2 == "Y"):

    os.system("cls")

    tictac = True
    while tictac:
        def gkb(player1,player2):
                if player1 == "B" and player2 == "K":
                    return "player2 menang!!!"
                elif player1 == "B" and player2 == "G":
                    return "player1 menang!!!"
                elif player1 == "K" and player2 == "B":
                    return "player1 menang!!!"
                elif player1 == "K" and player2 == "G":
                    return "player2 menang!!!"
                elif player1 == "G" and player2 == "K":
                    return "player1 menang!!!"
                elif player1 == "G" and player2 == "B":
                    return "player2 menang!!!"
                elif player1 == player2:
                    return "tie"
                else:
                    return "Wrong Input"       


        def gkb_game():
            jalan = True
            while jalan:    
            
                player1 = getpass.getpass("Player1 B batu ,K kertas,G gunting : ").upper()
                while player1 not in ["G", "B", "K"]:
                    print("input salah, masukan G, K, B saja")
                    player1 = getpass.getpass("Player1 B batu ,K kertas,G gunting : ").upper()     

                player2 = getpass.getpass("Player2 B batu ,K kertas,G gunting : ").upper()    
                while player2 not in ["G", "B", "K"]:
                    print("input salah, masukan G, K, B saja")
                    player2 = getpass.getpass("Player2 B batu ,K kertas,G gunting : ").upper()     


                if gkb(player1,player2) == "player2 menang!!!" or gkb(player1,player2) == "player1 menang!!!":
                    print(gkb(player1,player2))
                    jalan = False
                else:
                    print(gkb(player1,player2))
                    jalan = True   


        #LIST papan
        papan = ["", "", "", 
                 "", "", "", 
                 "", "", ""]       


        #papan utama
        def papan_tic():
            print(papan[6], "  || ", papan[7], " || ", papan[8])
            print("=============")
            print(papan[3], "  || ", papan[4], " || ", papan[5])
            print("=============")
            print(papan[0], "  || ", papan[1], " || ", papan[2])       


        #buat looping game
        game_jalan = True
        #fungsi permainan
        def game():
            global tictac
            papan_tic() 
            while game_jalan:
                giliran(current_player)
                check_game()
                flip()
            if (winner == "X" or winner == "O"):
                print(winner, "menang")
                tictac = False
            elif winner == None:
                print("Tied.")     


        #fungsi giliran untuk pemain
        def giliran(player):
        
           #menampilkan giliran siapa
           print(player, "turn.")
           #inputan untuk posisi 1 sampai 9 
           posisi = input("Pilih posisi anda 1-9: ")       

           valid = False
           while not valid:
               while posisi not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                   posisi = input("Pilih posisi anda 1-9: ")       

           #posisi dikurang 1 (input 1 = papan[0])
               posisi = int(posisi) - 1        

               if papan[posisi] == "":
                   valid = True
               else:
                   print("NOT ALLOWED")
           os.system("cls")
           papan[posisi] = player
           papan_tic() 


        #game checking
        def check_game():
            check_win()
            check_tie()    

        #set winner diawal sebagai None
        winner = None      

        #check menang
        def check_win(): 
            global winner      

            #pemenang di row
            row_winner = check_row()       

            #pemenang di coloumns
            columns_winner = check_columns()       

            #pemenang di diagonals
            diagonals_winner = check_diagonals()       

            if row_winner:
                winner = row_winner
            elif columns_winner:
                winner = columns_winner
            elif diagonals_winner: 
                winner = diagonals_winner
            else:
                winner = None
            return     


        #check row
        def check_row():
            global game_jalan      

            #urutan row yang menang
            row1 = papan[6] == papan[7] == papan[8] !=""
            row2 = papan[3] == papan[4] == papan[5] !=""
            row3 = papan[0] == papan[1] == papan[2] !=""       

            if row1 or row2 or row3:
                game_jalan = False
            if row1:
                return papan[6]
            elif row2:
                return papan[3]
            elif row3:
                return papan[0]
            return     


        #check columns
        def check_columns():
            global game_jalan      

            #urutan columns yang menang
            columns1 = papan[6] == papan[3] == papan[0] !=""
            columns2 = papan[7] == papan[4] == papan[1] !=""
            columns3 = papan[8] == papan[5] == papan[2] !=""       

            if columns1 or columns2 or columns3:
                game_jalan = False
            if columns1:
                return papan[6]
            elif columns2:
                return papan[7]
            elif columns3:
                return papan[8]
            return     


        #check diagonals
        def check_diagonals():
            global game_jalan      

            #urutan diagonal yang menang
            diagonals1 = papan[6] == papan[4] == papan[2] !=""
            diagonals2 = papan[8] == papan[4] == papan[0] !=""     

            if diagonals1 or diagonals2:
                game_jalan = False
            if diagonals1:
                return papan[6]
            elif diagonals2:
                return papan[8]
            return     


        #check jika tie
        def check_tie():
            global game_jalan
            if "" not in papan:
                game_jalan = False
            return     


        #fungsi menukar giliran player
        def flip():
            global current_player
            if current_player == "X":
                current_player = "O"
            elif current_player == "O":
                current_player = "X"
            return 

        gkb_game()
        current_player = input("Masukan X/O: ").upper()
        game()
        if winner == None:
            restart=input("Apakah mau rematch? Y/N: ").upper()
            if restart == "Y":
                os.system("cls")
                pass
            elif restart == "N":
                print("Sampai jumpa")
                break
            else:
                print("Input salah. Silahkan restart program")
                break
        else:
            pass   

elif (pertanyaan2 == "N"):
    print("Sampai jumpa")  

else:
    print("Input salah. Silahkan restart program")



  




