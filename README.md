# IoT Data Simulation — Blockchain Ledger

A smart tracking system that stores and retrieves IoT sensor data on a local blockchain using Web3.py and Ganache.

## Project Overview
This project simulates IoT data from a logistics tracking system and records each data entry as a transaction on the Ethereum blockchain using a deployed Solidity smart contract.

## Files
| File | Description |
|---|---|
| `iot_data.csv` | IoT sensor dataset (100 records) |
| `iot_data.json` | IoT sensor data in JSON format |
| `iot_logistics_charts.png` | IoT logistics data visualizations |
| `week4_week5_blockchain_ledger.ipynb` | Jupyter Notebook for Week 4 & Week 5 milestones |
| `IoTDataStorage.sol` | Solidity smart contract |
| `week6_data_retrieval.py` | Week 6 – Data retrieval and processing script |
| `cleaned_iot_data.csv` | Cleaned IoT data retrieved from blockchain (Week 6) |
| `week7_line_plot.py` | Week 7 – Line plot visualization of IoT sensor readings |
| `week7_original_lineplot.png` | Line plot of original IoT temperature readings over time |
| `week7_comparison_lineplot.png` | Comparison plot showing original vs anomaly-injected data |

## Technologies Used
- Python 3
- Web3.py
- Ganache (local Ethereum blockchain)
- Remix IDE
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Smart Contract
- **Contract Address:** 0xc013102fd1FF3484d53511B358B2De524EA39234
- **Network:** Ganache (local)
- **Functions:** `storeData()`, `getRecord()`, `getTotalRecords()`

## Setup Instructions
1. Install dependencies: `pip install web3 pandas numpy`
2. Open Ganache and start Quickstart
3. Deploy `IoTDataStorage.sol` in Remix IDE using `http://127.0.0.1:7545`
   - Set EVM version to `paris` in Advanced Configurations before compiling
4. Run `week4_week5_blockchain_ledger.ipynb` for Weeks 4 & 5
5. Run `week6_data_retrieval.py` for Week 6 data retrieval and processing
6. Run `week7_line_plot.py` for Week 7 line plot visualization

## Week 6 – Data Retrieval and Processing
- Retrieved all 100 IoT records stored on the blockchain
- Structured data into a Pandas DataFrame
- Converted Unix timestamps to readable datetime format
- Extracted numeric sensor values and handled missing data
- Saved cleaned dataset as `cleaned_iot_data.csv`

## Week 7 – IoT Sensor Data Visualization
- Created a multi-line plot of temperature readings over time, color-coded by package status
- Performed trend analysis using a 10-record rolling average
- Injected a sudden temperature anomaly (75°C spike at record 50) to simulate a sensor failure
- Generated a side-by-side comparison of original vs. anomaly-injected data
- Saved both visualizations as PNG files
