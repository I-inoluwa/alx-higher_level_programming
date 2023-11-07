#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

python_file="$1"

# Check if the Python file exists
if [ ! -f "$python_file" ]; then
    echo "Python file '$python_file' does not exist."
    exit 1
fi

# Check for module documentation
module_doc=$(python3 -c "print(__import__('$(basename -s .py "$python_file")').__doc__")"
if [ -z "$module_doc" ]; then
    echo "Module documentation missing for $python_file"
fi

# Check for class and function documentation
class_and_function_names=$(python3 -c "import $python_file; 
class_names = [name for name, obj in vars($python_file).items() if isinstance(obj, type)]; 
function_names = [name for name, obj in vars($python_file).items() if callable(obj) and name not in class_names]; 
print(','.join(class_names + function_names))")

IFS=',' read -ra items <<< "$class_and_function_names"
for item in "${items[@]}"; do
    item_doc=$(python3 -c "import $python_file; print(getattr($python_file, '$item').__doc__)")
    if [ -z "$item_doc" ]; then
        echo "Documentation missing for $item in $python_file"
    fi
done
