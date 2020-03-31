import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE IF NOT EXISTS GAME
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         PLAYERWEAPON           TEXT    NOT NULL,
         AIWEAPON            TEXT     NOT NULL,
         OUTCOME         TEXT    NOT NULL);''')

def insertOutcome(playerWeapon, aiWeapon, outcome):
    conn.execute("INSERT INTO Game (PLAYERWEAPON, AIWEAPON, OUTCOME) VALUES (?,?,?)", [playerWeapon, aiWeapon, outcome])
    conn.commit()

def onQuit():
    conn.close()

def getMostUsedWeapon():
    cursor = conn.execute("""select playerweapon, COUNT(playerweapon) as winnerweapon from game
        group by playerweapon
        order by winnerweapon DESC
        limit 1""")
    for weapon in cursor:
        print(weapon[0])
        enemyWeapon = weapon[0]
    if enemyWeapon == "rock":
        return "paper"
    elif enemyWeapon == "paper":
        return "scissors"
    else:
        return "rock"