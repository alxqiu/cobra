# Sidewinder
 Angle simulation and experimentation for emulating sidewinding motion with a robotic snake.


joint_positions.py : contains constants for wave generation for both angle_plot.py and animation.py. Functions sine()
	and find_joint_coords perform the calculation work. Run this file to get a sample of positions for a single
	sine function, the runtime for finding coordinates, and a plot of the positions and sine graph. 

angle_plot.py : Methods for plotting the angle as the sine wave in joint_positions is shifted to the right [0, WAVLENGTH],
	or completes one cycle. joint_angle(n) displays the plot of the n-th joint, with the 0-th joint being the one at
	x = 0, which can be interpreted as the tip of the head of the snake. The angle measured is currently the 
	angle of the vector from the n-th to n+1-th joints, respective to the x-axis. 

animation.py : animating the behavior of the joint finding algorithm with the wave defined by joint_positions.py. 
	

External Dependencies:
	PyQt5, matplotlib, numpy
	Others are built in for Python 3

Next Steps:
	Develop measurement system for the angle of each joint relative to the angle the previous one was turned to. 
	
	Once relative angles can be measured, find a function to represent it.

	Perhaps see if measuring and plotting changes in angle is more useful, as that tells us how much each
		motor needs to turn at each point in the wave. 



