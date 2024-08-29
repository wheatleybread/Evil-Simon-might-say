from main import Homer

bart = Homer()
bart.level = 3
bart.list = 0
bart.gamelist = [1,2,3,4]
bart.playerturn = False
bart.playerlist = []
bart.length = 0


print ("Testing PlayNote")
bart.PlayNote("E5", 0.27)


print ("Testing SequencDisplay")
bart.sequencedisplay()

print ("Testing PlayerTimer")
bart.playertime()

print(' Testing game')

bart.game()