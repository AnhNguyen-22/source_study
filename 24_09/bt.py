import pandas as pd

def find_top3_products_by_value(df):
    # Gia tri = UnitPrice x Quantity x (1 - Discount)
    df['TotalValue'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])
    product_value = df.groupby('ProductID')['TotalValue'].sum()
    # Sap xep giam dan theo gia tri va lay top 3
    top3_products = product_value.sort_values(ascending=False).head(3)
    # Chuyen doi thanh danh sach tuple
    result = []
    for product_id, total_value in top3_products.items():
        result.append((product_id, total_value))
    return result

df = pd.read_csv('/dataset/SalesTransactions.csv')
result = find_top3_products_by_value(df)

print("=== TOP 3 SAN PHAM BAN RA CO GIA TRI LON NHAT ===")
print("Thu hang\tProductID\tTong gia tri")
print("-" * 45)
for i, (product_id, total_value) in enumerate(result, 1):
    print(f"{i}\t\t{product_id}\t\t${total_value:.2f}")

print(f"\nTong so san pham trong dataset: {df['ProductID'].nunique()}")