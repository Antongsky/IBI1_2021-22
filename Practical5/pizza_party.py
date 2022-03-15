n=1 # n is the number of cuts
while (n**2+n+2)/2<=100: #(n**2+n+2)/2 is the piece. I think 100 is big enough to set. Nevertheless, the figure can be bigger and it doesn't matter.
	if(n**2+n+2)/2<=64: #If the piece is under 64, that means it's not enough to distribute the pizza to everyone,so we have to make n bigger.
		print("cut "+str(n)+" times, we can get "+str((n**2+n+2)/2)+" pieces, that's not enough!" ) 
		n=n+1 
	else:         #If the piece>=64, it's enough to distribute the pizza to everyone, so we can print the figure out and quit.
		print("cut "+str(n)+" times, we can get "+str((n**2+n+2)/2)+"pieces, enough!")
		exit()
		
	