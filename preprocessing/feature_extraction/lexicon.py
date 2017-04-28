class Lexicon(object):

    def __init__(self):
        self.__id2entry = {}
        self.__label2entry = {}
        self.__current_entry_id = 0

    def add_entry(self, label):
        if label in self.__label2entry.keys():
            e_id = self.__add_to_existing_entry(label)
        else:
            e_id = self.__add_new_entry(label)
        return e_id

    def __add_to_existing_entry(self, label):
        entry = self.__label2entry.get(label)
        entry.increase_frequency()
        return entry.get_id()

    def __add_new_entry(self, label):
        e_id = self.__current_entry_id
        self.__current_entry_id += 1
        entry = LexiconEntry(e_id, label)
        self.__id2entry[e_id] = entry
        self.__label2entry[label] = entry
        return e_id

    def store(self, file_path):
        with open(file_path, "w") as file:
            for e_id in self.__id2entry.keys():
                entry = self.__id2entry.get(e_id)
                file.write(entry)

    def print(self, frequency=0):
        for e_id in self.__id2entry.keys():
            entry = self.__id2entry.get(e_id)
            if entry.get_frequency() > frequency:
                print(entry)

    def create_histogram(self):
        histo = {}
        for e_id in self.__id2entry.keys():
            entry = self.__id2entry.get(e_id)
            frequency = entry.get_frequency()
            if frequency in histo.keys():
                count = histo.get(frequency)
                histo[frequency] = count + 1
            else:
                histo[frequency] = 1
        return histo


class LexiconEntry(object):

    def __init__(self, e_id, label):
        self.__e_id = e_id
        self.__label = label
        self.__frequency = 1

    def increase_frequency(self):
        self.__frequency += 1

    def get_id(self):
        return self.__e_id

    def get_frequency(self):
        return self.__frequency

    def __str__(self):
        return str(self.__e_id) + '\t' + self.__label + '\t' + str(self.__frequency)