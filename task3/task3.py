import json
import sys

def main():
    if len(sys.argv) != 4: 
        print("Использование: python task3.py <values.json> <tests.json> <report.json>")
        return

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    try:
        with open(values_path, 'r') as values_file:
            values_data = json.load(values_file)

        with open(tests_path, 'r') as tests_file:
            tests_data = json.load(tests_file)

    except (IOError, json.JSONDecodeError) as e:
        print("Ошибка при чтении файла JSON: " + str(e))
        return

    setter(values_data, tests_data, report_path)

def setter(values_data, tests_data, report_path):

    results = {}
    values_array = values_data.get("values", [])

    for value_obj in values_array:
        value = value_obj
        results[value["id"]] = value["value"]

    try:
        with open(report_path, 'w') as report_file:
            json.dump(tests_data, report_file)
    except IOError as e:
        print(str(e))

    with open(report_path, 'r') as report_file:
        report_data = json.load(report_file)

    report_data["tests"] = array_parser(report_data.get("tests", []), results)


    try:
        with open(report_path, 'w') as report_file:
            json.dump(report_data, report_file)
    except IOError as e:
        print(e)

def array_parser(values, results):
    helper = values

    for i in range(len(helper)):
        test = helper[i]

        if "values" in test:
            test["values"] = array_parser(test["values"], results)

        if "value" in test and "id" in test and test["id"] in results:
            test["value"] = results[test["id"]]

    return helper

if __name__ == "__main__":
    main()