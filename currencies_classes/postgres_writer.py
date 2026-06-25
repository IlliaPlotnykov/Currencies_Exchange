from sqlalchemy import create_engine, text


class PostgresWriter:
    def __init__(self, connection_string: str):
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

        df = df[["currency_code", "currency_name", "rate", "exchange_date"]]

        with self.engine.begin() as conn:
            df.to_sql(
                name="currency_rates_tmp",
                con=conn,
                if_exists="replace",
                index=False,
                method="multi"
            )

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
                FROM currency_rates_tmp
                ON CONFLICT (currency_code, exchange_date)
                DO UPDATE SET
                    currency_name = EXCLUDED.currency_name,
                    rate = EXCLUDED.rate;
            """))

            conn.execute(text("DROP TABLE IF EXISTS currency_rates_tmp;"))