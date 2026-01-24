```python
import pandas as pd 
import numpy as np 
df = pd.read_csv("unclean_data.csv")

print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
```

    Loaded Dataset: 5000 rows, 11 columns



```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 11 columns):
     #   Column                   Non-Null Count  Dtype 
    ---  ------                   --------------  ----- 
     0   USER_ID                  5000 non-null   object
     1   ORDER_ID                 5000 non-null   object
     2   PURCHASE_TS              5000 non-null   object
     3   SHIP_TS                  5000 non-null   object
     4   PRODUCT_NAME             5000 non-null   object
     5   PRODUCT_ID               5000 non-null   object
     6   GBP_PRICE                5000 non-null   object
     7   PURCHASE_PLATFORM        5000 non-null   object
     8   MARKETING_CHANNEL        4907 non-null   object
     9   ACCOUNT_CREATION_METHOD  4893 non-null   object
     10  CITY                     4903 non-null   object
    dtypes: object(11)
    memory usage: 429.8+ KB



```python
# =========================
# Step 1: HEADER CLEANING 
# =========================

print(df.columns.tolist())

df.columns = df.columns.str.strip().str.lower()

print("FIX APPLIED")
print(df.columns.tolist())
```

    ['USER_ID', 'ORDER_ID', 'PURCHASE_TS', 'SHIP_TS', 'PRODUCT_NAME', 'PRODUCT_ID', 'GBP_PRICE', 'PURCHASE_PLATFORM', 'MARKETING_CHANNEL', 'ACCOUNT_CREATION_METHOD', 'CITY']
    FIX APPLIED
    ['user_id', 'order_id', 'purchase_ts', 'ship_ts', 'product_name', 'product_id', 'gbp_price', 'purchase_platform', 'marketing_channel', 'account_creation_method', 'city']



```python
# =========================
# Step 2: CASE FORMATTING
# =========================

print(df['marketing_channel'].unique())
print(df['purchase_platform'].unique())
print(df['account_creation_method'].unique())
print(df['city'].unique())

df['marketing_channel'] = df['marketing_channel'].str.strip().str.lower()
df['purchase_platform'] = df['purchase_platform'].str.strip().str.lower()
df['account_creation_method'] = df['account_creation_method'].str.strip().str.lower()
df['city'] = df['city'].str.strip().str.lower()

print("FIX APPLIED")

print(df['marketing_channel'].unique())
print(df['purchase_platform'].unique())
print(df['account_creation_method'].unique())
print(df['city'].unique())

```

    ['EMAIL' 'search' 'affiliate' ' direct ' 'direct' 'social' 'email'
     'DIRECT' 'SEARCH' nan 'AFFILIATE' ' AFFILIATE ' ' email ' 'SOCIAL'
     ' affiliate ' ' SOCIAL ' ' social ' ' SEARCH ' ' DIRECT ' ' EMAIL '
     ' search ']
    ['website' 'mobile_app' 'WEBSITE' 'MOBILE_APP']
    ['desktop' 'mobile' 'unknown' 'UNKNOWN' 'MOBILE' nan 'DESKTOP']
    ['LEEDS' 'Manchester' 'Birmingham' 'MANCHESTER' 'GLASGOW' nan 'Leicester'
     'Leeds' 'London' 'Liverpool' 'LONDON' 'Glasgow' 'Bristol' 'Sheffield'
     'BIRMINGHAM' 'LEICESTER' 'Nottingham' 'BRISTOL' 'Londn' 'LIVERPOOL'
     'NOTTINGHAM' 'Glasow' 'Manchster' 'SHEFFIELD']
    FIX APPLIED
    ['email' 'search' 'affiliate' 'direct' 'social' nan]
    ['website' 'mobile_app']
    ['desktop' 'mobile' 'unknown' nan]
    ['leeds' 'manchester' 'birmingham' 'glasgow' nan 'leicester' 'london'
     'liverpool' 'bristol' 'sheffield' 'nottingham' 'londn' 'glasow'
     'manchster']



```python
# =============================
# Step 3: TYPOS CITY COLUMN
# =============================

print(df['city'].unique())

cleanup_map = {
    'londn':'london',
    'glasow':'glasgow',
    'manchster':'manchester' 
}

df['city'] = df['city'].replace(cleanup_map)

print("FIX APPLIED")

print(df['city'].unique())

```

    ['leeds' 'manchester' 'birmingham' 'glasgow' nan 'leicester' 'london'
     'liverpool' 'bristol' 'sheffield' 'nottingham' 'londn' 'glasow'
     'manchster']
    FIX APPLIED
    ['leeds' 'manchester' 'birmingham' 'glasgow' nan 'leicester' 'london'
     'liverpool' 'bristol' 'sheffield' 'nottingham']



```python
# ====================================
# Step 4: PRODUCT NAME AND PRICE MATCH 
# ====================================

print(df['product_name'].unique())
print(df['gbp_price'].unique())

price_map = {
    'Accessory': 24.99,
    'Steam Deck': 499.99,
    'Kindle Paperwhite': 129.99,
    'PS5': 479.99,
    'Google Pixel 8': 699.99,
    'Smartwatch': 249.99,
    'Xbox Series X': 449.99,
    'AirPods': 159.99,
    'Nintendo Switch': 299.99,
    'MacBook Air': 1199.99,
    'iPhone 15': 899.99
}

df.loc[df['product_name'].isin(price_map.keys()), 'gbp_price'] = (
    df['product_name'].map(price_map)
)


print("FIX APPLIED")
print(df['product_name'].unique())
print(df['gbp_price'].unique())


```

    ['Accessory' 'Steam Deck' 'Kindle Paperwhite' 'MacBook Air' 'iPhone 15'
     'Smartwatch' 'Google Pixel 8' 'PS5' 'Xbox Series X' 'AirPods'
     'Nintendo Switch']
    ['24.99' '499.99' '129.99' '1199.99' '899.99' '249.99' '699.99' '479.99'
     '499.99 GBP' 'gbp 499.99' '449.99' '449.99 GBP' 'gbp 699.99' '159.99'
     '£ 449.99' '£ 249.99' '299.99' '499.99,00' '479.99,00' '£24.99' '€899.99'
     '€479.99' '249.99,00' '24.99 GBP' '£ 1199.99' '479.99 GBP' 'gbp 129.99'
     '249.99 GBP' '£ 129.99' '£449.99' '£ 499.99' '299.99 GBP' '£499.99'
     '€249.99' '€499.99' '£ 159.99' '€24.99' '299.99,00' 'gbp 24.99'
     '159.99 GBP' '£479.99' '€1199.99' '€299.99' 'gbp 449.99' 'gbp 299.99'
     '£249.99' '£129.99' '1199.99 GBP' '£899.99' '1199.99,00' '£ 699.99'
     '159.99,00' 'gbp 479.99' '449.99,00' '£1199.99' '899.99 GBP' '£ 899.99'
     '129.99,00' '699.99,00' 'gbp 1199.99' '699.99 GBP' '24.99,00' '€129.99'
     '129.99 GBP' 'gbp 249.99' '£ 299.99' '£699.99' '€699.99' '£299.99'
     'gbp 899.99' '899.99,00' 'gbp 159.99' '€449.99' '£ 24.99' '12000'
     '£ 479.99' '£159.99' '€159.99']
    FIX APPLIED
    ['Accessory' 'Steam Deck' 'Kindle Paperwhite' 'MacBook Air' 'iPhone 15'
     'Smartwatch' 'Google Pixel 8' 'PS5' 'Xbox Series X' 'AirPods'
     'Nintendo Switch']
    [24.99 499.99 129.99 1199.99 899.99 249.99 699.99 479.99 449.99 159.99
     299.99]



```python
# ================================
# Step 4: PRICE COLUMN TYPE CHANGE  
# ================================

print("Dtype", df['gbp_price'].dtype)

df['gbp_price'] = df['gbp_price'].astype(float)

print("FIX APPLIED")

print("Dtype", df['gbp_price'].dtype)
```

    Dtype object
    FIX APPLIED
    Dtype float64



```python
# ========================================
# Step 5: PURCHASE DATE COLUMN TYPE CHANGE  
# ========================================

print(df['purchase_ts'].unique()[:10])
print("Dtype", df['purchase_ts'].dtype)

df['purchase_ts'] = df['purchase_ts'].str.strip().str.replace('-', '/', regex=False)


def parse_mixed_date(x): # some dates where mixed between DD/MM/YYYY & MM/DD/YYYY 
    try:
        dt = pd.to_datetime(x, format='%m/%d/%Y')
    except ValueError:
        dt = pd.to_datetime(x, format='%d/%m/%Y')
    return dt


df['purchase_ts'] = df['purchase_ts'].apply(parse_mixed_date).dt.strftime('%d/%m/%Y')
df['purchase_ts'] = pd.to_datetime(df['purchase_ts'], format='%d/%m/%Y')


print("FIX APPLIED")
print(df['purchase_ts'].unique()[:10])
print("Dtype", df['purchase_ts'].dtype)
num_missing = df['purchase_ts'].isna().sum()
print("NaT values:", num_missing)


```

    ['11/06/2025' '23/03/2025' '24/04/2025' '02/06/2025' '22/03/2025'
     '10/04/2025' '15/02/2025' '07/05/2025' '14/06/2025' '20/01/2025']
    Dtype object
    FIX APPLIED
    <DatetimeArray>
    ['2025-11-06 00:00:00', '2025-03-23 00:00:00', '2025-04-24 00:00:00',
     '2025-02-06 00:00:00', '2025-03-22 00:00:00', '2025-10-04 00:00:00',
     '2025-02-15 00:00:00', '2025-07-05 00:00:00', '2025-06-14 00:00:00',
     '2025-01-20 00:00:00']
    Length: 10, dtype: datetime64[ns]
    Dtype datetime64[ns]
    NaT values: 0



```python
# =======================================
# Step 6: SHIP DATE  COLUMN TYPE CHANGE  
# =======================================

print(df['ship_ts'].unique()[:10])
print("Dtype", df['ship_ts'].dtype)

df['ship_ts'] = df['ship_ts'].str.strip().str.replace('-', '/', regex=False)

def parse_mixed_date(x): # some dates where mixed between DD/MM/YYYY & MM/DD/YYYY 
    try:
        dt = pd.to_datetime(x, format='%m/%d/%Y')
    except ValueError:
        dt = pd.to_datetime(x, format='%d/%m/%Y')
    return dt

df['ship_ts'] = df['ship_ts'].apply(parse_mixed_date).dt.strftime('%d/%m/%Y')
df['ship_ts'] = pd.to_datetime(df['ship_ts'], format='%d/%m/%Y')

print("FIX APPLIED")
print(df['ship_ts'].unique()[:10])
print("Dtype", df['ship_ts'].dtype)
num_missing = df['ship_ts'].isna().sum()
print("NaT values:", num_missing)

```

    ['12/06/2025' '25/03/2025' '04-28-2025' '26/04/2025' '08/06/2025'
     '04-13-2025' '16/02/2025' '18/02/2025' '02-20-2025' '10/05/2025']
    Dtype object
    FIX APPLIED
    <DatetimeArray>
    ['2025-12-06 00:00:00', '2025-03-25 00:00:00', '2025-04-28 00:00:00',
     '2025-04-26 00:00:00', '2025-08-06 00:00:00', '2025-04-13 00:00:00',
     '2025-02-16 00:00:00', '2025-02-18 00:00:00', '2025-02-20 00:00:00',
     '2025-10-05 00:00:00']
    Length: 10, dtype: datetime64[ns]
    Dtype datetime64[ns]
    NaT values: 0



```python
# =======================================
# Step 7: LOGICAL INTEGRITY (TIME TRAVEL)
# =======================================

time_travel_mask = df['ship_ts'] < df['purchase_ts'] 
print(df.loc[time_travel_mask,['purchase_ts','ship_ts']].head(3)) #To show if they're rows with ship_ts date before purchase_ts date
num_time_travel = time_travel_mask.sum()
print("Total number:", num_time_travel)

df.loc[time_travel_mask, 'ship_ts'] = df.loc[time_travel_mask, 'purchase_ts'] + pd.Timedelta(days=30) #changed those dates to 30 days after the purchase_ts date

print("FIX APPLIED")
print(df.loc[time_travel_mask,['purchase_ts','ship_ts']].head(3))

```

       purchase_ts    ship_ts
    6   2025-10-04 2025-04-13
    14  2025-08-02 2025-02-14
    21  2025-09-04 2025-04-13
    Total number: 916
    FIX APPLIED
       purchase_ts    ship_ts
    6   2025-10-04 2025-11-03
    14  2025-08-02 2025-09-01
    21  2025-09-04 2025-10-04



```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 11 columns):
     #   Column                   Non-Null Count  Dtype         
    ---  ------                   --------------  -----         
     0   user_id                  5000 non-null   object        
     1   order_id                 5000 non-null   object        
     2   purchase_ts              5000 non-null   datetime64[ns]
     3   ship_ts                  5000 non-null   datetime64[ns]
     4   product_name             5000 non-null   object        
     5   product_id               5000 non-null   object        
     6   gbp_price                5000 non-null   float64       
     7   purchase_platform        5000 non-null   object        
     8   marketing_channel        4907 non-null   object        
     9   account_creation_method  4893 non-null   object        
     10  city                     4903 non-null   object        
    dtypes: datetime64[ns](2), float64(1), object(8)
    memory usage: 429.8+ KB



```python
df.to_csv('clean_data.csv', index=False)
# new cleaned file
print("CSV file saved successfully!")

```

    CSV file saved successfully!

