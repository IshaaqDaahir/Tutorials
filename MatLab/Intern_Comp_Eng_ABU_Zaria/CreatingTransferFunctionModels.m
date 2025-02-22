% Creating Transfer Function Models Using The CST function "tf"
% sys = tf(num, denom)

% Example: Create the first order transfer function (gain 10, time constant
% 5s)? - G(s) = 10/(5s + 1).

G = tf([10],[5 1])

%% Create a Transfer Function Model with a Time Delay.
% Consider the above model with a 2s time delay - Gd(se)^-2s = 10/(5s + 1).

Gd = tf([10],[5 1], 'InputDelay',2)

%% Setting and Accessing LTI Model Properties
% Example: Accessing the Model's Parameters Using the "get()" function
% - Access the properties of the transfer function Gd defined earlier:

get(Gd)

%% Example: Get a Specific Model Parameter Using "get()" function
% Retrieve the value of the property InputDelay of Gd:

Tdvec = get(Gd, "InputDelay")

%% Set Model Parameters Using "set()" function
% Set the property InputName of Gd to {'Voltage'}, a cell array:

set(Gd, 'InputName', {'Voltage'}) 
get(Gd, 'InputName');
get(Gd)





