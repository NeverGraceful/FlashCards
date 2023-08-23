import sys, os, re, random

class_list = []
front_first = 1
cur_class = ""
shuffle = 0
front_list = []
back_list = []
hint_list = []

def fill_data_structures():
    print("fill ds")
    wanted_path = os.path.join(find_path(),'info.txt')
    with open(wanted_path) as info_file:
        for line in info_file:
            list = (re.split(':', line))
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

    info_file.write("\n")

    info_file.close()

def fill_flash_list():
        print("fill flash")
        wanted_path = os.path.join(find_path(), 'Classes\\' + cur_class +".txt")
        with open(wanted_path) as info_file:
            index = 0
            global front_list
            global back_list
            global hint_list
            for line in info_file:
                card_list = re.split(':', line)
                for i in card_list:
                    if index % 3 == 0:
                        front_list.append(i)
                    elif index % 3 == 1:
                        back_list.append(i)
                    else:
                        hint_list.append(i)
                    index = index + 1
                if shuffle == 1:
                    temp = list(zip(front_list, back_list, hint_list))
                    random.shuffle(temp)
                    res1, res2, res3 = zip(*temp)
                    front_list, back_list, hint_list = list(res1), list(res2), list(res3)   
            info_file.close()


def find_path():
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
           application_path = os.path.dirname(os.path.abspath(__file__))

        return application_path