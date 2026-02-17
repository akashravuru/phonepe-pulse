# PhonePe Pulse Dashboard

An interactive data visualization dashboard built with Python, Streamlit, and Plotly to explore PhonePe's transaction data across India.

## Live Demo
[Add Streamlit Cloud link here after deployment]

## Features
- Transaction analysis by type, state, and time period
- Interactive India geo map showing transaction intensity
- User growth analysis across states
- District-level transaction insights
- Growth trend analysis from 2018 to 2024

## Tech Stack
- Python
- Pandas
- Streamlit
- Plotly
- SQLite

## How to Run
1. Clone this repository
2. Clone PhonePe data: `git clone https://github.com/PhonePe/pulse.git phonepe_data`
3. Install dependencies: `pip install -r requirements.txt`
4. Run data extraction: `jupyter notebook phonepe_pulse.ipynb`
5. Run the app: `streamlit run app.py`

## Data Source
[PhonePe Pulse](https://github.com/PhonePe/pulse)