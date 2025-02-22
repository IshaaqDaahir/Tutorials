% Vectors
a = [1 2 3 4 5 6 9 8 7]
t = 0:2:20
b = (a + 2)
c = (a + b)
d = (a - b)
e = (a .* b)
f = (a / b)

%%
% Functions
sin(pi/4)

%%
% Plotting
t = 0:0.25:7;
y = sin(t);
plot(t,y)
title('Sine wave as a function of time')
xlabel('t')
ylabel('y')

%%
% Polynomials
% s^4 + 3s^3 - 15s^2 + 9s - 2
x = [1 3 15 9 2]

%%
% s^4 + 1
y = [1 0 0 0 1]

%%
% Value of a polynomial using "polyval" function at s = 2.
z = polyval([1 0 0 0 1],2)

%%
% Roots of a polynomial
roots([1 3 -15 9 -2])

%%
% Product of two polynomials using a "conc" function.
x = [1 2];
y = [1 4 8];
z = conv(x,y)

%%
% Division of two polynomials using "deconv" function.
[xx, R] = deconv(z,y)

%%
% Matrices
B = [1 2 3 4; 5 6 7 8; 9 10 11 12]

%%
% Transpose using "Apostrophe" key.
C = B'

%%
% Multiplication of two matrices
D = B * C

%%
% Multiplication of two matrices
D = C * B

%%
% Multiplication of corresponding elements of two matrices using ".*"
E = [1 2;3 4]
F = [2 3;4 5]
G = E .* F

%%
% Multiplication of matrix by itself
E^3

%%
% Qubing of matrix's corresponding elements 
E.^3

%%
% Inverse of a matrix
X = inv(E)

%%
% Eigen-values of a matrix
eig(E)

%%
% Coefficient of the characteristics polynomial of a matrix using "poly"
% function
P = poly(E)

%%
% Eigen-value of a matrix is the same as the roots of its characteristics 
% polynomial of a matrix
roots(P)

%% Using M-Files in Matlab
% Creating Scripts
edit testscript.m

%% 
% Running Scripts by writing script names
testscript

%% 
% Printing current working directory
pwd

%% 
% Printing files in a current working directory
dir

%% 
% Saving worspace variables in a file
save Worksp a b B c C d D e E f F G P R t x X xx y z

%% 
% Loading the saved worspace variables from a file
load Worksp

%% Matlab Functions
% Function declaration
% function vec_sum = my_sum(x);

%% The function is applied here
z = rand(100,1);        % generates a random vector with 100 entries

% Summing "z" elements
z_sum = my_sum(z)       % use the function "my_sum" to sum elements
