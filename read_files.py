def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then 
    return a list of js function names as strings.
    """

    func_list = []
    func_dic = {}
    counter = 0
    end = 0
    path = str(path_to_js_file)
    endpath = []

    with open(path, "r") as f:
        for line in f.readlines():
            counter += 1

            if '}' in line:
                indent = len(line) - len(line.lstrip())
                if indent == 0:
                    endpath.append(counter)
                elif indent == 4:
                    endpath.append(counter)

            if 'function' in line:
                func = line.split(" ")
                # print(func)
                if 'function' in func[0]:
                    name = func[1].split("(")
                    # print(name)
                    func_dic['name'] = name[0]

                elif 'function' in func[2]:
                    func_name = func[0]
                    func_dic['name'] = func_name
                
                func_dic['start_row'] = counter

                for line_end in endpath:
                    end += line_end

                func_dic['end_row'] = end
                func_list.append(func_dic)
                func_dic = {}
                
        print(func_list)

def get_end_row(num):
    counter = 0
    empty_list = []
    line_list = [num]
    for x in line_list:
        counter += 1
        empty_list.append(x)

if __name__ == "__main__":
    list_all_js_function_names("script.js")