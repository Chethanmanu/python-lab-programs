import random
l=["r","p","s"]
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0
while True:
	#take input from user
	u=input("enter your choice ,press n to discontinue")
	#to exit
	if u=='n':
		print("game over")
		print("computer score:",cs)
		print("user score",us)
		if cs==us:
		    print("tie")
		elif cs > us:
			print("computer wins")
		else:
			print("user wins")
		exit()
	#input from computer
	c=random.choice(l)
	print ("computer chooses",c)
    #compare the user and computer choice 
	if u == c:
		print("tie")

	elif u=='r' and c=='p':
		print("comp wins")
		cs+=1
	elif u=='r' and c=='s':
		 print("user wins")
		 us+=1

	elif u=='p' and c=='r':
		print("comp wins")
		us+=1
	elif u=='p' and c=='s':
		print("user wins")
		us+=1
	elif u=='s' and c=='r':
	     print("comp wins")
	     cs+=1
	elif u=='s' and c=='p':
	     print("user wins")
	     us+=1