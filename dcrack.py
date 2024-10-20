import pyfiglet
import os
import time
import string
import pyzipper
import PyPDF2
from itertools import product


def clear_screen():
    if os.name=='nt':
        os.system('cls')
        t1=pyfiglet.figlet_format("D-Crack")
        print(t1)
    else:
        os.system('clear')
        t1=pyfiglet.figlet_format("D-Crack")
        print(t1)


class attack():
    def zipCrack(zip_file,password):
        try:
            with pyzipper.AESZipFile(zip_file,'r',compression=pyzipper.ZIP_LZMA,encryption=pyzipper.WZ_AES) as obj:
                print(f"Trying Password : {password}")
                obj.extractall(pwd=str.encode(password))
            with open('found_zipFile_Password.txt','w') as f:
                f.write(password)
            return True
        except FileNotFoundError:
            print(f"File '{zip_file}' Not Found")
        except:
            return False
    
    def pdfCrack(pdf_file,password):
        try:
            with open(pdf_file,"rb") as pdf:
                reader = PyPDF2.PdfReader(pdf)
                if reader.is_encrypted:
                    print(f"Trying Password : {password}")
                    if reader.decrypt(password):
                        with open('found_PdfFile_Password.txt','w') as f:
                            f.write(password)
                        return True
                    else:
                        return False
        except FileNotFoundError:
            print(f"File '{pdf_file}' Not Found")


def bruteforce(kind,filename, lower, upper, digits,special, min_len=1, max_len=4):
    flag = False
    data = list()

    if lower:
        data.extend(list(string.ascii_lowercase))
        
    if upper:
        data.extend(list(string.ascii_uppercase))
        
    if digits:
        data.extend(list(string.digits))
        
    if special:
        data.extend(list(string.punctuation))
    
    if not data:
        print("Error: No character sets selected!")
        return

    if kind=="pdf":
        obj = attack.pdfCrack
    elif kind=="zip":
        obj = attack.zipCrack

    for i in range(min_len, max_len + 1):
        found_comb = product(data, repeat=i) 
        if flag:
            break
        for j in found_comb:
            flag = obj(filename, ''.join(j))
            if flag:
                print(f"Password found: {''.join(j)}")
                print("password saved successfully...")
                time.sleep(5)
                break


while True:
    clear_screen()
    print("[0] Exit\n[1] Crack ZIP File\n[2] Crack PDF File")
    choice = input(">")

    if choice=='0':
        break
    elif choice=='1' or choice=='2':
        if choice=='1':
            kind="zip"
        else:
            kind="pdf"
        filename = input("Enter file path : ")
        print("Enter '1' for yes and '0' for no")
        lower = input("include lowercase a-z  :")=='1'
        upper = input("include uppercase A-Z  :")=='1'
        digit = input("include digits 1-9     :")=='1'
        special = input("include symbols        :")=='1'


        while True:
            try:
                min_len=int(input("Enter minimum lenght of passowrd : "))
                max_len=int(input("Enter maximum length of password : "))
                break
            except:
                print("Invalid input..")
                continue
        bruteforce(kind=kind,filename=filename,lower=lower,upper=upper,digits=digit,special=special,min_len=min_len,max_len=max_len)
    else:
        continue
        



