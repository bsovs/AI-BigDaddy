# Big Daddy, version 1.0 \\
# Created by B_sovs \\

import webbrowser, sys, random, string, os.path, getpass, time, itertools

path = 'C:\Python27\Big_Daddy'
os.chdir(path)

#status variables
var_mood = False

print
print 'Big Daddy, version 1.0'
print 'Press ctr+c to exit'
print
print 'Hello. How are you today?'

#Responses
greet = ['Hi', 'Hello', 'Hey', "What's up", "How's it going?"]
bye = ['See you later', 'See you', 'Take it easy', 'Bye']
	
#Inputs
my_name = ['say my name', 'who am i', 'my name is', "what's my name"]
my_hello = ['hi', 'hey', 'hello', 'hey there', 'hi big daddy', 'hey big daddy']
my_search = ['search', 'look up', 'google']
my_new_user = ['new user', 'new name', 'new username', 'new user-name', 'change name']
my_exit = ['bye', 'see ya', 'see you later', 'bye big daddy', 'exit', 'quit']
my_mood = ['good', 'bad', 'happy', 'sad', 'angry', 'mad', 'tired', 'sleepy', 'anxious']
bad_mood = ['bad','sad', 'angry', 'mad', 'tired', 'sleepy', 'anxious']

while True:
	#User Input
	userInput = raw_input(">>> ")
	userInput = (userInput.lower())
	
	#Pre-fixes
	input_fix = userInput.split() #split words
	input_list = list(userInput) #list letters
	mood_fix = ['i feel', 'i feel very', 'i am']
	mood_num = 0
	
	#Change prefix sentences so AI can understand 
	for mood in my_mood:
		mood_num = 0
		while mood_num <= 2:
			new_mood = mood_fix[mood_num]+' '+mood
			if new_mood in userInput:
				userInput = userInput.replace(mood_fix[mood_num], '')
				input_list = list(userInput)
			mood_num = mood_num + 1
	while userInput.find(' ') == 0:
		input_list[0] = ''
		userInput = ''.join(input_list)
		input_list = list(userInput)
	if len(userInput.split()) == 1: #Get rid of extra spaces
		userInput = userInput.replace(' ', '')
	
	#AI Responses to Commands
	if userInput == 'reset':
		var_mood = False
		continue
	#Initial responses
	if userInput in my_hello:
		print random.choice(greet);
	elif userInput in my_new_user: #greeting
		username = raw_input('Input a new username: ');
		file = open('username.txt', 'w');
		file.write(username);
		print 'Username has been set'
		file.close();
	elif userInput in my_name: #your name
		file = open('username.txt', 'r');
		myname = file.read();
		if myname == '':
			choice = raw_input('You do not have a username set. Would you like to set one? (y)es, (n)o, (q)uit: ');
			if choice == 'y':
				print
				username = raw_input('Input a username: ');
				file = open('username.txt', 'w');
				file.write(username);
				print 'Username has been set'
				file.close();
			elif choice == 'q':
				print 'See you later'
				break
		else:	
			print 'Your name is '+myname;
			file.close();
	elif userInput in my_mood: #Adjust to mood
		user_mood = userInput
		var_mood = True
		if user_mood in bad_mood:
			print 'I see '+getpass.getuser()+"... I'm feeling a bit "+user_mood+' as well' 
			dot = '.','.','.'
			for dot in dot:
				print dot,
				time.sleep(1)
			print "Let's talk about it."
		else: print 'Awesome '+getpass.getuser()+'! I feel super '+user_mood+' as well.'
		break
	elif userInput in my_search: #search
		search = raw_input('What would you like to search? ');
		print
		print 'Searching: '+search;
		print
		time.sleep(1)
		new=2;
		url='http://google.com#q='+search;
		webbrowser.open(url, new=new);
	elif userInput in my_exit: #exit BD
		print random.choice(bye)+' '+getpass.getuser();
		break
	else: #Did not understand
		print("I did not quite understand what you said. Can you say it again please.")

while True:
	#User Input
	userInput = raw_input(">>> ")
	userInput = (userInput.lower())

	#Secondary state
	if var_mood == True:
		if user_mood == bad_mood:
			print 'It is ok to feel this way sometimes. Lets try to work this out together.'
		else:
			print 'Let us try and find what is making you feel good, so you can stay happy all the time.'		
	else: break	