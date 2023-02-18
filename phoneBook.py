#membuat modul phone book
import os

def openContact():
    file = open("PhoneBooks.txt","r")
    print(file.read())
    file.close()

def addContact(nama,nomor):
    file = open("PhoneBooks.txt", "a")
    file.write(nama + ":" + nomor + "\n")
    file.close()

def findContact(nama):
    with open(r'PhoneBooks.txt', 'r') as file:
        # read all content from a file using read()
        content = file.read()
        # check if string present or not
        if nama in content:
            print('nama yang anda cari : '+ nama + ", ada dalam daftar kontak"  )
        else:
            print('string does not exist')

def delContact(nama):
    with open("PhoneBooks.txt",'r') as file:
        lines = file.readlines()

    with open("PhoneBooks.txt",'w') as file:
        for line in lines:
        # find() returns -1 if no match is found
            if line.find(nama) != -1:
                pass
            else:
                file.write(line)

def updateContact(nomorLama,nomorBaru):
    # creating a variable and storing the text
    # that we want to search
    nomor1 = nomorLama
  
    # creating a variable and storing the text
    # that we want to add
    nomorBaru2 = nomorBaru
  
    # Opening our text file in read only
    # mode using the open() function
    with open(r'PhoneBooks.txt', 'r') as file:
  
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
        data = file.read()
  
    # Searching and replacing the text
    # using the replace() function
        data = data.replace(nomorLama, nomorBaru)
  
    # Opening our text file in write only
    # mode to write the replaced content
    with open(r'PhoneBooks.txt', 'w') as file:
  
    # Writing the replaced data in our
    # text file
        file.write(data)
    




#main program
while True:
    print("========PhoneBooks========")
    print("1. Buka PhoneBook")
    print("2. Tambah Nomor")
    print("3. Hapus Nomor")
    print("4. Cari Nomor")
    print("5. Update Nomor")

    angka = input("Masukkan pilihan : ")
    if  angka=="1":
        openContact()
    elif angka =="2":
        nama = input("Masukkan nama : ")
        nomor = input("Masukkan nomor : ") 
        addContact(nama,nomor)
    elif angka=="3":
        nama=input("Ketik nama kontak yang akan dihapus : ")
        delContact(nama)
    elif angka=="4":
         nama = input("ketik nama yang dicari : ")
         findContact(nama)
    elif angka=="5":
        nomorLama = input("Masukkan nomor lama yang akan diganti : ")
        nomorBaru = input("Masukkan nomor barunya : ")
        updateContact(nomorLama,nomorBaru)
        print("nomor berhasil diupdate")
        

    

