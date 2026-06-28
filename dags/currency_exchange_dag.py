from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus


class PostgresWriter:
    def __init__(self, conn_id: str):
        airflow_conn = BaseHook.get_connection(conn_id)

        host = airflow_conn.host
        port = airflow_conn.port
        database = airflow_conn.schema
        user = airflow_conn.login
        password = quote_plus(airflow_conn.password)

        connection_string = (
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        )

        self.engine = create_engine(connection_string)

    def write_to_postgres(self, df):
        if df.empty:
            print("No data to insert")
            return

        df = df.rename(columns={
            "cc": "currency_code",
            "txt": "currency_name",
            "rate": "rate",
            "exchangedate": "exchange_date"
        })

        df = df[[
            "currency_code",
            "currency_name",
            "rate",
            "exchange_date"
        ]]

        df.to_sql(
            name="currency_rates_stg",
            con=self.engine,
            if_exists="replace",
            index=False,
            method="multi"
        )

        with self.engine.begin() as conn:
            conn.execute(text("""
                INSERT INTO currency_rates (
                    currency_code,
                    currency_name,
                    rate,
                    exchange_date
                )
                SELECT
                    currency_code,
                    currency_name,
                    rate,
                    exchange_date
                )
                FROM currency_rates_stg
                ON CONFLICT (currency_code, exchange_date)
                DO UPDATE SET
                    currency_name = EXCLUDED.currency_name,
                    rate = EXCLUDED.rate;
            """))