import json




def read_module_conf(file):
    with open(file, 'r') as f:
        return json.load(f)

def read_module_file(file):
    return None



if __name__ == "__main__":
    data = read_module_conf("../module.json")
    print(data)