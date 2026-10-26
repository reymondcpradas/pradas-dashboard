# Agusan del Sur Palay Dashboard

Design adapted from your uploaded `app(8).py`: dark navy theme, teal hero banner, KPI cards, sidebar navigation, and interactive Plotly charts.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Annual and semester values are embedded from the final Chapters 4–5 manuscript. The 2025 official annual farmgate value is ₱14.9325/kg, with semester values ₱14.56 and ₱15.28. The annual value is not calculated as the semester mean.

Forecasting uses independent year-based linear regression; metrics are in-sample, not independent validation.
