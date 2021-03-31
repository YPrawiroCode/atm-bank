from random import randint
import datetime

from customer import Customer

atm = Customer(id)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

cardNumber = random_with_N_digits(1)

while True:
    print("\n1. Create an account \n2. Log into account \n0. Exit")

    selectmenu1 = int(input("\nSilakan pilih menu: ")) 
    
    if selectmenu1 == 1:
        print("Your card has been created" )
        
        print ("Your card number:",cardNumber)
        print ("Your Card PIN:",atm.checkPin())

    elif selectmenu1 == 2:
        while True:              
            user = int(input("Enter your card number:"))
            pin = int(input("Enter your PIN:"))
            trial = 0

            while ((pin != int(atm.checkPin()) or user != cardNumber) and trial < 3):
                user = int(input("Pin atau nomor kartu anda salah. Silakan Masukkan lagi Card Number Anda: "))
                pin = int(input("Pin atau nomor kartu anda salah. Silakan Masukkan lagi PIN anda: "))
                trial += 1

                if trial == 3:
                    print("Error. Silakan ambil kartu dan coba lagi..")
                    exit()
            
            while True:
                print("You have successfully logged in!")
                print("\n1. Balance \n 2. Add Income \n 3. Transfer money \n 4. Close account \n 5. Log out \n 0.Exit ")

                selectmenu = int(input("\nSilakan pilih menu: ")) 

                if selectmenu == 1:
                    print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n" )
                elif selectmenu == 2:
                    nominal = float(input("Masukkan nominal saldo: "))
                    verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(nominal) + " ")
                    
                    if verify_withdraw == "y":
                        print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
                    else:
                        break
                    if nominal < atm.checkBalance():
                        atm.withdrawBalance(nominal)
                        print("Transaksi debet berhasil!")
                        print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
                    else:
                        print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                        print("Silakan lakukan penambahan nominal saldo")

                elif selectmenu == 3:
                    nominal = float(input("Masukkan nominal saldo: "))
                    verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")

                    if verify_deposit == "y":
                        atm.depositBalance(nominal)
                        print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n" )
                    else:
                        break

                elif selectmenu == 4:
                    verify_pin = int(input("masukkan pin anda: "))

                    while verify_pin != int(atm.checkPin()):
                        print("pin anda salah, silakan masukkan pin:")

                    updated_pin = int(input("silakan masukkan pin baru: "))
                    print("pin anda berhasil diganti!")

                    verify_newpin = int(input("coba masukkan pin baru: "))

                    if verify_newpin == updated_pin:
                        print("pin baru anda sukses!")
                    else:
                        print("maaf, pin anda salah! ")

                elif selectmenu == 5:
                    print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
                    print("No. Rekord: ", random_with_N_digits(5))
                    print("Tanggal: ", datetime.datetime.now())
                    print("Saldo akhir: ", atm.checkBalance())
                    print("Terima kasih telah menggunakan ATM Progate!")
                    exit()
                
                 elif selectmenu == 0:
                     exit()
            else:
                print("Error. Maaf, menu tidak tersedia")
        
    elif selectmenu1 == 0:
        exit()

else:
    print("Error. Maaf, menu tidak tersedia")