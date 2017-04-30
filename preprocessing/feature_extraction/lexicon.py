class Lexicon(object):

    def __init__(self):
        self.__id2entry = {}
        self.__entry2id = {}
        self.__current_entry_id = 0

    def add_entry(self, entry):
        if entry in self.__entry2id.keys():
            e_id = self.__entry2id.get(entry)
        else:
            e_id = self.__add_new_entry(entry)
        return e_id

    def __add_new_entry(self, entry):
        e_id = self.__current_entry_id
        self.__current_entry_id += 1
        self.__id2entry[e_id] = entry
        self.__entry2id[entry] = e_id
        return e_id

    def get_entry(self, e_id):
        return self.__id2entry.get(e_id)

    def __len__(self):
        return len(self.__id2entry.keys())

    def store(self, file_path):
        with open(file_path, "w") as file:
            for e_id, entry in self.__id2entry.items():
                file.write(str(e_id) + '\t' + entry)

    def print(self):
        for e_id, entry in self.__id2entry.items():
            print(str(e_id) + '\t' + entry)
