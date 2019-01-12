# Define a dictionary that contains information about several members of your family. Use the following example as a template.

# my_family = {
#     'sister': {
#         'name': 'Krista',
#         'age': 42
#     },
#     'mother': {
#         'name': 'Cathie',
#         'age': 70
#     }
# }


my_family = {
  "mom": {
    "name": "Debbie",
    "age": 57
  },
  "dad": {
    "name": "Bill",
    "age": 57
  },
  "sister": {
    "name": "Justina",
    "age": 32
  }
}

bob = ["my " + k + " is "+ v['name']+ "and is " + str(v['age']) + "years old." for (k,v) in my_family.items()]

print((". ").join(bob))

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)