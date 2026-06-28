from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy import text


class PostgresWriter:
    def __init__(self, conn_id: str):
        self.hook = PostgresHook(postgres_conn_id=conn_id)
        self.engine = self.hook.get_sqlalchemy_engine()

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
                    exchange_date::date
                FROM currency_rates_stg
                ON CONFLICT (currency_code, exchange_date)
                DO UPDATE SET
                    currency_name = EXCLUDED.currency_name,
                    rate = EXCLUDED.rate;
            """))