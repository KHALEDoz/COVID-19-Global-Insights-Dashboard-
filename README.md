# COVID19 Global Insights Dashboard

## Overview
[cite_start]This project is an **interactive real-time dashboard** developed to visualize and analyze COVID-19 pandemic trends across **230+ countries**[cite: 26, 27]. [cite_start]The system extracts and processes real-time global health data from reliable sources, managing datasets with over **200,000+ records** to ensure accurate daily reporting[cite: 27].

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

* [cite_start]**Language:** Python[cite: 12].
* [cite_start]**Library:** Streamlit for Web Interface & Interactivity[cite: 29].
* [cite_start]**Data Management:** High-volume data processing and integrity (Handling 200,000+ records)[cite: 27].
* **DevOps:** **Docker & Containers** for consistent environments and easy deployment.

## Key Learnings
* **Full-Stack Thinking:** Learned how to bridge the gap between data analysis (Python/Pandas) and deployment (Docker).
* **Data Integrity:** Gained experience in handling inconsistent global data sources and cleaning them for accurate visualization.
* **UI/UX for Data:** Mastered the art of presenting complex statistics in a simple, user-friendly interactive dashboard.

## Key Technical Challenges & Solutions
* **Optimizing Large-Scale Data Loading:** Implemented Streamlit’s `@st.cache_data` to optimize data loading and ensure a responsive UI despite the large dataset.
* **Real-time Data Integrity:** Developed a pipeline to extract and process data from reliable sources to ensure accurate daily reporting.
* **User-Centric Interactivity:** Created a dynamic UI that updates charts and KPIs based on user selection, including specific country-level analysis like Saudi Arabia.

## Project Visuals

### 1. Global Data Aggregation & Analytics
* **Massive Data Summarization:** Efficiently processes and aggregates live records for **232 countries**, displaying real-time global KPIs (Total Cases & Deaths).
* **Comparative Insights:** Implements a dynamic ranking system to visualize the **Top 10 impacted regions** using a gradient-coded bar chart for quick severity assessment.

<img width="1441" height="796" alt="global_dashboard" src="https://github.com/user-attachments/assets/81be6555-9a0b-4f6c-9c62-1611d939475d" />

### 2. Time-Series Trend Analysis
* **Historical Data Visualization:** Processes daily case fluctuations from **2020 to 2023**, identifying major pandemic waves and seasonal peaks through advanced data aggregation.
* **Granular Tracking:** Features a high-precision line chart that maintains performance and clarity while rendering thousands of daily data points across the multi-year timeline.
<img width="1349" height="544" alt="Screenshot 2026-04-23 at 10 04 03 AM" src="https://github.com/user-attachments/assets/615fd9f5-0e22-4f8a-9369-059984ead4e6" />


### 3. Interactive Country-Level Exploration
* **Dynamic Search & Filtering:** Features a robust dropdown interface that allows users to seamlessly navigate through **232 global entities**, providing instant access to localized data.
* **Cross-Regional Comparison:** Demonstrates the dashboard's ability to render distinct epidemiological profiles—comparing unique wave patterns (e.g., **Saudi Arabia** vs. **United States**) using high-performance rendering logic.
* **Real-Time Data Re-rendering:** The backend reactively updates all visualizations based on user selection, ensuring a zero-lag experience while switching between complex multi-year datasets.

<img width="1340" height="596" alt="Country Selection" src="https://github.com/user-attachments/assets/f752a8c5-df84-4bd6-b405-6630c3afda16" />
<img width="1349" height="583" alt="Saudi Arabia Analysis" src="https://github.com/user-attachments/assets/6fa44eec-6f9b-40ea-9297-49e088536223" />
<img width="1347" height="590" alt="USA Analysis" src="https://github.com/user-attachments/assets/21713462-ca32-4078-926c-aed8086a3031" />


