#!/usr/bin/env python3

# Purpose: Generate Sample Data for Subject and Program 
# Author:  Vishva Jeet Singh (May 2021)
# Usage Example: python3 ./Exercise-1.py --env DEV \
#                                        --sample-number 200

import argparse
import logging
import random
import os
import numpy as np
import pandas as pd
from faker import Faker
from faker.providers.person.en import Provider 
from uuid import uuid4
from datetime import datetime
import csv
import time

logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)
fake = Faker('en_US')

def main():
    args = parse_args()

    
    try:
        env = args.env
        logging.info("Environment %s" , env)
        sample_number = args.sample_number
        logging.info("Sample Records Number %s" , sample_number)
        
        logging.info("Subject Demographic Generation - Started")
        subject_ids = subject_demographic_data(sample_number)
        logging.info("Subject Demographic Generation - Completed")

        logging.info("Subject Program Generation - Started")
        subject_program_data(subject_ids)
        logging.info("Subject Program Generation - Completed")
        
        logging.info("Subject Accelerometer Generation - Started")
        subject_accelerometer_data((subject_ids))
        logging.info("Subject Accelerometer Generation - Completed")

        logging.info("Subject Sample Data Generation - Completed")
    
    except:
        logging.error("Subject Sample Data Generation Failed")
        




def subject_demographic_data(sample_number):
    """ Generate subject  demographic details and save as .CSV file"""

    size = int(sample_number)
    df = pd.DataFrame(columns=['SubjectFirstName','SubjectLastName','SubjectGender','SubjectBirthdate','SubjectId','SubjectCity','SubjectZipcode','SubjectState'])
    df['SubjectFirstName'] = random_names('first_names', size)
    df['SubjectLastName'] = random_names('last_names', size) 
    df['SubjectGender'] = random_genders(size)
    df['SubjectBirthdate'] = random_dates(start=pd.to_datetime('1940-01-01'), end=pd.to_datetime('2008-01-01'), size=size)
    df['SubjectId']  = df.index.to_series().map(lambda x: uuid4())
    df['SubjectCity'] = df.index.to_series().map(lambda x: fake.city())
    df['SubjectZipcode'] = df.index.to_series().map(lambda x: fake.zipcode())
    df['SubjectState'] = df.index.to_series().map(lambda x: fake.state())
    df.to_csv('Subject_Demographic.csv', index=False)

    return df['SubjectId'].to_list()

def subject_program_data(ids):
    """ Generate subjects program details and save as .CSV file"""
    
    subjectids = ids
    SampleProgramNames = ['Amplatzer PFO Occluder', 'Quadra Allure MP CRT-P', 'Endurity Pacemaker','Engage TR Introducer']
    with open("Subject_Program.csv", 'at') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=['SubjectId','ProgramName','Amplitude','Frequency','Pulse'])
        writer.writeheader()
        for i in subjectids:
            for program in SampleProgramNames:
                writer.writerow({
                "SubjectId": i,
                "ProgramName":program,
                "Amplitude":random.randint(3, 8),
                "Frequency":str(random.randint(40, 60)) + 'MHz',
                "Pulse": random.randint(60, 100)
                })
                

def subject_accelerometer_data(ids):
    subjectids = ids
    SampleProgramNames = ['Amplatzer PFO Occluder', 'Quadra Allure MP CRT-P', 'Endurity Pacemaker']
    with open("Subject_Accelerometer.csv", 'at') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=['SubjectId','ProgramName','HFTime','Gyroscope'])
        writer.writeheader()
        
        for j in range(100): 
            time.sleep(3) 
            for i in subjectids:
                    for program in SampleProgramNames:
                        writer.writerow({
                        "SubjectId": i,
                        "ProgramName":program,
                        "HFTime":datetime.now().timestamp(),
                        "Gyroscope": random.randint(600, 1000)
                        })
            

def random_names(name_type, size):
    """ Generate subject names first_names or last_names """
    
    names = getattr(Provider, name_type)
    return np.random.choice(names, size=size)

def random_genders(size, p=None):
    """Generate genders """
    
    if not p:
        # default probabilities
        p = (0.49, 0.49, 0.01, 0.01)
    gender = ("M", "F", "O", "")
    return np.random.choice(gender, size=size, p=p)


def random_dates(start, end, size):
    """ Generate random dates within range between start and end.
    Unix timestamp is in nanoseconds by default, so divide it by
    24*60*60*10**9 to convert to days. """
    
    divide_by = 24 * 60 * 60 * 10**9
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, size), unit="D")

def parse_args():
    """Parse argument values from command-line"""

    parser = argparse.ArgumentParser(description='Arguments required for script.')
    parser.add_argument('-e', '--env', required=True, choices=['DEV', 'TEST', 'PREPROD', 'PROD'] , help='Name of Environment')
    parser.add_argument('-s', '--sample-number', required=True, help='Number Of Sample Records')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
