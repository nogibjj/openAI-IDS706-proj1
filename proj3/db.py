#!/usr/bin/env python
import pandas as pd
import MySQLdb
import os
import click

@click.group()
def cli():
    """
    University CLI
    """

#mysql -h database-lqc.ciankffgrtkz.us-east-1.rds.amazonaws.com -P 3306 -u admin -p

def get_connection():
    """Returns a connection to the database"""
    print(os.environ["DBPASS"])
    connection = MySQLdb.connect(
        host="db706.ciankffgrtkz.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd=os.environ["DBPASS"],
        db="proj4",
    )
    return connection


def save_data(
    connection,
    University_name,
    Region,
    Founded_year,
    Motto,
    World_rank,
    Website,
):
    

    cursor = connection.cursor()
    str = (
        "INSERT INTO universities VALUES ('"
        + University_name
        + "', '"
        + Region
        + "',"
        + Founded_year
        + ",'"
        + Motto
        + "',"
        + World_rank
        + ",'"
        + Website
        + "');"
    )
    print(str)
    cursor.execute(str)
    connection.commit()



    # University_name,
    # Region,
    # Founded_year,
    # Motto,
    # World_rank,
    # Website,
@cli.command()
@click.option("--region", default='North East England', help="region of the uni")
def get_uni(region):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM universities where region = '" + region + "';"
    cursor.execute(sql)
    data = cursor.fetchall()
    for (
        University_name,
        Region,
        Founded_year,
        Motto,
        World_rank,
        Website,
    ) in data:
        print("University_name: " + University_name)
        print("Region: " + Region)
        print("Founded_year: " + str(Founded_year))
        print("Motto: " + Motto)
        print("World_rank: " + str(World_rank))
        print("Website: " + Website)
        print("----------------------")
    connection.close()

    # University_name,
    # Region,
    # Founded_year,
    # Motto,
    # World_rank,
    # Website,
def save_all_data():
    """Saves the csv data to the database"""
    df = pd.read_csv("./uk_universities.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        save_data(
            connection,
            str(row["University_name"]),
            str(row["Region"]),
            str(row["Founded_year"]),
            str(row["Motto"]),
            str(row["World_rank"]),
            str(row["Website"]),
        )
        print("saved")

if __name__ == "__main__":
    #cli()
    save_all_data()


# create table universities
# 