% Introductory Example
% First Order Closed Loop Step Response Simulation With Unity Feedback
num = [10];             % First Order Transfer Function With Gain Of "10"
den = [5 1];            % First Order TF With Time Constant "5"   
G = tf(num,den);        % Open Loop Transfer Function
H = G/(1 + G)           % Closed Loop Transfer Function
H = minreal(H);         % Remove Cancelling Poles/Zeros
t = [0:0.1:4]';         % Simulation Time Interval
y = step(H,t);          % Simulate Step Response
plot(t,y);              % Plot Step Response
title('Figure 4: Closed loop step response as calculated by the CST')
xlabel('t')
ylabel('y')

