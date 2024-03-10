input_dict = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}
def generate_output(input_dict, current_path=None):
    if current_path is None:
        current_path = []

    output = {}
    for key, value in input_dict.items():
        current_path.append(key)
        if isinstance(value, dict):
            sub_output = generate_output(value, current_path)
            output[key] = list(sub_output.keys())
            output.update(sub_output)
        else:
            output[key] = value
        current_path.pop()

    return output
print(generate_output(input_dict=input_dict))
