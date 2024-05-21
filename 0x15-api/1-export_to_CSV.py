#!/usr/bin/python3
"""import libraries"""
import csv
import json
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users/{}".format(
                sys.argv[1])).json()
    req_data = requests.get(url + "todos", params={
                "userId": sys.argv[1]}).json()

    employee_name = req_personal.get("username")

    lst = []
    for c in req_data:
        sub_lst = []
        sub_lst.append(str(c.get("userId")))
        sub_lst.append(employee_name)
        sub_lst.append(str(c.get("completed")))
        sub_lst.append(c.get("title"))
        # result = ' '.join(sub_lst)
        # words = result.split()
        # quoted_words = ['"' + word + '"' for word in words]
        # print(quoted_words)
        lst.append(sub_lst)

    file_name = "{}.csv".format(sys.argv[1])

    with open(file_name, 'w', newline='') as file:
        csvwriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(lst)


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
