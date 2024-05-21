#!/usr/bin/python3
"""import libraries"""
import json
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users").json()

    dct = {}
    for i in req_personal:
        id = i.get("id")
        username = i.get("username")
        req_data = requests.get(url + "todos", params={
                "userId": str(id)}).json()

        sub_lst = []
        for c in req_data:
            sub_dct = {}
            sub_dct["username"] = username
            sub_dct["task"] = c.get("title")
            sub_dct["completed"] = c.get("completed")
            sub_lst.append(sub_dct)

        dct[str(id)] = sub_lst

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(dct, json_file, indent=4)


if __name__ == "__main__":
    main()
