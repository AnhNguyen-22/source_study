import sqlite3
import pandas as pd
from typing import Optional


def get_customers_with_min_invoices(db_path: str, min_invoices: int) -> pd.DataFrame:
    """
    Trả về DataFrame danh sách Customer có số lượng Invoice >= min_invoices.

    Columns:
    - CustomerId, FirstName, LastName, Company, Email, Phone, Country, Invoices
    """
    conn: Optional[sqlite3.Connection] = None
    try:
        conn = sqlite3.connect(db_path)
        query = (
            """
            SELECT c.CustomerId,
                   c.FirstName,
                   c.LastName,
                   c.Company,
                   c.Email,
                   c.Phone,
                   c.Country,
                   COUNT(i.InvoiceId) AS Invoices
            FROM Customer c
            LEFT JOIN Invoice i ON i.CustomerId = c.CustomerId
            GROUP BY c.CustomerId, c.FirstName, c.LastName, c.Company, c.Email, c.Phone, c.Country
            HAVING COUNT(i.InvoiceId) >= ?
            ORDER BY Invoices DESC, c.CustomerId ASC
            """
        )
        df = pd.read_sql_query(query, conn, params=(min_invoices,))
        return df
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Đường dẫn DB tương đối từ thư mục 24_09
    db_path = "database/Chinook_Sqlite.sqlite"
    n = 3  # ví dụ: khách hàng có >= 5 hóa đơn
    result_df = get_customers_with_min_invoices(db_path, n)
    print(result_df.head())
    print(f"\nTổng số khách hàng có >= {n} invoice: {len(result_df)}")
