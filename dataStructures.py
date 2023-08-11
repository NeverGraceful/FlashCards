import sys, os, re

class_list = []
front_first = 1
cur_class = ""
shuffle = 0

def fill_data_structures():
    print("fill ds")
    wanted_path = os.path.join(find_path(),'info.txt')
    with open(wanted_path) as info_file:
        for line in info_file:
            list = line.split() #(re.split(':|\n\s', line))
            print(list)
            match list[0]:
                case "classes:":
                    list.remove("classes:")
                    global class_list
                    class_list = list.copy()
                    
        info_file.close()

def save_data():
    print("save ds")
    wanted_path = os.path.join(find_path(),'info.txt')
    info_file = open(wanted_path, 'w')
    info_file.write("classes")
    for classes in class_list:
        print(classes)
        info_file.write(":" + classes)

    # info_file.write("\n")

    info_file.close()


def find_path():
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path