import os
import pickle

brightness = pickle.load(open("/home/bharat/brightness_fix/brightness_var", "rb"))
if brightness <= 0:
	brightness = 0
else:
	brightness -= 0.05
	
pickle.dump(brightness,open("/home/bharat/brightness_fix/brightness_var", "wb"))
command = "xrandr --output DP-2 --brightness {}".format(brightness)
os.system(command)
