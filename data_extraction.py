import os
import json
import pandas as pd

def extract_aggregated_transaction_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    transactions = data["data"]["transactionData"]
                    for transaction in transactions:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "transaction_type": transaction["name"],
                            "transaction_count": transaction["paymentInstruments"][0]["count"],
                            "transaction_amount": transaction["paymentInstruments"][0]["amount"]
                        })
    return pd.DataFrame(records)

def extract_aggregated_user_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    records.append({
                        "state": state,
                        "year": int(year),
                        "quarter": quarter,
                        "registered_users": data["data"]["aggregated"]["registeredUsers"],
                        "app_opens": data["data"]["aggregated"]["appOpens"]
                    })
    return pd.DataFrame(records)

def extract_map_transaction_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    districts = data["data"]["hoverDataList"]
                    for district in districts:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "district": district["name"],
                            "transaction_count": district["metric"][0]["count"],
                            "transaction_amount": district["metric"][0]["amount"]
                        })
    return pd.DataFrame(records)

def extract_map_user_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    for district_name, district_data in data["data"]["hoverData"].items():
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "district": district_name,
                            "registered_users": district_data["registeredUsers"],
                            "app_opens": district_data["appOpens"]
                        })
    return pd.DataFrame(records)

def extract_top_transaction_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    for district in data["data"]["districts"]:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "entity_name": district["entityName"],
                            "entity_type": "district",
                            "transaction_count": district["metric"]["count"],
                            "transaction_amount": district["metric"]["amount"]
                        })
                    for pincode in data["data"]["pincodes"]:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "entity_name": pincode["entityName"],
                            "entity_type": "pincode",
                            "transaction_count": pincode["metric"]["count"],
                            "transaction_amount": pincode["metric"]["amount"]
                        })
    return pd.DataFrame(records)

def extract_top_user_data(data_path):
    records = []
    for state in os.listdir(data_path):
        state_path = os.path.join(data_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)
                    quarter = int(file.replace(".json", ""))
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    for district in data["data"]["districts"]:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "entity_name": district["name"],
                            "entity_type": "district",
                            "registered_users": district["registeredUsers"]
                        })
                    for pincode in data["data"]["pincodes"]:
                        records.append({
                            "state": state,
                            "year": int(year),
                            "quarter": quarter,
                            "entity_name": pincode["name"],
                            "entity_type": "pincode",
                            "registered_users": pincode["registeredUsers"]
                        })
    return pd.DataFrame(records)

def setup_database(conn):
    print("Cloning PhonePe data...")
    os.system("git clone https://github.com/PhonePe/pulse.git phonepe_data")
    
    print("Extracting aggregated transaction data...")
    df = extract_aggregated_transaction_data("phonepe_data/data/aggregated/transaction/country/india/state")
    df.to_sql("aggregated_transaction", conn, if_exists="replace", index=False)
    
    print("Extracting aggregated user data...")
    df = extract_aggregated_user_data("phonepe_data/data/aggregated/user/country/india/state")
    df.to_sql("aggregated_user", conn, if_exists="replace", index=False)
    
    print("Extracting map transaction data...")
    df = extract_map_transaction_data("phonepe_data/data/map/transaction/hover/country/india/state")
    df.to_sql("map_transaction", conn, if_exists="replace", index=False)
    
    print("Extracting map user data...")
    df = extract_map_user_data("phonepe_data/data/map/user/hover/country/india/state")
    df.to_sql("map_user", conn, if_exists="replace", index=False)
    
    print("Extracting top transaction data...")
    df = extract_top_transaction_data("phonepe_data/data/top/transaction/country/india/state")
    df.to_sql("top_transaction", conn, if_exists="replace", index=False)
    
    print("Extracting top user data...")
    df = extract_top_user_data("phonepe_data/data/top/user/country/india/state")
    df.to_sql("top_user", conn, if_exists="replace", index=False)
    
    print("Database setup complete!")