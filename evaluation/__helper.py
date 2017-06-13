from collections import defaultdict
from re import sub as regex_replace


def load_mapping_id2chapter():
    lexicon = {}
    with open('grimm_lexicon_documents.csv', 'r') as f:
        for line in f:
            data = line.split('\t')
            id = int(data[0])
            chapter_information = data[1]
            chapter = chapter_information[6 : chapter_information.index('.')]
            lexicon[id] = int(chapter)
    return lexicon


def map_to_broader_classes(mapping, class_ids):
    result = []
    for class_id in class_ids:
        if class_id == 'Unclassified':
            result.append('unclassified')
            continue
        class_id = int(regex_replace("\D", "", class_id).strip())
        for broader_class, borders in mapping.items():
            if borders[0] <= class_id <= borders[1]:
                result.append(broader_class)
    return result


def load_grimm_classification_clusters():
    mapping = {'animal_tales': (1, 299), 'tales_of_magic': (200, 749), 'religious_tales': (750, 849),
                     'realistic_tales': (850, 999), 'tales_of_stupid_orgre': (1000, 1199),
                     'anecdotes_and_jokes': (1200, 1999), 'formula_tales': (2000, 2399)}
    clusters = defaultdict(set)
    with open('grimm_classification.tsv', 'r') as f:
        for line in f:
            data = line.split('\t')
            chapter = int(data[0])
            class_ids = data[1].split(',')
            if not class_ids == 'Unclassified':
                class_ids = [class_id.strip() for class_id in class_ids]
                class_ids = list(filter(lambda id: len(id) > 0, class_ids))
            else:
                class_ids = []
            broader_classes = map_to_broader_classes(mapping, class_ids)
            for broader_class in broader_classes:
                clusters[broader_class].add(chapter)
    return clusters


def read_matlab_clusters():
    clusters = {}
    current_condition = ''
    with open('matlab_clustering_result.txt', 'r') as f:
        for line in f:
            if line.startswith('euclidean') or line.startswith('cosine'):
                current_condition = line.replace('\n', '')
            if line.startswith('assignment_to_clusters'):
                further_condition =  line[25 : line.index('=')]
                cluster_ids_as_string = line[line.index('=') + 1 : ].replace('\n', '').replace('[', '').replace(']', '')
                cluster_ids = cluster_ids_as_string.split(';')
                clusters[current_condition+further_condition] = cluster_ids
    return clusters


def map_matlabpos2chapter(assignment_to_clusters):
    mapping = load_mapping_id2chapter()
    clusters = defaultdict(list)
    for fairy_tale_id in range(0, len(assignment_to_clusters)):
        cluster_id = assignment_to_clusters[fairy_tale_id]
        clusters[cluster_id].append(mapping[fairy_tale_id])
    return clusters


def calculate_precision_recall(expected_cluster, actual_cluster):
    expected_cluster = set(expected_cluster)
    actual_cluster = set(actual_cluster)
    overlap = 0
    for fairy_tale in expected_cluster:
        overlap += 1 if fairy_tale in actual_cluster else 0
    precision = overlap / len(actual_cluster)
    recall = overlap / len(expected_cluster)
    return precision, recall

