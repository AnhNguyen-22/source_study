from bs4 import BeautifulSoup

with open('dataset/SalesTransactions.xml', 'r') as f:
    data=f.read()

bs_data=BeautifulSoup(data, 'xml')

UelSample=bs_data.find_all('UelSample')
print(UelSample)

#-----------------------------------------------------------
import pandas_read_xml as pdx
df=pdx.read_xml("dataset/SalesTransactions.xml", ['UelSample', 'SalesItem'])
print(df) #đọc file
print(df.iloc[0]) #in dữ liệu ở dòng thứ 0
data=df.iloc[0] #đặt biến data=dữ liệu ở dòng thứ 0

print(data[0]) #in data dòng 0
print(data[1]) #in data dòng 1
print(data[1]["OrderID"]) #in giá trị của orderid ở dòng 1