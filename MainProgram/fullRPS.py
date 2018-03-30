import random
winEas = loseEas = tieEas = winInt = loseInt = tieInt = winHard = loseHard = tieHard = winExp = loseExp = tieExp = winspec = losespec = tiespec = 0.0

buildTMatrix = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}

n = 3
m = 3
tMatrix = [[0] * m for i in range(n)]
tMatrixL = [[0] * m for i in range(n)]
tMatrixT = [[0] * m for i in range(n)]

probabilitiesRPS = [1/3,1/3,1/3]

buildTMatrixrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}
buildTMatrixLrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}
buildTMatrixTrpsclsp = {'rr': 1, 'rp': 1, 'rsc': 1, 'rl': 1, 'rsp': 1, 'pr': 1, 'pp': 1, 'psc': 1, 'pl': 1, 'psp': 1, 'scr': 1, 'scp': 1, 'scsc': 1, 'scl': 1, 'scsp': 1, 'lr': 1, 'lp': 1, 'lsc': 1, 'll': 1, 'lsp': 1, 'spr': 1, 'spp': 1, 'spsc': 1, 'spl': 1, 'spsp': 1}

sheldon = 5
cooper = 5
tMatrixrpsclsp = [[0] * sheldon for i in range(cooper)]
tMatrixLrpsclsp = [[0] * sheldon for i in range(cooper)]
tMatrixTrpsclsp = [[0] * sheldon for i in range(cooper)]

probabilitiesrpsclsp = [1/5,1/5,1/5,1/5,1/5]

def chooseMode():
  mode = 6
  try:
    mode = int(input("What Mode do you want to play in? 1: beginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
  except ValueError:
    print("you must enter an integer \n")

  if(mode > 4 and mode != 73):
    print ("You must enter an integer less than five \n")
    while(mode > 4 and mode != 73):
      try:
        mode = int(input("What Mode do you want to play in? 1: begginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
      except ValueError:
        print("you must enter an integer \n")
  return mode

def easyMode():
  choices = ["Rock","Paper","Scissors"]
  continuePlaying = True
  continueGame = ""
  try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if(choice > 2 or choice < 0):
    print ("You must enter an integer less than three and greater than 0  \n")
    while(choice > 2 or choice < 0):
      print ("You must enter an integer less than three and greater than 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 2)
  result = checkWin(choice,machineChoice,1)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  while(continuePlaying):
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 2 or choice < 0) and choice != 5):
        print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 5):
      print ("Thanks for Playing!")
      continuePlaying = False
    else:
      machineChoice = random.randint(0, 2)
      result = checkWin(choice,machineChoice,1)

      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

def intermediateMode():
	choices = ["Rock", "Paper", "Scissors"]
	continuePlaying = True
	continueGame = ""
	prevChoice = ""
	prevMachineChoice = ""
	result = ""
	streak = 0
	won = 0
	alt = 0
	numoff = 0
	choice = 3

	try:
		choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
	except ValueError:
		print("you must enter an integer \n")

	if (choice > 2 or choice < 0):
		print(
		    "You must enter an integer less than three and greater than or equal to 0. \n")
		while (choice > 2 or choice < 0):
			try:
				choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
			except ValueError:
				print("you must enter an integer \n")
	machineChoice = random.randint(0, 2)
	result = checkWin(choice, machineChoice, 2)
	if (result == "Win!"):
		won += 1
	else:
		numoff += 1
		if (numoff == 3):
			won -= 3
			numoff = 0
		if (won < 0):
			won = 0

	print("You chose %s" % choices[choice])
	print("The machine chose %s" % choices[machineChoice])
	print("You %s" % result)

	prevChoice = choice
	prevMachineChoice = machineChoice
	streak += 1

	while (continuePlaying):
		try:
			choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
		except ValueError:
			print("you must enter an integer \n")

		if ((choice > 2 or choice < 0) and choice != 5):
			print(
			    "You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit \n"
			)
			while ((choice > 2 or choice < 0) and choice != 5):
				try:
					print(
					    "You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit \n"
					)
					choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
				except ValueError:
					print("you must enter an integer \n")

		if (choice == 5):
			print("Thanks for Playing!")
			continuePlaying = False
		else:
			if (prevChoice == choice):
				streak += 1
			else:
				streak -= 1
				if (streak < 0):
					streak = 0
			if (streak > 3):
				machineChoice = prevChoice - 2
				if (machineChoice < 0):
					machineChoice += 3
			elif (won > 9):
				print(
				    "Yo. Stop cheating and keep your eyes off my code. Just play normally. You wouldn't be able to look at previous decisions so accurately in a real game alright? If ya continue to do dis the machine won't care anymore - it's a sore loser and hates people like you."
				)
				machineChoice = random.randint(0, 2)
			elif (won > 3 and won < 10):
				machineChoice = prevChoice
			else:
				if (result == "Win!"):
					machineChoice = prevChoice - 2
					if (machineChoice < 0):
						machineChoice += 3
				elif (result == "Lose!"):
					machineChoice = prevChoice + 1
					if (machineChoice > 2):
						machineChoice -= 3
					machineChoice -= 2
					if (machineChoice < 0):
						machineChoice += 3
				else:
					machineChoice = random.randint(0, 2)

			result = checkWin(choice, machineChoice, 2)

			if (result == "Win!"):
				won += 1
			else:
				won -= 2
				if (won < 0):
					won = 0

			print("You chose %s" % choices[choice])
			print("The machine chose %s" % choices[machineChoice])
			print("You %s" % result)
			prevChoice = choice

def expertMode():
  global probabilitiesRPS
  choices = ["Rock","Paper","Scissors"]
  choi = ['r','p','s']
  continuePlaying = True
  prevChoice = ""
  choice = 3
  probRock = 0
  probPaper = 0
  probScissors = 0

  try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 2 or choice < 0)):
    print ("You must enter an integer less than three and greater than or equal to 0  \n")
    while((choice > 2 or choice < 0)):
      print ("You must enter an integer less than three and greater than or equal to 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 2)
  result = checkWin(choice,machineChoice,3)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  prevChoice = choice

  while(continuePlaying):
    choice = 3
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 2 or choice < 0) and choice != 5):
        print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 5):
      print("Thanks for Playing!\n")
      continuePlaying = False
    else:
      transMatrix = buildTransitionProbabilities(prevChoice,choice,result)
      machineChoice = random.randint(1, 100)
      probabilitiesRPS[0] = transMatrix[prevChoice][0]
      probabilitiesRPS[1] = transMatrix[prevChoice][1]
      probabilitiesRPS[2] = transMatrix[prevChoice][2]
      rangeR = probabilitiesRPS[0] * 100
      rangeP = probabilitiesRPS[1] * 100 + rangeR
      if (machineChoice <= rangeR):
        machineChoice = 1
      elif (machineChoice <= rangeP):
        machineChoice = 2
      else:
        machineChoice = 0

      result = checkWin(choice,machineChoice,3)
      prevChoice = choice
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

  #print("Your winning transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrix[0],tMatrix[1],tMatrix[2]))
  #print("Your losing transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixL[0],tMatrixL[1],tMatrixL[2]))
  #print("Your tying transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixT[0],tMatrixT[1],tMatrixT[2]))

def buildTransitionProbabilities(pC,c,winloss):
  global buildTMatrix
  global buildTMatrixL
  global buildTMatrixT
  choi = ['r','p','s']

  if winloss == "Win!":
    for i, x in buildTMatrix.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrix['%s%s' % (choi[pC], choi[c])] += 1
  elif winloss == "Tied!":
    for i, x in buildTMatrixT.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixT['%s%s' % (choi[pC], choi[c])] += 1
  else:
    for i, x in buildTMatrixL.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixL['%s%s' % (choi[pC], choi[c])] += 1

  return buildTransitionMatrix(winloss)

def buildTransitionMatrix(winlosstwo):
  global tMatrix
  global tMatrixL
  global tMatrixT

  if winlosstwo == "Win!":
    rock = buildTMatrix['rr'] + buildTMatrix['rs'] +buildTMatrix['rp']
    paper = buildTMatrix['pr'] + buildTMatrix['ps'] +buildTMatrix['pp']
    scissors = buildTMatrix['sr'] + buildTMatrix['ss'] +buildTMatrix['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrix):
      for col_index, item in enumerate(row):
          a = int(buildTMatrix['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrix)
  elif winlosstwo == "Tied!":
    rock = buildTMatrixT['rr'] + buildTMatrixT['rs'] +buildTMatrixT['rp']
    paper = buildTMatrixT['pr'] + buildTMatrixT['ps'] +buildTMatrixT['pp']
    scissors = buildTMatrixT['sr'] + buildTMatrixT['ss'] +buildTMatrixT['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixT):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixT['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixT)

  else:
    rock = buildTMatrixL['rr'] + buildTMatrixL['rs'] +buildTMatrixL['rp']
    paper = buildTMatrixL['pr'] + buildTMatrixL['ps'] +buildTMatrixL['pp']
    scissors = buildTMatrixL['sr'] + buildTMatrixL['ss'] +buildTMatrixL['sp']
    choi = ['r','p','s']
    for row_index, row in enumerate(tMatrixL):
      for col_index, item in enumerate(row):
          a = int(buildTMatrixL['%s%s' % (choi[row_index],choi[col_index])])
          if (row_index == 0):
            c = a/rock
          elif (row_index == 1):
            c = a/paper
          else:
            c = a/scissors
          row[col_index] = float(c)
    return (tMatrixL)
def superHard():
  choices = ["Rock","Paper","Scissors"]
  continuePlaying = True
  continueGame = ""
  result = ""
  print ("I am going to play %s" % choices[random.randint(0, 2)])
  try:
    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 2 or choice < 0)):
    print ("You must enter an integer less than three and greater than or equal to 0 \n")
    while((choice > 2 or choice < 0)):
      try:
        print ("You must enter an integer less than three and greater than or equal to 0 \n")
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = choice - 2
  if (machineChoice < 0):
    machineChoice += 3

  result = checkWin(choice,machineChoice,4)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  while(continuePlaying):
    print ("I am going to play %s" % choices[random.randint(0, 2)])
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 2 or choice < 0) and choice != 5):
      print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit. \n")
      while((choice > 2 or choice < 0) and choice != 5):
        try:
          print ("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit. \n")
          choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
          print("you must enter an integer \n")

    if (choice == 5):
      print("Giving up? How sad :(")
      continuePlaying = False
    else:
      machineChoice = choice - 2
      if (machineChoice < 0):
        machineChoice += 3

      result = checkWin(choice,machineChoice,4)
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

def bigbang():
  global probabilitiesRPS
  print(
  """
    As a wise man said:
    
    Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.
  """)
  choices = ["Rock","Paper","Scissors","Lizard","Spock"]
  choi = ['r','p','sc','l','sp']
  continuePlaying = True
  prevChoice = ""
  choice = 8
  probRock = 0
  probPaper = 0
  probScissors = 0
  probLizard = 0
  probSpock = 0

  try:
    choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
  except ValueError:
    print("you must enter an integer \n")

  if((choice > 4 or choice < 0)):
    print ("You must enter an integer less than five and greater than or equal to 0  \n")
    while((choice > 4 or choice < 0)):
      print ("You must enter an integer less than five and greater than or equal to 0 \n")
      try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
      except ValueError:
        print("you must enter an integer \n")

  machineChoice = random.randint(0, 4)
  result = checkWin(choice,machineChoice,1)
  print ("You chose %s" % choices[choice])
  print ("The machine chose %s" % choices[machineChoice])
  print("You %s" % result)

  prevChoice = choice

  while(continuePlaying):
    choice = 8
    try:
      choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
    except ValueError:
      print("you must enter an integer \n")

    if((choice > 4 or choice < 0) and choice != 7):
      print ("You must enter an integer less than five and greater than or equal to 0 or choose 5 to exit.  \n")
      while((choice > 4 or choice < 0) and choice != 7):
        print ("You must enter an integer less than five and greater than or equal to 0 or choose 5 to exit.\n")
        try:
          choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
        except ValueError:
          print("you must enter an integer \n")
    if (choice == 7):
      print ("There's just no pleasing you, is there, Leonard?")
      continuePlaying = False
    else:
      transMatrix = buildTransitionProbabilitiesrpsclsp(prevChoice,choice,result)
      machineChoice = random.randint(1, 100)
      probabilitiesrpsclsp[0] = transMatrix[prevChoice][0]
      probabilitiesrpsclsp[1] = transMatrix[prevChoice][1]
      probabilitiesrpsclsp[2] = transMatrix[prevChoice][2]
      probabilitiesrpsclsp[3] = transMatrix[prevChoice][3]
      probabilitiesrpsclsp[4] = transMatrix[prevChoice][4]
      rangeR = probabilitiesrpsclsp[0] * 100
      rangeP = probabilitiesrpsclsp[1] * 100 + rangeR
      rangeSC = probabilitiesrpsclsp[2] * 100 + rangeP
      rangeL = probabilitiesrpsclsp[3] * 100 + rangeSC
      oneOrTwo = random.randint(1,2)
      if (machineChoice <= rangeR):
          if (oneOrTwo == 1):
              machineChoice = 1
          else:
              machineChoice = 4
      elif (machineChoice <= rangeP):
          if (oneOrTwo == 1):
              machineChoice = 2
          else:
              machineChoice = 3
      elif (machineChoice <= rangeSC):
          if (oneOrTwo == 1):
              machineChoice = 4
          else:
              machineChoice = 0
      elif (machineChoice <= rangeL):
          if (oneOrTwo == 1):
              machineChoice = 2
          else:
              machineChoice = 0
      else:
          if (oneOrTwo == 1):
              machineChoice = 1
          else:
              machineChoice = 3
      result = checkWin(choice,machineChoice,73)
      prevChoice = choice
      print ("You chose %s" % choices[choice])
      print ("The machine chose %s" % choices[machineChoice])
      print("You %s" % result)

  #print("Your winning transition matrix is:\nr: %s\np: %s\nsc: %s\nl: %s\nsp: %s\n" % (tMatrixrpsclsp[0],tMatrixrpsclsp[1],tMatrixrpsclsp[2],tMatrixrpsclsp[3],tMatrixrpsclsp[4]))
  #print("Your losing transition matrix is:\nr: %s\np: %s\nsc: %s\nl: %s\nsp: %s\n" % (tMatrixLrpsclsp[0],tMatrixLrpsclsp[1],tMatrixLrpsclsp[2],tMatrixLrpsclsp[3],tMatrixLrpsclsp[4]))
  #print("Your tying transition matrix is:\nr: %s\np: %s\nsc: %s\nl: %s\nsp: %s\n" % (tMatrixTrpsclsp[0],tMatrixTrpsclsp[1],tMatrixTrpsclsp[2],tMatrixTrpsclsp[3],tMatrixTrpsclsp[4]))

def buildTransitionProbabilitiesrpsclsp(pC,c,winloss):
  global buildTMatrixrpsclsp
  global buildTMatrixLrpsclsp
  global buildTMatrixTrpsclsp
  choi = ['r','p','sc','l','sp']

  if winloss == "Win!":
    for i, x in buildTMatrixrpsclsp.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixrpsclsp['%s%s' % (choi[pC], choi[c])] += 1
  elif winloss == "Tied!":
    for i, x in buildTMatrixTrpsclsp.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixTrpsclsp['%s%s' % (choi[pC], choi[c])] += 1
  else:
    for i, x in buildTMatrixLrpsclsp.items():
      if ('%s%s' % (choi[pC],choi[c]) == i):
        buildTMatrixLrpsclsp['%s%s' % (choi[pC], choi[c])] += 1

  return buildTransitionMatrixrpsclsp(winloss)

def buildTransitionMatrixrpsclsp(winlosstwo):
    global tMatrixrpsclsp
    global tMatrixTrpsclsp
    global tMatrixLrpsclsp

    if winlosstwo == "Win!":
        rock = buildTMatrixrpsclsp['rr'] + buildTMatrixrpsclsp['rsc'] + buildTMatrixrpsclsp['rp'] + buildTMatrixrpsclsp['rl'] +buildTMatrixrpsclsp['rsp']
        paper = buildTMatrixrpsclsp['pr'] + buildTMatrixrpsclsp['psc'] + buildTMatrixrpsclsp['pp'] + buildTMatrixrpsclsp['pl'] +buildTMatrixrpsclsp['psp']
        scissors = buildTMatrixrpsclsp['scr'] + buildTMatrixrpsclsp['scsc'] + buildTMatrixrpsclsp['scp'] + buildTMatrixrpsclsp['scl'] +buildTMatrixrpsclsp['scsp']
        lizard = buildTMatrixrpsclsp['lr'] + buildTMatrixrpsclsp['lsc'] + buildTMatrixrpsclsp['lp'] + buildTMatrixrpsclsp['ll'] +buildTMatrixrpsclsp['lsp']
        spock = buildTMatrixrpsclsp['spr'] + buildTMatrixrpsclsp['spsc'] + buildTMatrixrpsclsp['spp'] + buildTMatrixrpsclsp['spl'] +buildTMatrixrpsclsp['spsp']
        choi = ['r','p','sc','l','sp']
        for row_index, row in enumerate(tMatrixrpsclsp):
            for col_index, item in enumerate(row):
                a = int(buildTMatrixrpsclsp['%s%s' % (choi[row_index],choi[col_index])])
                if (row_index == 0):
                    c = a/rock
                elif (row_index == 1):
                    c = a/paper
                elif (row_index == 2):
                    c = a/scissors
                elif (row_index == 3):
                    c = a/lizard
                else:
                    c = a/spock
                row[col_index] = float(c)
        return (tMatrixrpsclsp)
    elif winlosstwo == "Tied!":
        rock = buildTMatrixTrpsclsp['rr'] + buildTMatrixTrpsclsp['rsc'] + buildTMatrixTrpsclsp['rp'] + buildTMatrixTrpsclsp['rl'] +buildTMatrixTrpsclsp['rsp']
        paper = buildTMatrixTrpsclsp['pr'] + buildTMatrixTrpsclsp['psc'] + buildTMatrixTrpsclsp['pp'] + buildTMatrixTrpsclsp['pl'] +buildTMatrixTrpsclsp['psp']
        scissors = buildTMatrixTrpsclsp['scr'] + buildTMatrixTrpsclsp['scsc'] + buildTMatrixTrpsclsp['scp'] + buildTMatrixTrpsclsp['scl'] +buildTMatrixTrpsclsp['scsp']
        lizard = buildTMatrixTrpsclsp['lr'] + buildTMatrixTrpsclsp['lsc'] + buildTMatrixTrpsclsp['lp'] + buildTMatrixTrpsclsp['ll'] +buildTMatrixTrpsclsp['lsp']
        spock = buildTMatrixTrpsclsp['spr'] + buildTMatrixTrpsclsp['spsc'] + buildTMatrixTrpsclsp['spp'] + buildTMatrixTrpsclsp['spl'] +buildTMatrixTrpsclsp['spsp']
        choi = ['r','p','sc','l','sp']
        for row_index, row in enumerate(tMatrixTrpsclsp):
            for col_index, item in enumerate(row):
                a = int(buildTMatrixTrpsclsp['%s%s' % (choi[row_index],choi[col_index])])
                if (row_index == 0):
                    c = a/rock
                elif (row_index == 1):
                    c = a/paper
                elif (row_index == 2):
                    c = a/scissors
                elif (row_index == 3):
                    c = a/lizard
                else:
                    c = a/spock
                row[col_index] = float(c)
        return (tMatrixTrpsclsp)
    else:
        rock = buildTMatrixLrpsclsp['rr'] + buildTMatrixLrpsclsp['rsc'] + buildTMatrixLrpsclsp['rp'] + buildTMatrixLrpsclsp['rl'] +buildTMatrixLrpsclsp['rsp']
        paper = buildTMatrixLrpsclsp['pr'] + buildTMatrixLrpsclsp['psc'] + buildTMatrixLrpsclsp['pp'] + buildTMatrixLrpsclsp['pl'] +buildTMatrixLrpsclsp['psp']
        scissors = buildTMatrixLrpsclsp['scr'] + buildTMatrixLrpsclsp['scsc'] + buildTMatrixLrpsclsp['scp'] + buildTMatrixLrpsclsp['scl'] +buildTMatrixLrpsclsp['scsp']
        lizard = buildTMatrixLrpsclsp['lr'] + buildTMatrixLrpsclsp['lsc'] + buildTMatrixLrpsclsp['lp'] + buildTMatrixLrpsclsp['ll'] +buildTMatrixLrpsclsp['lsp']
        spock = buildTMatrixLrpsclsp['spr'] + buildTMatrixLrpsclsp['spsc'] + buildTMatrixLrpsclsp['spp'] + buildTMatrixLrpsclsp['spl'] +buildTMatrixLrpsclsp['spsp']
        choi = ['r','p','sc','l','sp']
        for row_index, row in enumerate(tMatrixLrpsclsp):
            for col_index, item in enumerate(row):
                a = int(buildTMatrixLrpsclsp['%s%s' % (choi[row_index],choi[col_index])])
                if (row_index == 0):
                    c = a/rock
                elif (row_index == 1):
                    c = a/paper
                elif (row_index == 2):
                    c = a/scissors
                elif (row_index == 3):
                    c = a/lizard
                else:
                    c = a/spock
                row[col_index] = float(c)
        return (tMatrixLrpsclsp)

def checkWin(user, machine, mode):
    win = False
    tie = False
    if (mode == 73):
        if (user == 0):
            if (machine == 2 or machine == 3):
                win = True
                tie = False
            elif (machine == 1 or machine == 4):
                win = False
                tie = False
            elif (machine == 0):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        elif (user == 1):
            if (machine == 0 or machine == 4):
                win = True
                tie = False
            elif (machine == 2 or machine == 3):
                win = False
                tie = False
            elif (machine == 1):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        elif (user == 2):
            if (machine == 1 or machine == 3):
                win = True
                tie = False
            elif (machine == 0 or machine == 4):
                win = False
                tie = False
            elif (machine == 2):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        elif (user == 3):
            if (machine == 4 or machine == 1):
                win = True
                tie = False
            elif (machine == 2 or machine == 0):
                win = False
                tie = False
            elif (machine == 3):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        else:
            if (machine == 2 or machine == 0):
                win = True
                tie = False
            elif (machine == 1 or machine == 3):
                win = False
                tie = False
            elif (machine == 4):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
    else:
        if (user == 0):
            if (machine == 2):
                win = True
                tie = False
            elif (machine == 1):
                win = False
                tie = False
            elif (machine == 0):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        elif (user == 1):
            if (machine == 0):
                win = True
                tie = False
            elif (machine == 2):
                win = False
                tie = False
            elif (machine == 1):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)
        else:
            if (machine == 1):
                win = True
                tie = False
            elif (machine == 0):
                win = False
                tie = False
            elif (machine == 2):
                tie = True
            else:
                print ("Something wierd happened and machine was: %s" % machine)

    if (tie == True):
        checkStats(2, mode)
        return "Tied!"
    elif (win):
        checkStats(0, mode)
        return "Win!"
    else:
        checkStats(1, mode)
        return "Lose!"

def main():
  playAgain = True
  notyesorno = True

  while (playAgain):
    notyesorno = True
    playAgain = False
    chosenMode = chooseMode()
    if(chosenMode == 1):
      easyMode()
      percentWon = "{percent:.2%}".format(percent=(winEas/(winEas + loseEas +  tieEas)))
      print ("You won %d times on Easy Mode! \n" % winEas)
      print ("You lost %d times on Easy Mode! \n" % loseEas)
      print ("You tied %d times on Easy Mode! \n" % tieEas)
      print ("You have a %s win rate on Easy Mode!" % percentWon)
    elif (chosenMode == 2):
      intermediateMode()
      percentWon = "{percent:.2%}".format(percent=(winInt/(winInt + loseInt +  tieInt)))
      print ("You won %d times on Intermediate Mode! \n" % winInt)
      print ("You lost %d times on Intermediate Mode! \n" % loseInt)
      print ("You tied %d times on Intermediate Mode! \n" % tieInt)
      print ("You have a %s win rate on Intermediate Mode!" % percentWon)
    elif (chosenMode == 3):
      expertMode()
      percentWon = "{percent:.2%}".format(percent=(winExp/(winExp + loseExp +  tieExp)))
      print ("You won %d times on Expert Mode! \n" % winExp)
      print ("You lost %d times on Expert Mode! \n" % loseExp)
      print ("You tied %d times on Expert Mode! \n" % tieExp)
      print ("You have a %s win rate on Expert Mode!" % percentWon)
    elif (chosenMode == 4):
      superHard()
      percentWon = "{percent:.2%}".format(percent=(winHard/(winHard + loseHard +  tieHard)))
      print ("You won %d times on Super Hard Mode! \n" % winHard)
      print ("You lost %d times Super Hard Mode! \n" % loseHard)
      print ("You tied %d times Super Hard Mode! \n" % tieHard)
      print ("You have a %s win rate! Super Hard Mode" % percentWon)
    elif (chosenMode == 73):
      bigbang()
      print ("You won %d times!" % int(winspec))
      print ("You lost %d times!" % int(losespec))
      print ("You tied %d times!" % int(tiespec))
      percentWon = "{percent:.2%}".format(percent=(winspec / (winspec+losespec+tiespec)))
      print ("Your win percentage is %s from a total of %d games" % (percentWon,int(winspec+losespec+tiespec)))
    else:
      print ("I guess we will move on to whether or not ya wanna play again...\n")

    while(notyesorno):
      continueGame = input("Do you wanna play again? Type Yes or No \n")
      if (continueGame == "Yes"):
        print ("Coolio. \n")
        notyesorno = False
        playAgain = True
      elif (continueGame == "No"):
        print ("Aw that's too bad. :( \n")
        notyesorno = False
        playAgain = False
      else:
        print ("Nah... That's not an acceptable answer. Please type Yes or No")
        notyesorno = True

def continueGameCheck(ans):
  if (ans == "Yes"):
    return "Yes"
  elif (ans == "No"):
    return "No"
  else:
    return "Wrong input"

def checkStats(wlt,modeChosen):
  global winEas
  global loseEas
  global tieEas
  global winInt
  global loseInt
  global tieInt
  global winHard
  global loseHard
  global tieHard
  global winExp
  global loseExp
  global tieExp
  global winspec
  global losespec
  global tiespec

  if (modeChosen == 1):
    if (wlt == 0):
      winEas += 1
    elif (wlt == 1):
      loseEas += 1
    else:
      tieEas += 1
  elif (modeChosen == 2):
    if (wlt == 0):
      winInt += 1
    elif (wlt == 1):
      loseInt += 1
    else:
      tieInt += 1
  elif (modeChosen == 3):
    if (wlt == 0):
      winExp += 1
    elif (wlt == 1):
      loseExp += 1
    else:
      tieExp += 1
  elif (modeChosen == 4):
    if (wlt == 0):
      winHard += 1
    elif (wlt == 1):
      loseHard += 1
    else:
      tieHard += 1
  else:
    if (wlt == 0):
      winspec += 1
    elif (wlt == 1):
      losespec += 1
    else:
      tiespec += 1


main()
