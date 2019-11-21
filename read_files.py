def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """

    func_list = []
    func_dic = {}
    counter = 0
    end = 0
    path = str(path_to_js_file)

    with open(path, "r") as f:
        # print(f.read())
        for line in f.readlines():
            counter += 1
            # print(line)

            if '}' in line:
                indent = len(line) - len(line.lstrip())
                if indent == 0:
                    print(counter)
                    end = counter

            if 'function' in line:
                func = line.split(" ")
                if 'function' in func[0]:
                    name = func[1].split("(")
                    func_dic['name'] = name[0]

                elif 'function' in func[2]:
                    func_name = func[0]
                    func_dic['name'] = func_name
                    # print(func_name)
                
                func_dic['start_row'] = counter
                func_dic['end_row'] = end
                func_list.append(func_dic)
                func_dic = {}
                
        print(func_list)

if __name__ == "__main__":
    list_all_js_function_names("script.js")