class MyClass:
    def func1(self):
        print("func1 called")

    def func2(self):
        print("func2 called")

    def func3(self):
        print("func3 called")

# Create a dictionary to hold function references by name
function_map = {
    "func1": MyClass.func1,
    "func2": MyClass.func2,
    "func3": MyClass.func3,
}

# Instantiate the class
my_object = MyClass()

# Dynamically call a function based on its name (e.g., 'func2')
function_to_call = "func2"

# Check if the function exists in the dictionary
if function_to_call in function_map:
    # Get the function object from the dictionary
    function_to_execute = function_map[function_to_call]

    # Call the function using the object and the function object
    function_to_execute(my_object)
else:
    print(f"Function '{function_to_call}' not found")