from os.path import sep

VERSION = "1.0"
PICDIR = "pics" + sep
PICSCOINS = "coins" + sep
ABOUTPROG = """<html><body>
TrueRand - True Random Generator Client<br>
Version: %s<br>
This is not commercial product
<hr>
Author: Bohdan Fedys (Ukraine)
<a href='https://www.odesk.com/users/~01ff73ae5e700d45ed'>View oDesk profile</a>
<hr>
Library: <a href='http://qt.digia.com/'>Qt (PyQt)</a>
<hr>
This client uses <a href='http://www.random.org/'>RANDOM.ORG</a> HTTP API - True Random Number Service
RANDOM.ORG offers true random numbers to anyone on the Internet. <br>
The randomness comes from atmospheric noise, <br>
which for many purposes is better than the pseudo-random number <br>
algorithms typically used in computer programs. 
</body></html>
""" % (VERSION)

PRESETS={
    "Integers":
    {
        "None": None,
        "Yes/No": (0,1),
        "4-side dice": (1,4),
        "6-side dice": (1,6),
        "8-side dice": (1,8),
        "10-side dice": (1,10),
        "12-side dice": (1,12),
        "20-side dice": (1,20)
    },
    "Lottery":
    {},
    "Sequences":
    {
        "0None": None,
        "1Deck with 52 playing cards": ['Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades', 'Eight of Clubs', 'Eight of Diamonds', 'Eight of Hearts', 'Eight of Spades', 'Five of Clubs', 'Five of Diamonds', 'Five of Hearts', 'Five of Spades', 'Four of Clubs', 'Four of Diamonds', 'Four of Hearts', 'Four of Spades', 'Jack of Clubs', 'Jack of Diamonds', 'Jack of Hearts', 'Jack of Spades', 'King of Clubs', 'King of Diamonds', 'King of Hearts', 'King of Spades', 'Nine of Clubs', 'Nine of Diamonds', 'Nine of Hearts', 'Nine of Spades', 'Queen of Clubs', 'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades', 'Seven of Clubs', 'Seven of Diamonds', 'Seven of Hearts', 'Seven of Spades', 'Six of Clubs', 'Six of Diamonds', 'Six of Hearts', 'Six of Spades', 'Ten of Clubs', 'Ten of Diamonds', 'Ten of Hearts', 'Ten of Spades', 'Three of Clubs', 'Three of Diamonds', 'Three of Hearts', 'Three of Spades', 'Two of Clubs', 'Two of Diamonds', 'Two of Hearts', 'Two of Spades'],
        "2Deck with 36 playing cards": ['Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts', 'Ace of Spades', 'Eight of Clubs', 'Eight of Diamonds', 'Eight of Hearts', 'Eight of Spades', 'Jack of Clubs', 'Jack of Diamonds', 'Jack of Hearts', 'Jack of Spades', 'King of Clubs', 'King of Diamonds', 'King of Hearts', 'King of Spades', 'Nine of Clubs', 'Nine of Diamonds', 'Nine of Hearts', 'Nine of Spades', 'Queen of Clubs', 'Queen of Diamonds', 'Queen of Hearts', 'Queen of Spades', 'Seven of Clubs', 'Seven of Diamonds', 'Seven of Hearts', 'Seven of Spades', 'Six of Clubs', 'Six of Diamonds', 'Six of Hearts', 'Six of Spades', 'Ten of Clubs', 'Ten of Diamonds', 'Ten of Hearts', 'Ten of Spades'],
        "3Some names": ["John", "Bob", "Jack", "Steven", "Peter", "Adam", "Christopher"]
    }
}
