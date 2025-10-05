'''
import pandas as pd

def find_order_within_range(df, minValue, maxValue, SortType=True):
    """
    Tìm các hóa đơn có tổng giá trị nằm trong khoảng [minValue, maxValue]
    
    Parameters:
    - df: DataFrame chứa dữ liệu bán hàng
    - minValue: Giá trị tối thiểu
    - maxValue: Giá trị tối đa  
    - SortType: True = sắp xếp tăng dần, False = sắp xếp giảm dần
    
    Returns:
    - Danh sách các tuple (OrderID, Tổng giá trị) đã được sắp xếp
    """
    # Tính tổng giá trị cho mỗi OrderID
    order_total = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    
    # Lọc các đơn hàng trong khoảng [minValue, maxValue]
    order_within_range = order_total[(order_total >= minValue) & (order_total <= maxValue)]
    
    # Tạo danh sách các hóa đơn với mã hóa đơn + tổng giá trị
    result = []
    for order_id in order_within_range.index:
        result.append((order_id, order_within_range[order_id]))
    
    # Sắp xếp theo SortType
    if SortType:  # True = sắp xếp tăng dần
        result.sort(key=lambda x: x[1])
    else:  # False = sắp xếp giảm dần
        result.sort(key=lambda x: x[1], reverse=True)
    
    return result

# Đọc dữ liệu
df = pd.read_csv('dataset/SalesTransactions.csv')

# Nhập dữ liệu từ người dùng
minValue = float(input("Nhập giá trị tối thiểu (minValue): "))
maxValue = float(input("Nhập giá trị tối đa (maxValue): "))
sortType = input("Nhập SortType (True/False): ").lower() == 'true'

# Gọi hàm và hiển thị kết quả
result = find_order_within_range(df, minValue, maxValue, sortType)

print(f"\nCác hóa đơn có tổng giá trị trong khoảng [{minValue} - {maxValue}]:")
print("OrderID\t\tTổng giá trị")
print("-" * 30)
for order_id, total_value in result:
    print(f"{order_id}\t\t{total_value:.2f}")
print(f"\nTổng số hóa đơn tìm được: {len(result)}")
'''
import pandas as pd

def find_order_within_range(df, minValue, maxValue, SortType=True):
    order_total = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
 
    order_within_range = order_total[(order_total >= minValue) & (order_total <= maxValue)]

    result = []
    for order_id in order_within_range.index:
        result.append((order_id, order_within_range[order_id]))
    
   
    if SortType:  
        result.sort(key=lambda x: x[1])
    else:  
        result.sort(key=lambda x: x[1], reverse=True)
    
    return result

df = pd.read_csv('dataset/SalesTransactions.csv')

minValue = float(input("Nhập giá trị tối thiểu (minValue): "))
maxValue = float(input("Nhập giá trị tối đa (maxValue): "))
sortType = input("Nhập SortType (True/False): ").lower() == 'true'

result = find_order_within_range(df, minValue, maxValue, sortType)

print(f"\nCác hóa đơn có tổng giá trị trong khoảng [{minValue} - {maxValue}]:")
print("OrderID\t\tTổng giá trị")
print("-" * 30)
for order_id, total_value in result:
    print(f"{order_id}\t\t{total_value:.2f}")

print(f"\nTổng số hóa đơn tìm được: {len(result)}")
