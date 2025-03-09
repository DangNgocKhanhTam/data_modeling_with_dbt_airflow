#!/bin/bash
echo "Khởi động Airflow..."
pip install -r requirements.txt
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com || true
airflow webserver & airflow scheduler