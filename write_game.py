import sys
sys.stdout.reconfigure(encoding='utf-8')
content = open(r"C:\Users\30539\Documents\keji\parkour-game-new.html", "r", encoding="utf-8").read()
print("OK: " + str(len(content)) + " chars")