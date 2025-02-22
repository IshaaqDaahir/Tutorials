% Example: Vector Sum Matlab Function
% Sums the element of a vector
function vec_sum = my_sum(x)
    vec_sum = 0;    
    for i = 1:length(x)
        vec_sum = vec_sum + x(i);
    end
    


