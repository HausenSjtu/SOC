clear;
close all;

% a=eye(100);
% fout = fopen('out.txt','w');
% fprintf(fout,'%d\n',a);
% fclose(fout);

% fin = fopen('out.txt')
% [b count ]=fscanf(fin,'%d',10000);
% fclose(fin);
% b = reshape(b,100,100);


% for i=1:100
%     pause(0.2);
%     disp(i);
% end

for i=1:200
    fb = fopen('pyout.txt','rb');
    b = fread(fb,[200,200],'double');
    % b = reshape(b,200,200);
    imshow(b);
    fclose(fb);
    i
    pause(0.5);
end