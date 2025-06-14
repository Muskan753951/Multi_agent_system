# 🚀 Multi-Agent System for Goal-Based Information Retrieval

This project demonstrates a modular **multi-agent system** built in Python. It takes a user's high-level goal (e.g., "Check if the next SpaceX launch may be delayed due to weather") and uses **chained intelligent agents** to fulfill the task step-by-step using public APIs.

---

## 🧠 Agents Involved

### 🧭 Planner Agent
Breaks the goal into sequential steps.

### 🚀 Launch Agent
Finds the next SpaceX launch using SpaceX API.

### 🌦️ Weather Agent
Fetches weather at the launchpad using OpenWeatherMap API.

### 🧾 Summary Agent
Analyzes the weather and returns a delay risk summary.

---

## 🗂️ Folder Structure

Multi_agent system/
│
├── main.py
├── coordinator.py
├── .env
├── requirements.txt
│
├── agents/
│ ├── init.py
│ ├── planner_agent.py
│ ├── launch_agent.py
│ ├── weather_agent.py
│ └── summary_agent.py
│
├── evals/
│   └── test_case_1.json
