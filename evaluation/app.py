from evaluation.__helper import *


expected_clusters = load_grimm_classification_clusters()

for condition, assignment_to_clusters in read_matlab_clusters().items():
    print('####\n' + condition)
    actual_clusters = map_matlabpos2chapter(assignment_to_clusters)
    print('#cluster:', len(actual_clusters))

    for cluster_id, actual_cluster in actual_clusters.items():
        for expected_cluster_name, expected_cluster in expected_clusters.items():
            precision, recall = calculate_precision_recall(expected_cluster, actual_cluster)
            f = 2.0 * precision * recall / (precision + recall) if precision + recall > 0 else 0
            if f > 0.6 or precision > 0.9 or recall > 0.9:
                print('actual cluster:', cluster_id)
                print('\texpected cluster:', expected_cluster_name)
                print('\t\tprecision:', precision, ', recall:', recall, ', f:', f)

