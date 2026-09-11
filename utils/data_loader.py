import pandas as pd
import streamlit as st

DATA_FILE = "EV_Charging_Demand_Final2.csv"

def load_data():
    """Load and cache EV charging demand dataset with standard column names."""
    try:
        df = pd.read_csv(DATA_FILE)
    except Exception:
        df = pd.read_csv("EV_Charging_Demand_Final.csv")

    column_mapping = {
        "state": "State",
        "EV_Registrations": "EV Registrations",
        "Charging_Stations": "Charging Stations"
    }
    df = df.rename(columns=column_mapping)

    if "State" in df.columns:
        df["State"] = df["State"].astype(str).str.title()

    if "EVs per Station" not in df.columns and "EVs_per_Station" in df.columns:
        df["EVs per Station"] = df["EVs_per_Station"]

    return df
