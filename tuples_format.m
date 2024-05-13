filename = 'chromosome_1_matrix.txt'; 
check = dlmread(filename);
cont = dlmread(filename);
len = length(cont);
c = [];
for row = 1:len
   for col = row:len
       IF = cont(row, col);
       c = [c; row, col, IF];  
   end
end
dlmwrite('chromosome_1_tuple.txt', c, 'delimiter', ' ');
disp('Conversion to Tuple Format Done successfully');