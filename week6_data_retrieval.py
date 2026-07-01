"""
Week 6: Data Retrieval and Processing
MO-IT148 - Application Development and Emerging Technologies
Smart Tracking System - Blockchain Ledger
"""

from web3 import Web3
import pandas as pd
import numpy as np

# ── Step 1: Connect to Ganache ─────────────────────────────────────────────────
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Make sure Ganache is running.")
    exit()

# ── Step 2: Load Smart Contract ────────────────────────────────────────────────
CONTRACT_ADDRESS = "0xc013102fd1FF3484d53511B358B2De524EA39234"

CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "_deviceId",  "type": "string"},
            {"internalType": "string", "name": "_dataType",  "type": "string"},
            {"internalType": "string", "name": "_dataValue", "type": "string"}
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}],
        "name": "getRecord",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "string",  "name": "", "type": "string"},
            {"internalType": "string",  "name": "", "type": "string"},
            {"internalType": "string",  "name": "", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=CONTRACT_ABI
)
print(f"✅ Connected to Smart Contract at {CONTRACT_ADDRESS}")

# ── Step 3: Get Total Records ──────────────────────────────────────────────────
total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")

# ── Step 4: Fetch All Records into a DataFrame ─────────────────────────────────
print("\n📥 Retrieving records from blockchain...")
data = []
for i in range(total_records):
    record = contract.functions.getRecord(i).call()
    data.append({
        "timestamp": record[0],
        "device_id": record[1],
        "data_type": record[2],
        "data_value": record[3]
    })

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

print("✅ Data retrieved successfully from blockchain!")
print(f"\nShape: {df.shape}")
print("\nFirst 5 records:")
print(df.head())

# ── Step 5: Preprocess and Clean ──────────────────────────────────────────────
df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)

print("\nMissing values per column (before fillna):")
print(df.isnull().sum())

missing_threshold = 0.1
for col in df.columns:
    missing_pct = df[col].isnull().sum() / len(df)
    if missing_pct > 0:
        if missing_pct < missing_threshold:
            df[col].fillna(0, inplace=True)
            print(f"  → '{col}': minor missing values filled with 0")
        else:
            if df[col].dtype in ["float64", "int64"]:
                df[col].fillna(df[col].mean(), inplace=True)
                print(f"  → '{col}': filled with mean")
            else:
                df[col].fillna("Unknown", inplace=True)
                print(f"  → '{col}': filled with 'Unknown'")

print("\nMissing values per column (after fillna):")
print(df.isnull().sum())
print("\nCleaned DataFrame preview:")
print(df.head())

# ── Step 6: Summary Statistics ─────────────────────────────────────────────────
print("\nDescriptive Statistics:")
print(df.describe())
print(f"\nUnique data_type values (statuses): {df['data_type'].unique()}")

# ── Step 7: Save as CSV ────────────────────────────────────────────────────────
df.to_csv("cleaned_iot_data.csv", index=False)
print("\n✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")
print(f"   Total records saved: {len(df)}")
print(f"   Columns: {list(df.columns)}")

# ── Step 8: Verify ─────────────────────────────────────────────────────────────
df_verify = pd.read_csv("cleaned_iot_data.csv")
print("\n✅ Verification – cleaned_iot_data.csv loaded successfully")
print(f"   Rows: {len(df_verify)}, Columns: {len(df_verify.columns)}")
print("\nFirst 5 rows:")
print(df_verify.head())
