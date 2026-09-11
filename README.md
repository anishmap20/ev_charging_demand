# ⚡ EV Charging Demand Analysis & Prediction Dashboard

An interactive data analytics dashboard for analyzing and understanding **Electric Vehicle (EV) charging demand across Indian states**.

The project transforms EV charging data into meaningful visualizations, rankings, trends, and insights to support **data-driven EV charging infrastructure planning**.

---

## 📌 Project Overview

The rapid adoption of Electric Vehicles is increasing the demand for reliable and strategically located charging infrastructure.

This project provides an interactive dashboard to explore EV charging demand across different Indian states. Users can analyze state-wise demand, compare regions, identify high-demand areas, explore the underlying dataset, and generate actionable insights.

The dashboard is designed to make complex EV charging data easier to understand through interactive charts, KPIs, rankings, and visual analysis.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze EV charging demand across Indian states.
- Identify states with high and low charging demand.
- Compare charging demand between states.
- Visualize demand patterns and trends.
- Provide data-driven insights for charging infrastructure planning.
- Allow users to explore the underlying EV charging dataset interactively.
- Support better decision-making for future EV charging expansion.

---

## ✨ Key Features

### 📊 Interactive Dashboard

Provides an overview of EV charging demand using interactive KPIs, charts, and visualizations.

### 🏛️ State-wise Analysis

Analyze charging demand for individual Indian states and compare their performance.

### 🏆 Demand Ranking

Rank states based on EV charging demand and identify regions requiring greater charging infrastructure.

### 💡 Insights

Generate meaningful insights from the dataset to understand important demand patterns and trends.

### 🔍 Data Explorer

Explore and filter the underlying EV charging dataset interactively.

### 📈 Data Visualization

Interactive visualizations make it easier to identify:

- Demand patterns
- State-level differences
- High-demand regions
- Charging infrastructure requirements
- Trends and comparisons

### 🇮🇳 India-focused Analysis

The project focuses on EV charging demand across Indian states and includes geographical data for visualization.

---

## 🖥️ Dashboard Pages

The application contains multiple pages:

| Page | Description |
|------|-------------|
| 🏠 Overview | High-level summary of EV charging demand |
| 🏛️ State Analysis | Detailed state-wise demand analysis |
| 🏆 Demand Ranking | Ranking of states based on demand |
| 💡 Insights | Important observations and data-driven insights |
| 🔍 Data Explorer | Interactive exploration of the dataset |

---

## 🛠️ Tech Stack

### Programming Language

- **Python**

### Framework

- **Streamlit**

### Data Analysis

- **Pandas**
- **NumPy**

### Data Visualization

- **Plotly**

### Data & Geographic Visualization

- CSV datasets
- GeoJSON
- Interactive maps

### Development Tools

- Jupyter Notebook
- Git
- GitHub

---

## 📂 Project Structure

```text
EV_charging_demand/
│
├── app.py
│
├── pages/
│   ├── __init__.py
│   ├── overview.py
│   ├── state_analysis.py
│   ├── demand_ranking.py
│   ├── insights.py
│   └── data_explorer.py
│
├── components/
│   ├── __init__.py
│   ├── bottom_trends.py
│   ├── footer_bar.py
│   ├── header_banner.py
│   ├── kpi_cards.py
│   └── middle_charts.py
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── sidebar.py
│   └── style.py
│
├── notebooks/
│   ├── EV_Charging_Analysis.ipynb
│   └── india_states.geojson
│
├── assets/
│   ├── ev_hero_charging_station.png
│   └── ev_smart_city_india.png
│
├── EV_Charging_Demand_Final.csv
├── EV_Charging_Demand_Final2.csv
├── EV_Charging_Demand_Final2R.csv
│
├── requirements.txt
├── README.md
└── .gitignore
