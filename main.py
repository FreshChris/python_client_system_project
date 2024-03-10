import pandas as pd

input_data = "1. Add new client details/record.\n2. Search client details (Client ID).\n3. Remove any client details.\n4. Print all the client’s details.\n5. Order the stored client's details.\n6. Save the client's details into the file.\n7. Exit.\n"
data_c = {}
Input_c = 1
SL = 1


def client_F(SL, Input_c):
    if SL == 1:
        client = {}
        client["Name_"] = input("Enter Name:  ")
        client["Address_"] = input("Enter Address:  ")
        client["Phone_Number_"] = input("Enter PhoneNumber:  ")
        client["Email_ID"] = input("Enter Email Address:  ")
        client["Product_Details"] = input("Enter Product_Details:-  ")
        data_c[Input_c] = client
        Input_c += 1
    if SL == 2:
        data = int(input("Enter Client ID:  "))
        if data in data_c:
            print(data_c[data])
        else:
            print("Not available  in database.  ")
    if SL == 3:
        d = int(input("Enter Client ID:  "))
        if d in data_c:
            del data_c[d]
            print("Client data deleted.  ")
        else:
            print("ID not Found  ")
    if SL == 4:
        print(data_c)
        SL = int(input(input_data))
    if SL == 5:
        for i in sorted(data_c, key=lambda x: data_c[x]['Name_']):
            print(data_c[i])
    if SL == 6:
        data_f = pd.DataFrame.from_dict(data_c)
        data_f1 = data_f.T
        data_f1.to_csv('Client_Data.csv', index=False)


while SL != 7:
    SL = int(input(input_data))
    client_F(SL, Input_c)
    if SL == 1:
        Input_c += 1


