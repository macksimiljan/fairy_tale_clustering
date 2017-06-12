disp('---START---')
path_to_sentence_lengths = 'grimm_lengths.csv';
disp(strcat('reading from: ', path_to_sentence_lengths, ' ... '));
points = transpose(dlmread(path_to_sentence_lengths, '\t'));

metrics = {'euclidean', 'cosine'};
for metric = metrics
    metric = metric{1};
    distances = pdist(points, metric);
    linkage_methods = {'average', 'single'};
    for method = linkage_methods
        method = method{1};
        disp(strcat(metric, '.', method))
        if and(strcmp(method, 'centroid'), not(strcmp(metric, 'euclidean')))
            continue
        end
        
        tree = linkage(distances, method);
%         figure('Name', strcat('dendrogram: ', metric, '-', method))
%         dendrogram(tree, 205);

        cophenetic_correlation = cophenet(tree, distances);
        if cophenetic_correlation < 0.6
            continue
        end
        
        disp(strcat('cophenetic_corr=', num2str(cophenetic_correlation)))
        inconsistency = inconsistent(tree);
        
        inconsistency_coefficient = 1.0;
        assignment_to_clusters_by_incons = cluster(tree, 'cutoff', inconsistency_coefficient);
        disp(strcat('assignment_to_clusters_by_incons=', mat2str(assignment_to_clusters_by_incons)))
        
        expected_number = 10;
        assignment_to_clusters_by_number = cluster(tree, 'maxclust', expected_number);
        disp(strcat('assignment_to_clusters_by_number=', mat2str(assignment_to_clusters_by_number)))
        
        disp('#####')
        
        
%         figure('Name', strcat('silhouette: ', metric, '-', method))
%         silhouette(points, assignment_to_clusters)
    end
end

disp('--- END ---')
