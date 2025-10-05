import pandas as pd
def find_order_within_range(df, minValue, maxValue, SortType=True):
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

df=pd.read_csv('dataset/SalesTransactions.csv')
minValue=float(input("min = "))
maxValue=float(input("max = "))
result= find_order_within_range(df,minValue,maxValue)
print(minValue, '-->', maxValue, "là:", result)
