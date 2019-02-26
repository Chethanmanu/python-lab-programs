import random
l=["r","p","s"]
while True:
	#take input from user
	u=input("enter your choice ,press n to discontinue")
	#to exit
	if u=='n':
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)
	print ("computer chooses",c)

	#compare the user and computer choice 
	if u == c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
	elif u == 'r' and c =='s':
		 print("user wins")