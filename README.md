# Currency Exchange ETL Pipeline

Personal Data Engineering project for collecting, validating, and storing currency exchange rates.

## Overview

This project extracts exchange rate data from public APIs, transforms and validates the data using Pandas, and stores historical exchange rates in PostgreSQL for further analysis.

The goal of the project is to practice Data Engineering concepts such as ETL pipelines, data validation, API integration, and workflow automation.

## Technologies

* Python
* Pandas
* PostgreSQL
* REST API
* Requests

## Features

* Currency exchange rate extraction from external APIs
* Historical data collection
* Data transformation and validation
* PostgreSQL storage
* Automated data quality checks

## Project Structure

```text
src/
├── request_api.py
├── file_reader.py
├── file_writer.py
├── config/
└── main.py
```

## Future Improvements

* Apache Airflow orchestration
* Docker containerization
* Parquet export
* Data Quality monitoring
* CI/CD pipeline

## Author

Illia Plotnykov
