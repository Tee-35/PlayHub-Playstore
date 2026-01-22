#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd 
import numpy as np 
df = pd.read_csv("unclean_data.csv")

print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")


# In[51]:


# =========================
# Step 1: HEADER CLEANING 
# =========================

print(df.columns.tolist())

df.columns = df.columns.str.strip().str.lower()

print("FIX APPLIED")
print(df.columns.tolist())


# In[52]:


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


# In[53]:


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


# In[54]:


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



# In[55]:


# ================================
# Step 4: PRICE COLUMN TYPE CHANGE  
# ================================

print("Dtype", df['gbp_price'].dtype)

df['gbp_price'] = df['gbp_price'].astype(float)

print("FIX APPLIED")

print("Dtype", df['gbp_price'].dtype)


# In[56]:


# ========================================
# Step 5: PURCHASE DATE COLUMN TYPE CHANGE  
# ========================================

print(df['purchase_ts'].unique()[:10])
print("Dtype", df['purchase_ts'].dtype)

df['purchase_ts'] = pd.to_datetime(df['purchase_ts'], format='%d/%m/%Y')

print("FIX APPLIED")

print(df['purchase_ts'].unique()[:10])
print("Dtype", df['purchase_ts'].dtype)



# In[57]:


# =======================================
# Step 6: SHIP DATE  FORMAT / TYPE CHANGE  
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


# In[58]:


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


# In[48]:


df.info()

