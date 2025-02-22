% We Use "series()", "parallel()" and "feedback" functions
% Example: Given - Ga(s) = 1/(s+2) and Gb(s) = 3/(s+4).

% Create the two sysyems:
Ga = tf(1, [1 2])
Gb = tf(3, [1 4])

%% 
% Connect Ga(s) and Gb(s) in cascade or series, so Gser(s) becomes
% Ga(s)*Gb(s):

Gser = series(Ga, Gb)

%% 
% Connect Ga(s) and Gb(s) in parallel, so Gpar(s) becomes Ga(s)+Gb(s):

Gpar = parallel(Ga, Gb)

%% 
% Ga(s) and Gb(s) are connected in a negative feedback loop with Ga(s)
% being in the forward path and Gb(s) being in the negative feedback path:
feedbsignN = -1;
feedbsignP = 1;
HfeedbN = feedback(Ga, Gb, feedbsignN);
HfeedbP = feedback(Ga, Gb, feedbsignP)

%% 
% The transfer function HfeedbN(s), HfeedbP(s) are given by:
% HfeedbN(s) = Ga(s)/[1 + feedbsignN*Ga(s)*Gb(s)]
% HfeedbP(s) = Ga(s)/[1 + feedbsignP*Ga(s)*Gb(s)]

HfeedbN = Ga/[1 + feedbsignN*Ga*Gb]
HfeedbP = Ga/[1 + feedbsignP*Ga*Gb]


