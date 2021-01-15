import requests
import json
import pyfiglet
from prettytable import PrettyTable
import base64
import time
import sys
import os
#hunter io

url = "https://api.hunter.io/v2/"
xtr = "OGRmMjBiMWZiMjU0OTNhYTAxNjcyNGRkY2EzOWNlMWRiZGYzZTA2Mg=="
xtr2 = base64.b64decode(xtr)
key = xtr2.decode('utf-8')

def pToTable_exp_2(dTable):
    print(f'Jumlah Data : {len(dTable)}')
    pTable = PrettyTable()
    pTable.field_names = ['ID','Email','First Name','Last Name','Position','Company',
                          'Company Industry','Confidence Score','Website','Country Code',
                          'Company Size','linkedin url','Number Phone','Twitter','Sync Status',
                          'Notes','Sending status','Last Activity','Last Connected',
                          'Lead List ID','Lead List Name']

def pToTable_exp(dTable):
    #print(f'Jumlah Data : {len(dTable)}')
    print("Jumlah Data : ", len(dTable))
    pTable = PrettyTable()
    pTable.field_names = ['ID','Email','First Name','Last Name','Position','Company',
                          'Company Industry','Confidence Score','Website','Country Code',
                          'Company Size','Number Phone','Twitter']
    pTable.align = 'l'
    no = 0
    for x in dTable:
        no += 1
        rDetail = [x['id'],x['email'],x['first_name'],x['last_name'],x['position'],x['company'],
                   x['company_industry'],x['confidence_score'],x['website'],x['country_code'],
                   x['company_size'],x['phone_number'],x['twitter']]
        pTable.add_row(rDetail)
    print(pTable)
    print('\r')

def S_lead():
    print(pyfiglet.figlet_format("Cari Lead", font="digital"))
    sId = input("Masukan User ID : ")
    #hat = {"Content-type": "Application/Json"}
    rekt = requests.get(url+"leads/"+sId+"?api_key="+key)
    if rekt.status_code == 200:
        r = rekt.text
        data = json.loads(r)
        rekt2 = data["data"]
        pToTable_exp([rekt2])
    else:
        print(rekt.status_code)
        print("gak ada datanya cok")
        print('\r')

def L_lead():
    print(pyfiglet.figlet_format("List Lead", font="digital"))
    rekt = requests.get(url+"leads?api_key="+key).text
    data = json.loads(rekt)
    rekt2 = data["data"]
    rekt4 = rekt2["leads"]
    rekt41 = data["meta"]
    if rekt41["count"] ==0:
        print("Gak ada leads cok")
    else:
        pToTable_exp(rekt4)

def C_lead_data():
    global data, email, fName, lName, position, company, cIndustry, cSize, cScore
    global cScore, website, pNumber, twitter, cusAtt
    email = input("Masukan E-mail : ")
    fName = input("Masukan Nama Awal : ")
    lName = input("Masukan Nama Akhir :")
    position = input("Masukan Posisi : ")
    company = input("Masukan Perusahaan : ")
    mField = input("Perlu data tambahan[ex: industry][y/n] ? >")
    if mField == "y":
        cIndustry = input("Masukan tipe perusahaan : ")
        cSize = input("Masukan jumlah pegawai : ")
        cScore = input("Masukan Nilai Rating(0-100) : ")
        website = input("Masukan Website Perusahaan anda : ")
        pNumber = input("Masukan nomer telepon anda : ")
        twitter = input("Masukan username twitter anda : ")
        cusAtt = input("Masukan kode anda : ")
        data = {
            "email": email, "first_name": fName, "last_name": lName,
            "position": position, "company": company, "company_industry": cIndustry,
            "company_size": cSize, "confidence_score": cScore, "website": website,
            "phone_number": pNumber, "twitter": twitter,
            "custom_attributes": {
                "customer_id": cusAtt
            }
        }
    else:
        data = {"email": email, "first_name": fName, "last_name": lName,
                "position": position, "company": company}
    return data

def C_lead():
    print(pyfiglet.figlet_format("Create Lead", font="digital"))
    C_lead_data()
    hat = {"Content-type": "Application/Json"}
    rekt = requests.post(url+"leads?api_key="+key, json=data, headers=hat)
    if rekt.status_code == 201:
        print("Sukses bikin user ")
    else:
        print(rekt.status_code)
        print("Gagal bikin cok")

def U_lead():
    print(pyfiglet.figlet_format("Update lead", font="digital"))
    tUID = input("tampilkan user ID ?[y/n] >")
    if tUID == "y":
        L_lead()
    else:
        pass
    mUID = input("Masukan ID : ")
    C_lead_data()
    hat = {"Content-type": "Application/Json"}
    rekt = requests.put(url+"leads/"+mUID+"?api_key="+key,json=data, headers=hat)
    if rekt.status_code == 204:
        print("Sukses update user "+mUID)
    else:
        print(rekt.status_code)
        print("Gagal update cok")

def C_lead_exp():
    data = {
            "email": "dustin@asana.com",
            "first_name": "Dustin",
            "last_name": "Moskovitz",
            "position": "Co-founder",
            "company": "Asana",
            "company_industry": "Internet and Telecom",
            "company_size": "201-500 employees",
            "confidence_score": 95,
            "website": "asana.com",
            "phone_number": "720-555-6251",
            "twitter": "moskov",
            "custom_attributes": {
              "customer_id": "cus-1234abcd"
                }
            }
    hat = {"Content-type":"Application/Json"}
    rekt = requests.post(url+"leads?api_key="+key, json=data, headers=hat)
    print(rekt)
    skop = rekt.text
    data = json.loads(skop)
    print(data["data"])

def D_lead():
    #id 71455354
    print(pyfiglet.figlet_format("Delete Lead ", font="digital"))
    id = input("Masukan User ID : ")
    hat = {"Content-type": "Application/Json"}
    rekt = requests.delete(url+"leads/"+id+"?api_key="+key, headers=hat)
    #print(rekt)
    if rekt.status_code == 204 :
        print('Sukses Delete User ID = '+id)
        print('\r')
        L_lead()
    else:
        print(rekt)
        print('\r')

def readMe():
    print('\r')
    with open("README.md", "r", encoding="utf-8") as fh:
        print(fh.read())
    print('\r')
def Menu():
    print(pyfiglet.figlet_format("Hunter IO", font="digital"))
    print("1. List Lead")
    print("2. Search Lead")
    print("3. Create Lead")
    print("4. Update Lead")
    print("5. Delete Lead")
    print("6. Baca Akuu >...< ")
    print("0. Keluar")
    menu = int(input("Pilih Menu >"))
    os.system('cls')
    if menu == 1:
        L_lead()
    elif menu == 2:
        S_lead()
    elif menu == 3:
        C_lead()
    elif menu == 4:
        U_lead()
    elif menu == 5:
        D_lead()
    elif menu == 6:
        readMe()
    elif menu == 0:
        animation = "|/-\\"
        for i in range(25):
            time.sleep(0.1)
            sys.stdout.write("\r " + animation[i % len(animation)])
            sys.stdout.flush()
        print('\r')
        print(pyfiglet.figlet_format("babai :v ", font="digital"))
        exit()
    else:
        print("Salah pilih")
        print("Ulangin")

if __name__ == "__main__":
    while(True):
        Menu()

kmz = "8df20b1fb25493aa016724ddca39ce1dbdf3e062"