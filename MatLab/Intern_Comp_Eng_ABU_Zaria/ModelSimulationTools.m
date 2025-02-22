% Consider a continuous time transfer function - Glc(s)=(s+0.5)/(s^2+2s+4).
% Create Glc(s)
Glc = tf([1 0.5], [1 2 4])

%% Simulation (time response)
% Simulation of step response with the "step()" function. The input step is
% a unit step (the step height is equal to one applied at time t=0).

% Simulate the Systems's Step Response - Simulate Glc from t=0 to t=10 time
% units?

step(Glc,10);
legend('Figure 5: Continuous time step response')

%%
% Storing simulated time response,y, and the time vector,t, by using return
% (left) arguments:
[y,t] = step(Glc, 10);

%%
% The "impulse()" function simulates the impulse response.
% Example: Simulate the System's Impulse Response

impulse(Glc, 10);
legend('Figure 6: Continuous time impulse response')

%%
% "lsim()" function is more general as it accepts any input signal, not
% just step or impulse. To generate the input signal, we may use the 
% "gensig()" function which produces a sine wave, or a square wave, or
% periodic pulses.

% Example: Systems Response to a General Input Signal.
% Simulate Glc with a sinusoidal input,u, having a period Tp=0.5, final
% time Tf=10, and time step Tstep=0.01:

Tp = 0.5; Tf = 10; Tstep = 0.01;
[u, t] = gensig('sin', Tp, Tf, Tstep);  % Sine wave input
lsim(Glc, u, t);
legend('Figure 7: Continuous time sinusoidal response')

%%
[u, t] = gensig('square', Tp, Tf, Tstep);   % Square wave input
lsim(Glc, u, t);

%%
[u, t] = gensig('pulse', Tp, Tf, Tstep);   % Pulse input
lsim(Glc, u, t);


