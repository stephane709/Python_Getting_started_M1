from contextlib import redirect_stderr


my_dict = {"chantal":25000, "Stephane":15000, "Giresse":20000, "Lionel":10000}

print(my_dict)
print(my_dict.get("chantal"))
print(my_dict["Stephane"])
print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())


nested_dict = { "chantal":
                {"colour": "red",
                "boulot": "nurse",
                "Salary": 90000},
                "Stephane":
                {"colour": "blue",
                "boulot": "IT",
                "Salary": 80000},
                "Giresse":
                {"colour": "Green",
                "boulot": "Civil Engineering",
                "Salary": 70000}
                }

print(nested_dict)

print(nested_dict["Giresse"])