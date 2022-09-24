#!/usr/bin/env python

"""
Covid19 cli
"""
import os
import click
from databricks import sql


@click.group()
def cli():
    """
    Salary cli
    """


@cli.command()
@click.option(
    "--country",
    default="United States of America",
    help="Country you wana retrieve total cases",
)
def get_total_cases(country):
    print("Getting total cases for ", country)
    with sql.connect(
        server_hostname=os.environ["DATABRICKS_SERVER_HOSTNAME"],
        http_path=os.environ["DATABRICKS_HTTP_PATH"],
        access_token=os.environ["DATABRICKS_TOKEN"],
    ) as conn:

        with conn.cursor() as cursor:
            sql_statement = 'SELECT Total_Cases FROM default.covid19_csv where Country = \"' + str(country) + '\"'
            print(sql_statement)
            cursor.execute(sql_statement)
            result1 = cursor.fetchall()

            print(result1[0]['Total_Cases'], " cases")

if __name__ == "__main__":
    cli()