# IoT Data Simulation — Blockchain Ledger

A smart tracking system that stores and retrieves IoT sensor data on a local blockchain using Web3.py and Ganache.

## Project Overview
This project simulates IoT data from a logistics tracking system and records each data entry as a transaction on the Ethereum blockchain using a deployed Solidity smart contract.

## Files
| File | Description |
|---|---|
| `iot_data.csv` | IoT sensor dataset (100 records) |
| `iot_data.json` | IoT sensor data in JSON format |
| `week4_week5_blockchain_ledger.ipynb` | Jupyter Notebook for Week 4 & Week 5 milestones |
| `IoTDataStorage.sol` | Solidity smart contract |

## Technologies Used
- Python 3
- Web3.py
- Ganache (local Ethereum blockchain)
- Remix IDE
- Jupyter Notebook
- Pandas

## Smart Contract
- **Contract Address:** 0x090f65a5128C183294816008589A6231A5b43A8d
- **Network:** Ganache (local)
- **Functions:** `storeData()`, `getRecord()`, `getRecordCount()`

## Setup Instructions
1. Install dependencies: `pip install web3 pandas`
2. Open Ganache and start Quickstart
3. Deploy `IoTDataStorage.sol` in Remix IDE using `http://127.0.0.1:7545`
4. Run `week4_week5_blockchain_ledger.ipynb` in Jupyter Notebook
