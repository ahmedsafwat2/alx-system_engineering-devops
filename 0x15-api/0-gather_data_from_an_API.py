#!/usr/bin/python3
"""import libraries"""
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users/{}".format(
                sys.argv[1])).json()
    req_data = requests.get(url + "todos", params={
                "userId": sys.argv[1]}).json()

    employee_name = req_personal.get("name")
    total_tasks = len(req_data)
    done_tasks = list(filter(lambda x: x.get("completed") is True, req_data))
    title = [x['title'] for x in done_tasks]
    num_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done, total_tasks))
    for task in title:
        print("\t {}".format(task))


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
