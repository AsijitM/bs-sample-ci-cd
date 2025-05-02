import ast

def extract_test_metadata(file_path):
    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)
    metadata = {}

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            test_name = node.name
            tags = []
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call) and hasattr(decorator.func, 'attr'):
                    tag_name = decorator.func.attr
                    if decorator.args:
                        arg = decorator.args[0]
                        if isinstance(arg, ast.Constant):  # Python 3.8+
                            tag_value = arg.value
                        elif isinstance(arg, ast.Str):  # Older compatibility
                            tag_value = arg.s
                        else:
                            tag_value = str(arg)
                    else:
                        tag_value = None
                    tags.append((tag_name, tag_value))
            if tags:
                metadata[test_name] = tags

    return metadata

# Run it
if __name__ == "__main__":
    file = "test_sample.py"
    test_metadata = extract_test_metadata(file)
    for test, tags in test_metadata.items():
        print(f"{test}: {tags}")
