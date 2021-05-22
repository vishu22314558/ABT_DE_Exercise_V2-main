#!/usr/bin/env python3

# Purpose: Read Sample CSV data and ingest into Azure SQL Sever  
# Author:  Vishva Jeet Singh (May 2021)
# Usage Example: python3 ./Exercise-2-File1 --File Subject_Program.CSV 
#                                       


import argparse
import logging
import random
import os
from datetime import datetime
import csv
import pyodbc
import pandas as pd


logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)

def main():
    args = parse_args()

    
    try:
        file = args.File
        logging.info("File Name %s" , file)

        df_file = pd.read_csv(file, index_col=0)
        
        SQL_SERVER = os.environ.get("SQLSERVER")
        logging.info("SQL Server Name :%s" , SQL_SERVER)
        DATABASE_NAME = os.environ.get("DATABASE")
        logging.info("SQL DATABASE Name :%s" , DATABASE_NAME)

        USER_NAME = os.environ.get("SQLUSERNAME")
        PASSWORD = os.environ.get("PASSWORD")

        logging.info("Connecting to SQL Sever :%s" , SQL_SERVER)
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+SQL_SERVER+';DATABASE='+DATABASE_NAME+';UID='+USER_NAME+';PWD='+ PASSWORD)
        cursor = cnxn.cursor()
        logging.info("Connected to SQL Sever :%s" , SQL_SERVER)

        logging.info("Insert Dataframe into SQL Server" , SQL_SERVER)
        for index, row in df_file.iterrows():
            cursor.execute("INSERT INTO dbo.SubjectDemographic (SubjectFirstName,SubjectLastName,SubjectGender,SubjectBirthdate,SubjectId,SubjectCity,SubjectZipcode,SubjectState) values(?,?,?,?,?,?,?,?)", row.SubjectFirstName, row.SubjectLastName, row.SubjectGender, row.SubjectBirthdate, row.SubjectId, row.SubjectCity, row.SubjectZipcode , row.SubjectState)

        logging.info("All record Inserted")
        coxn.commit()
        cursor.close()

        logging.info("SQL Server Connection Closed")

    except Exception as e:
        logging.error(e)


def parse_args():
    """Parse argument values from command-line"""

    parser = argparse.ArgumentParser(description='Arguments required for script.')
    parser.add_argument('-f', '--File', required=True, help='Name of CSV Data Set')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
