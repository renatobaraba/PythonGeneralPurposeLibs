# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:43:10 2019

@author: Renato
"""

import fileDialog as fd
import excelClass as ec
import postgreConnection as pgc
import time
from statistics import mean, median

if __name__ == '__main__':
    database = 'postgres'
    username = 'postgres'
    password = 'postgres'
    host = '127.0.0.1'
    port = '5432'
    sqlList = []
    executionTimes = []
    
    file = fd.fileDialog('Excel file', '.xlsx')
    file.openFile()
    fileName = file.path
    
    excelModule = ec.excelClass(fileName, 0)
    excelModule.excelCrawl()
    for rows in range(excelModule.sheet.nrows):
        value = excelModule.sheet.row_values(rows)
        sqlList.append(value[0])
        
    connection = pgc.postgresConnection(database,username,password, host, port)
    connection.connect()
    db_conn = connection.connection
    cur = db_conn.cursor()
    for query in sqlList:
        for i in range(5):
            startTime = time.time()
            cur.execute(query)
            endTime = time.time()
            totalTime = startTime - endTime
            executionTimes.append(totalTime)
        minTime = min(executionTimes)
        maxTime = max(executionTimes)
        averageTime = mean(executionTimes)
        medianTime = median(executionTimes)
        print(f'Query: {query}, minTime: {minTime}, maxTime: {maxTime}, averageTime: {averageTime}, medianTime: {medianTime}\n')
        executionTimes.clear()
    cur.close()
    db_conn.close()
        