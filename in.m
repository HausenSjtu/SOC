for i = 1:195
    a = [zeros(i,200); zeros(5,i) ones(5) zeros(5,200-5-i); zeros(200-5-i,200)];
    imshow(a);
    pause(0.1);
end