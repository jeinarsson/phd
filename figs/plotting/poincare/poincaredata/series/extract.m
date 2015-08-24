
clear all;

files = dir('*.mat')
num = length(files);
for k=1:num
    
    file = files(k).name
    
    load(file);
    save(file,'-v7.3');
    
end