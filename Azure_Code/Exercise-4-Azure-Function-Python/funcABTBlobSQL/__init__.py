import logging

import azure.functions as func
import json
import pandas as pd
import pymssql



def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    json_data = myblob.read()

    sample_json = json.loads(json_data.decode("utf-8"))
    #logging.info(f"This is Updated JSON Data :  {sample_json} ")

    if sample_json == None or sample_json == '':
        logging.info(f"empty or blank message received ")
    else:
        guid = sample_json['guid']
        filename = sample_json['filename']
        packetnumber = sample_json['packetnumber']
        
        hkdata = sample_json['hkdata']
        hkdata_df = pd.DataFrame(hkdata)
        hkdata_df['guid'] = guid

        logging.info(f"hk DataFrame size: {len(hkdata_df.index)}")

        locdata = sample_json['locdata']
        locdata_df = pd.DataFrame(locdata)
        locdata_df['guid'] = guid

        logging.info(f"Location DataFrame size: {len(locdata_df.index)}")

        
        packetdata = str(sample_json['data'])
        datalist = [[sample_json['guid']],[sample_json['filename']] ,[sample_json['packetnumber']] , [str(sample_json['data'])]]
        
        logging.info(f"Data List :  {datalist}")

        try:
            SQL_SERVER = "xxxxxxxxxxx.database.windows.net"
            logging.info("SQL Server Name :%s" , SQL_SERVER)
            DATABASE_NAME = "abtsample"
            logging.info("SQL DATABASE Name :%s" , DATABASE_NAME)

            USER_NAME = "xxxxxxxxx"
            PASSWORD = "xxxxxx@xxxxx"

            logging.info("Connecting to SQL Sever :%s" , SQL_SERVER)
            #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+SQL_SERVER+';DATABASE='+DATABASE_NAME+';UID='+USER_NAME+';PWD='+ PASSWORD)
            cnxn = pymssql.connect(server=SQL_SERVER, user=USER_NAME, password=PASSWORD, database=DATABASE_NAME)  
            cursor = cnxn.cursor()
            
            logging.info("Connected to SQL Sever :%s" , SQL_SERVER)

            logging.info("Insert HK Dataframe into SQL Server :%s" , SQL_SERVER)
            
            for index, row in hkdata_df.iterrows():
                cursor.execute("INSERT INTO dbo.hkdata (quantity,quantityUnit,startTime,endTime,quantityType,guid) values(%s,%s,%s,%s,%s,%s)", (row.quantity,row.quantityUnit,row.startTime,row.endTime,row.quantityType,row.guid))

            cnxn.commit()
            logging.info("HK Dataframe - All record Inserted")

            
            logging.info("Insert locdata Dataframe into SQL Server :%s" , SQL_SERVER)
            for index, row in locdata_df.iterrows():
                cursor.execute("INSERT INTO dbo.locdata (latitude,longitude,time,altitude,guid) values(%s,%s,%s,%s,%s)", (row.latitude,row.longitude,row.time,row.altitude,row.guid) )

            cnxn.commit()
            logging.info("LOCDATA Dataframe - All record Inserted")

            logging.info("Insert packetdata  into SQL Server :%s" , SQL_SERVER)

            cursor.execute("INSERT INTO dbo.packetdata (guid,filename,packetnumber,data) values(%s,%s,%s,%s)" ,(guid,filename,packetnumber,packetdata))
            cnxn.commit()

            cursor.close()
            logging.info("SQL Server Connection Closed")

        except Exception as e:
            logging.error(e)




