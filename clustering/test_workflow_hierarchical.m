disp('---START---')
path_to_sentence_lengths = 'test_fairy_tales_lengths.csv';
disp(strcat('reading from: ', path_to_sentence_lengths, ' ... '));
points = transpose(dlmread(path_to_sentence_lengths, '\t'))
pause


metrics = {'euclidean', 'cosine'};
for metric = metrics
    metric = metric{1};
    disp(metric)
    distances = pdist(points, metric);
    linkage_methods = {'average', 'centroid', 'single'};
    for method = linkage_methods
        method = method{1};
        if and(strcmp(method, 'centroid'), not(strcmp(metric, 'euclidean')))
            continue
        end
        
        tree = linkage(distances, method);
        figure('Name', strcat(metric, '-', method))
        dendrogram(tree)
    end
    pause
end

disp('--- END ---')
