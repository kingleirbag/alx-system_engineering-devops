#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the CSV format.
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    usrId = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(usrId)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(usrId)

    employee = sessionReq.get(usrId)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = usrId + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([usrId, usr, i.get('completed'), i.get('title')])
