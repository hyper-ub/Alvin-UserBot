""" Userbot module for having some fun with people. """

import os
import urllib
import requests
from re import sub
from cowpy import cow
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint

from userbot import bot, CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
METOOSTR = [
    "Me Too Thank You",
    "Haha Yeah, Me Too",
    "Same Haha",
    "Me Too Bitch",
    "Same Here",
    "Haha Yes",
    "Me too",
]

ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
    [
    " ̍",
    " ̎",
    " ̄",
    " ̅",
    " ̿",
    " ̑",
    " ̆",
    " ̐",
    " ͒",
    " ͗",
    " ͑",
    " ̇",
    " ̈",
    " ̊",
    " ͂",
    " ̓",
    " ̈́",
    " ͊",
    " ͋",
    " ͌",
    " ̃",
    " ̂",
    " ̌",
    " ͐",
    " ́",
    " ̋",
    " ̏",
    " ̽",
    " ̉",
    " ͣ",
    " ͤ",
    " ͥ",
    " ͦ",
    " ͧ",
    " ͨ",
    " ͩ",
    " ͪ",
    " ͫ",
    " ͬ",
    " ͭ",
    " ͮ",
    " ͯ",
    " ̾",
    " ͛",
    " ͆",
    " ̚",
],
    [
    " ̕",
    " ̛",
    " ̀",
    " ́",
    " ͘",
    " ̡",
    " ̢",
    " ̧",
    " ̨",
    " ̴",
    " ̵",
    " ̶",
    " ͜",
    " ͝",
    " ͞",
    " ͟",
    " ͠",
    " ͢",
    " ̸",
    " ̷",
    " ͡",
]]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
    "Don't drink and type.",
    "I think you should go home or better to a mental hospital.",
    "Command not found. Just like your brain.",
    "Are you aware that you are fooling yourself? It's not.",
    "You can type better than that.",
    "The 544 part 9 rule bot prevents me from retaliating for a fool like you.",
    "Sorry, we don't sell brains.",
    "Believe me you're not normal.",
    "I bet your brain feels like new, considering you've never used it.",
    "If I want to kill myself, I will increase your ego and jump to your IQ.",
    "Zombies eat brains... you are safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your IQ exceeds your age.",
    "I'm not saying you're stupid, I'm just saying that you're unlucky when it comes to thinking.",
    "What language do you speak? Because it sounds like bullshit.",
    "Ignorance is not a crime so you are free to go.",
    "You are proof that evolution CAN reverse.",
    "I was going to ask how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains are not everything. In your case they are nothing.",
    "Usually people live and learn. You just live.",
    "I don't know what made you so stupid, but it really worked.",
    "Keep talking, someday you'll say something smart! (Though I doubt it)"
    "Shock me, say something smart.",
    "Your IQ is lower than your shoe size.",
    "Ouch! Your neurotransmitter is no longer working.",
    "Are you crazy you stupid.",
    "Everyone has the right to be stupid but you abuse the privilege.",
    "Sorry I hurt your feelings when I called you stupid. I thought you knew that already.",
    "You should try the cyanide tasting.",
    "Your enzymes are meant to digest rat poison.",
    "You should try to sleep forever.",
    "Take a gun and shoot yourself.",
    "You can set a world record by jumping from a plane without a parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try taking a shower with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can hold it forever.",
    "Go Green! Stop breathing Oxygen.",
    "God is looking for you. You must go to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred storey building but you can only do it once.",
    "You should donate your brain seeing that you never use it.",
    "Volunteer for targets within shooting range.",
    "Shooting the head is fun. Get it yourself.",
    "You should try swimming with great white sharks.",
    "You have to paint yourself red and run a bull marathon.",
    "You can stay underwater for the rest of your life without ever having to come back.",
    "How about you stop breathing for 1 day? That would be great.",
    "Try provoking the tiger while you two are in a cage.",
    "Have you tried shooting yourself 100m high using a canon.",
    "You should try to hold the TNT in your mouth and ignite it.",
    "Try playing catch and throw with RDX it's fun.",
    "I heard that phogine is poisonous but I don't think you mind snorting it for fun.",
    "Launch yourself into space while forgetting about oxygen on Earth.",
    "You should try playing snakes and ladders, with real snakes and without ladders.",
    "Dancing naked on some HT cable.",
    "Active Volcano is the best swimming pool for you.",
    "You should try a hot bath in the volcano.",
    "Try to spend a day in the coffin and it will be yours forever.",
    "Hit Uranium with slow-moving neutrons in front of you. It will be a rewarding experience.",
    "You can be the first to step on the sun. Good luck.",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

IWIS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNS_STR = [
    "Run to Thanos..",
    "Running far, far from the earth..",
    "Outrun Bolt because I'm a bot user!!",
    "Running to Mia Khalifa..",
    "This group is too dangerous to handle, I have to run.",
    "`Running From The Man Who Smells Mustard `",
    "I'm so tired to run and chase you ",
    "I go first",
    "I just walked away, because I was too fat to run.",
    "I'm tired!",
    "Run Here Smell of Mustard ",
    "I ran because I was so fat.",
    "Run... \nbecause dieting is not an option.",
    "Running Fast From Mad Men",
    "If you want to catch me, you have to hurry... \nIf you want to live with me, you have to be a good person... \nBut if you want to get past me... \nYou must be joking.",
    "Anyone can run a hundred meters, that's the next forty-two thousand two hundred.",
    "Why are all these people following me?",
    "Are the kids still chasing me?",
    "Running as fast as Super Dede.. Is that polite?",
]

CHASE_STR = [
    "Where do you think you are going?",
    "Huh? What? Did they escape?",
    "ZZzzZZzz... Huh? What? Oh, it's just them again, forget it.",
    "Come back here!",
    "Not too fast...",
    "Watch out for the walls!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Just kidding, I'm everywhere",
    "You will regret that...",
    "You can also try /kickme, I heard it's fun.",
    "Disturb others, no one cares.",
    "You can run, but you can't hide."
    "Is that all you have?",
    "I'm behind you...",
    "You have friends!",
    "We can do this the easy way, or the hard way.",
    "You don't understand, do you?"
    "Yeah, you better run!",
    "Please remind me do I care?",
    "I would run faster if I were you.",
    "That must be the droids we were looking for.",
    "May opportunities always be in your favor.",
    "The famous last words.",
    "And they disappeared forever, never to be seen again.",
    "Oh look at me! I'm so cool, I can run from this guy's bot",
    "Yes yes, just tap /kickme.",
    "Here, take this ring and go to Mordor while you do.",
    "Legend says, they are still walking...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear causes anger. Anger leads to hatred. Hate causes suffering. If you keep running in fear, you may"
    "be the next Vader.",
    "A few calculations later, I've decided my interest in your crime is exactly 0.",
    "Legend says, they are still running.",
    "Go on, we're not sure we want you here.",
    "You're a wizard- Oh. Wait. You're not Harry, keep moving.",
    "DO NOT RUN HERE!",
    "Hasta la vista, dear.",
    "Who let the dog out?",
    "It's funny, because no one cares.",
    "Ah, what a shame, I like that one.",
    "Frankly, my dear, I don't care.",
    "My milkshakes take all the boys to the yard... So run faster!",
    "You can't HANDLE the truth!",
    "Once upon a time, in a galaxy far far away... Someone would have cared about it, But not anymore.",
    "Hey, look at them! They're running from the inevitable hammer... Sweet.",
    "Han shoots first, me too.",
    "What are you after, white rabbit?",
    "As The Doctor said... RUN!",
]

HELLOSTR = [
    "Hi!",
     "'Ello, bro!",
     "What is crackin?",
     "How are you?",
     "Hello, how are you, how are you!",
     "Hello, who's there, I'm talking.",
     "You know who this is.",
     "Yo!",
     "Wassup.",
     "Greetings and greetings!",
     "Hello, sunshine!",
     "Hey, how are you, hi!",
     "What's kicking, little chicken?",
     "Peek a boo!",
     "Hello-good!",
     "Hello, freshman!",
     "I came in peace!",
     "Oh, buddy!"
     "Hey!",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES_EN = [
    "{hits} {victim} with {item}.",
    "{hits} {victim} in the face with {item}.",
    "{hits} {victim} around a bit with {item}.",
    "{throws} {item} to {Victim}.",
    "takes {items} and {throws} into {victim}'s face.",
    "Stab {victim} with the spear of love.",
    "{throws} multiple {items} to {victim}.",
    "takes {items} and {throws} into {victim}'s face.",
    "launch {item} toward common {victim}.",
    "sitting on {victim}'s face while slamming {item}.",
    "started slapping {victim} silly with {item}.",
    "pin {victim} down and repeatedly {hits} them with {item}.",
    "takes {items} and {hits} {victim} with it.",
    "started slapping {victim} silly with {item}.",
    "holding {victim} and repeatedly {hits} them with {item}.",
    "hit {victim} with {item}.",
    "takes {items} and {hits} {victim} with it.",
    "tie {victim} to a chair and {throws} {items} on him.",
    "{hits} {victim} {where} with {item}.",
    "tie {victim} to a pole and whip them {where} with {item}."
    "provide friendly encouragement to help {victim} learn to swim in the lava.",
    "sending {victim} to /ocean/lava.",
    "sending {victim} to the memory hole.",
    "behead {victim}.",
    "throwing {victim} from a building.",
    "replacing all {victim} music with envious song says boss.",
    "spam email {victim}.",
    "makes {victim} depressed.",
    "slap {victim} for nothing.",
    "hit {victim} by garuda plane.",
    "hit {victim}'s head.",
    "put {victim} in the trash.",
    "Kicked {victim} and threw him in the river.",
    "put {victim} in the haunted house.",
    "slap {victim} with an iron rod!"]

ITEMS_EN = [
    "Gas cylinders",
     "42 In Television",
     "Racket",
     "Mosquito Racket",
     "Glass",
     "Book",
     "Ringgis",
     "Egg",
     "Needle",
     "Tube Monitor",
     "Screwdriver",
     "Aluminum",
     "Gold",
     "Printers",
     "Speaker",
     "LPG gas",
     "Gas tank",
     "Water reservoir",
     "Bowling Ball",
     "Laptops",
     "Damaged Hard Drive",
     "Hot Pan",
     "Coronavirus",
     "Office desk",
     "File Desk",
     "Cupboard",
     "Iron Bucket",
     "Steel bar",
     "Hot Tin",
     "Tiger",
     "Gravel Stone",
     "Stale Food",
     "AirBus Plane",
     "Nasa Rockets",
     "Nasa Satellite",
     "Sun",
     "Meteor",
     "Office Files",
     "hot concrete",
     "Mirror",
     "Jade",
     "Bottle",
     "Nezuko",
     "Tape Cassette",
     "Clothes Pole",
     "Folding knife",
     "Ice Bump",
     "Asteroids",
]

THROW_EN = [
    "throw",
     "throw",
]

HIT_EN = [
    "hit",
     "kick",
     "slap",
     "hit",
     "throw",
]

WHERE_EN = ["on the cheeks", "on the head", "on the buttocks", "on the body"]

SLAP_TEMPLATES_ID = [
    "{hits} {victim} with {item}.",
    "{throws} an {item} to {victim}.",
    "fetch {item} and {hits} {victim} .",
    "Take An {item} and {hits} {victim} With it.",
    "Dropping {victim} Into Lava.",
    "Sending {victim} to the Crater.",
    "Throwing {victim} Into the Sea.",
    "Removing {victim} From Earth.",
    "Throwing {victim} Into space.",
    "Putting {victim} on Pluto.",
    "Throws an {item} at {victim}.",
    "Throws {item} to {victim}.",
    "Slap {victim} using {item}.",
    "Throw {victim} into the air.",
    "Removing {victim} From Friends List.",
    "Throws {item} {where} {victim}.",
    "Put {item} {where} {victim}.",
    "Attacking {victim} using {anime}.",
    "Hack Entire account {victim}"
]

ITEMS_ID = [
    "Gas cylinders",
     "42 In Television",
     "Racket",
     "Mosquito Racket",
     "Glass",
     "Book",
     "Ringgis",
     "Egg",
     "Needle",
     "Tube Monitor",
     "Screwdriver",
     "Aluminum",
     "Gold",
     "Printers",
     "Speaker",
     "LPG gas",
     "Gas tank",
     "Water reservoir",
     "Bowling Ball",
     "Laptops",
     "Damaged Hard Drive",
     "Hot Pan",
     "Coronavirus",
     "Office desk",
     "File Desk",
     "Cupboard",
     "Iron Bucket",
     "Steel bar",
     "Hot Tin",
     "Tiger",
     "Gravel Stone",
     "Stale Food",
     "AirBus Plane",
     "Nasa Rockets",
     "Nasa Satellite",
     "Sun",
     "Meteor",
     "Office Files",
     "hot concrete",
     "Mirror",
     "Jade",
     "Bottle",
     "Nezuko",
     "Tape Cassette",
     "Clothes Pole",
     "Folding knife",
     "Ice Bump",
     "Asteroids",
]

THROW_ID = [
    "Throw",
     "Throw"
]

HIT_ID = [
    "Hit",
     "throw",
     "beating",
]
WHERE_ID = ["on the cheeks", "on the head", "on the buttocks", "on the body"]


SLAP_TEMPLATES_Jutsu = [
    "Attacking {victim} Using {hits}.",
     "Attacking {victim} Using {item}.",
     "Throws {throws} at {victim} .",
     "Throws {throws} {where} {victim}."
]
ITEMS_Jutsu = [
    "KAA MEE HAA MEE HAA",
    "Chibaku Tensei",
]

THROW_Jutsu = [
    "Futon Rasen Shuriken",
    "Shuriken",
]

HIT_Jutsu = [
    "Rasengan",
    "Chidori",
]

GAMBAR_TITIT = """
😋😋
😋😋😋
  😋😋😋
    😋😋😋
     😋😋😋
       😋😋😋
        😋😋😋
         😋😋😋
          😋😋😋
          😋😋😋
      😋😋😋😋
 😋😋😋😋😋😋
 😋😋😋  😋😋😋
    😋😋       😋😋
"""

GAMBAR_OK = """
░▐▀▀▀▀▀▀▀▀▌▐▀▌▄▄▄▀▀▓▀
░▐▌▓▀▀▀▀▓▌▌▐▐▌▀▌▄▄▀░░
░▐▐▌▐▀▀▌▐▐▌▐▌▐▓▄▀░░░░
░▐▌▌▐▄▄▌▐▌▌▐▐▌▓▀▄░░░░
░▐▐▓▄▄▄▄▓▐▌▐▌▌▄▌▀▀▄░░
░▐▄▄▄▄▄▄▄▄▌▐▄▌▀▀▀▄▄▓▄
"""


GAMBAR_TENGKORAK = """
░░░░░░░░░░░░░▄▐░░░░
░░░░░░░▄▄▄░░▄██▄░░░
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█▄░░░░
░░░░░░░▐▌▀▄▀▄▀▐░░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░
"""

GAMBAR_KONTL = """
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠁⠉⠉⠉
"""


WHERE_Jutsu = ["On the Cheeks", "On the Head", "On the Buttocks", "On the Body, On the Ass"]

normiefont = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z']

weebyfont = [
    '卂',
    '乃',
    '匚',
    '刀',
    '乇',
    '下',
    '厶',
    '卄',
    '工',
    '丁',
    '长',
    '乚',
    '从',
    '𠘨',
    '口',
    '尸',
    '㔿',
    '尺',
    '丂',
    '丅',
    '凵',
    'リ',
    '山',
    '乂',
    '丫',
    '乙']

# ===========================================


@register(outgoing=True, pattern=r"^\;(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern=r"^\;coinflip (.*)")
async def coin(event):
    r = choice(["head", "tail"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "head":
        if input_str == "head":
            await event.edit(
                "The Coin Landed On: **Head**.\nYou're Right.")
        elif input_str == "tail":
            await event.edit(
                "The Coin Landed On: **Head**.\nYou're Wrong, Try Again..."
            )
        else:
            await event.edit("The Coin Landed On: **Head**.")
    elif r == "tail":
        if input_str == "tail":
            await event.edit(
                "The Coin Landed On: **Tail**.\nYou're Right.")
        elif input_str == "Kepala":
            await event.edit(
                "The Coin Landed On: **Tail**.\nYou're Wrong, Try Again..."
            )
        else:
            await event.edit("The Coin Landed On: **Tail**.")


@register(pattern=r"^\;slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ slaps a user, or get slapped if not a reply. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "_Can't slap this guy, need to pick up some meteors and rocks!_"
        )


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    slap_str = event.pattern_match.group(1)
    if slap_str == "en":
        temp = choice(SLAP_TEMPLATES_EN)
        item = choice(ITEMS_EN)
        hit = choice(HIT_EN)
        throw = choice(THROW_EN)
        where = choice(WHERE_EN)
    elif slap_str == "id":
        temp = choice(SLAP_TEMPLATES_ID)
        item = choice(ITEMS_ID)
        hit = choice(HIT_ID)
        throw = choice(THROW_ID)
        where = choice(WHERE_ID)
    elif slap_str == "jutsu":
        temp = choice(SLAP_TEMPLATES_Jutsu)
        item = choice(ITEMS_Jutsu)
        hit = choice(HIT_Jutsu)
        throw = choice(THROW_Jutsu)
        where = choice(WHERE_Jutsu)
    else:
        temp = choice(SLAP_TEMPLATES_EN)
        item = choice(ITEMS_EN)
        hit = choice(HIT_EN)
        throw = choice(THROW_EN)
        where = choice(WHERE_EN)

    caption = "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where)

    return caption


@register(outgoing=True, pattern=r"^\;boobs(?: |$)(.*)")
async def boobs(e):
    await e.edit("_Sinned, Getting Boobs Pictures..._")
    await sleep(3)
    await e.edit("_Sending Boobs Pictures..._")
    nsfw = requests.get(
        'http://api.oboobs.ru/noise/1').json()[0]["Boobs Pictures"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'boobs.jpg')
    await e.client.send_file(e.chat_id, "boobs.jpg")
    os.remove("boobs.jpg")
    await e.delete()


@register(outgoing=True, pattern=r"^\;ass(?: |$)(.*)")
async def butts(e):
    await e.edit("_Sin, Get Beautiful Ass Pictures..._")
    await sleep(3)
    await e.edit("_Sending Beautiful Ass Pictures..._")
    nsfw = requests.get(
        'http://api.obutts.ru/noise/1').json()[0]["ass pictures"]
    urllib.request.urlretrieve(
        "http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'butts.jpg')
    await e.client.send_file(e.chat_id, "butts.jpg")
    os.remove("butts.jpg")
    await e.delete()


@register(outgoing=True, pattern=r"^\;(yess|noo|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(event.chat_id,
                                    str(r["answer"]).upper(),
                                    reply_to=message_id,
                                    file=r["image"])


@register(outgoing=True, pattern=r"^\;fp$")
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern=r"^\;cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(choice(CRI))


@register(outgoing=True, pattern=r"^\;insult$")
async def insult(e):
    """ I make you cry !! """
    await e.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern=r"^\;cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await cp_e.edit("`😂🅱️AhHH👐good👅Bro👅for✌️make👌me👐like👀funny💞HaHAhaA!💦`")

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern=r"^\;vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await vpr.edit("_G I V E S O M E T E X T F O R V A P O R！_")

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\;str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await stret.edit("_Giveeeeee someeeeee teeeeeeext!_")

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern=r"^\;zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await zgfy.edit(
            "`b̜́ͨe͒͜r̠͂ͬi̷̱̋k͖͒ͤa̋ͫ͑n͕͂͗ t̢͘͟e͂̽̈́k͎͂͠s̤͚ͭ m̪͔͑è͜͡n͈ͮḁ͞ͅk̲̮͛u̺͂ͩt̬̗́k͍̙̮á ̺n̨̹ͪ`"
        )

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            rand = randint(0, 2)

            if rand == 0:
                charac = charac.strip() + \
                    choice(ZALG_LIST[0]).strip()
            elif rand == 1:
                charac = charac.strip() + \
                    choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + \
                    choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\;hi$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern=r"^\;owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await owo.edit("_please give some UwU Text!_")

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern=r"^\;react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=r"^\;shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern=r"^\;chase$")
async def police(chase):
    """ Run bro run, I will catch you soon !! """
    await chase.edit(choice(CHASE_STR))


@register(outgoing=True, pattern=r"^\;run$")
async def runner_lol(run):
    """ run, run, RUUUN! """
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern=r"^\;metoo$")
async def metoo(hahayes):
    """ Haha yes """
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern=r"^\;oem$")
async def oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\;Oem$")
async def Oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\;10iq$")
async def iqless(e):
    await e.edit("♿")


@register(outgoing=True, pattern="^;fuck$")
async def iqless(e):
    await e.edit("🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕")


@register(outgoing=True, pattern=r"^\;moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\;bunga$")
async def moon(event):
    deq = deque(list("🌼🌻🌺🌹🌸🌷"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\;waktu$")
async def moon(event):
    deq = deque(list("🎑🌄🌅🌇🌆🌃🌌"))
    try:
        for x in range(100):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\;buah$")
async def moon(event):
    deq = deque(list("🍉🍓🍇🍎🍍🍐🍌"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\;clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;rain$")
async def rain(event):
    deq = deque(list("☀️🌤⛅️🌥☁️🌧⛈"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;love$")
async def love(event):
    deq = deque(list("❤️🧡💛💚💙💜🖤💕💞💓💗💖💘💝"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;earth$")
async def earth(event):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;hati$")
async def earth(event):
    deq = deque(list("🖤💜💙💚💛🧡❤️🤍"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;monyet$")
async def earth(event):
    deq = deque(list("🙈🙉🙈🙉🙈🙉🙈🙉"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^;emo$")
async def earth(event):
    deq = deque(list("🙂😁😄😃😂🤣😭🐵🙊🙉🙈"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\;mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await mock.edit("_gIve MesSagE For MoCk!_")

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\;weeb(?: |$)(.*)")
async def weebify(e):
    args = e.pattern_match.group(1)
    if not args:
        get = await e.get_reply_message()
        args = get.text
    if not args:
        await e.edit("what are you doing master")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await e.edit(string)


@register(outgoing=True, pattern=r"^\;clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await memereview.edit("master,Please Reply To The Message Of The Person You Want To Compliment ツ")
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=r"^\;bluetext$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/BLUE TEXT /WHAT ARE /YOU.\n"
            "/ARE /DOESN'T /BECAUSE / INTERESTED / SEE / TEXT / BLUE / SURE / YOU / BORED?")


@register(outgoing=True, pattern=r"^\;f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)


@register(outgoing=True, pattern=r"^\;lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit("Ini Dia, Bantu Dirimu Sendiri."
                        f"\n[{query}]({r.json()['shorturl']})")


@register(outgoing=True, pattern=r"^\;sayhi$")
async def sayhi(e):
    await e.edit(
        "\n💰💰💰💰💰💰💰💰💰💰💰💰"
        "\n💰🔷💰💰💰🔷💰💰🔷🔷🔷💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷🔷🔷🔷🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰💰🔷💰💰"
        "\n💰🔷💰💰💰🔷💰💰🔷🔷🔷💰"
        "\n💰💰💰💰💰💰💰💰💰💰💰💰")


@register(pattern=r";scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Tidak Valid`")
        return
    try:
        if (scam_time > 300):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r";type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await typew.edit("_Give some text for type_")
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


@register(outgoing=True, pattern=r"^\;leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("*bye everyone, master leave this group ツ*")


@register(outgoing=True, pattern=r"^\;fail$")
async def fail(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `"
                     "`\n████▌▄▌▄▐▐▌█████ `"
                     "`\n████▌▄▌▄▐▐▌▀████ `"
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")


@register(outgoing=True, pattern=r"^\;lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `")


@register(outgoing=True, pattern=r"^\;rock$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮┈┈┈┈┈┈┈┈┈┈┈┈ `"
                     "`\n┈┃┃┈╭╮┈┏╮╭╮╭╮┃╭ `"
                     "`\n┈┃┃┈┃┃┈┣┫┃┃┃┈┣┫ `"
                     "`\n┈┃┣┳┫┃┈┃╰╰╯╰╯┃╰ `"
                     "`\n╭┻┻┻┫┃┈┈╭╮┃┃━┳━ `"
                     "`\n┃╱╭━╯┃┈┈┃┃┃┃┈┃┈ `"
                     "`\n╰╮╱╱╱┃┈┈╰╯╰╯┈┃┈ `")


@register(outgoing=True, pattern=r"^\;lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")


@register(outgoing=True, pattern=r"^\;stfu$")
async def stfu(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n██████████████████████████████`"
                     "`\n██▀▀▀▀████▀▀▀▀████▀▀▀▀▀███▀▀██▀▀█`"
                     "`\n█──────██──────██───────██──██──█`"
                     "`\n█──██▄▄████──████──███▄▄██──██──█`"
                     "`\n█▄────▀████──████────█████──██──█`"
                     "`\n█▀▀██──████──████──███████──██──█`"
                     "`\n█──────████──████──███████──────█`"
                     "`\n██▄▄▄▄█████▄▄████▄▄████████▄▄▄▄██`"
                     "`\n█████████████████████████████████`")


@register(outgoing=True, pattern=r"^\;gtfo$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n███████████████████████████████ `"
                     "`\n█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█ `"
                     "`\n█───────█──────█───────█──────█ `"
                     "`\n█──███──███──███──███▄▄█──██──█ `"
                     "`\n█──███▄▄███──███─────███──██──█ `"
                     "`\n█──██───███──███──██████──██──█ `"
                     "`\n█──▀▀▀──███──███──██████──────█ `"
                     "`\n█▄▄▄▄▄▄▄███▄▄███▄▄██████▄▄▄▄▄▄█ `"
                     "`\n███████████████████████████████ `")


@register(outgoing=True, pattern=r"^\;nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *this for you*"
                     "\n                    \n"
                     r"`(\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *just kidding*")


@register(outgoing=True, pattern=r"^\;fag$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`"
                     "`\n█▄█████▄█`"
                     "`\n█▼▼▼▼▼`"
                     "`\n█       STFU FAGGOT'S`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                     "`\n ██   ██`")


@register(outgoing=True, pattern=r"^\;tai$")
async def taco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\\__/}"
                     "\n(●_●)"
                     "\n( >💩 Mau Tai Ku?")


@register(outgoing=True, pattern=r"^\;paw$")
async def paw(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern=r"^\.tf$")
async def tf(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@register(outgoing=True, pattern=r"^\;gey$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈Lu Bau Hehe`"
                     "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


@register(outgoing=True, pattern=r"^\;gay$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈ANDA GAY`"
                     "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


@register(outgoing=True, pattern=r"^\;bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@register(outgoing=True, pattern=r"^\;hey$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@register(outgoing=True, pattern=r"^\;nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
                     "`\n┗━━┻━┛`")


@register(outgoing=True, pattern=r"^\;iwi(?: |$)(.*)")
async def faces(siwis):
    """ IwI """
    textx = await siwis.get_reply_message()
    message = siwis.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await siwis.edit("you most give text for iwi")
        return

    reply_text = sub(r"(a|i|u|e|o)", "i", message)
    reply_text = sub(r"(A|I|U|E|O)", "I", reply_text)
    reply_text = sub(r"\!+", " " + choice(IWIS), reply_text)
    reply_text += " " + choice(IWIS)
    await siwis.edit(reply_text)


@register(outgoing=True, pattern="^;koc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8===✊D💦")
        await e.edit("8==✊=D💦💦")
        await e.edit("8=✊==D💦💦💦")
        await e.edit("8✊===D💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦")
        await e.edit("8=✊==D💦💦💦💦💦💦💦")
        await e.edit("8✊===D💦💦💦💦💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
        await e.edit("8=✊==D Lah Kok Habis?")
        await e.edit("😭😭😭😭")


@register(outgoing=True, pattern="^;gas$")
async def gas(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("___________________🚑")
        await e.edit("________________🚑___")
        await e.edit("______________🚑_____")
        await e.edit("___________🚑________")
        await e.edit("________🚑___________")
        await e.edit("_____🚑______________")
        await e.edit("__🚑_________________")
        await e.edit("🚑___________________")
        await e.edit("_____________________")
        await e.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=r"^\;shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern=r"^\;(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('😋', emoji)
    await e.edit(titid)


@register(outgoing=True, pattern=r"^\;(?:kon|kontl)\s?(.)?")
async def emoji_kontl(e):
    emoji = e.pattern_match.group(1)
    kontl = GAMBAR_KONTL
    if emoji:
        kontl = kontl.replace('😂', emoji)
    await e.edit(kontl)


@register(outgoing=True, pattern=r"^\;oks$")
async def emoji_oke(e):
    emoji = e.pattern_match.group(1)
    oke = GAMBAR_OK
    if emoji:
        oke = oke.replace('😂', emoji)
    await e.edit(oke)


@register(outgoing=True, pattern=r"^\.skull$")
async def emoji_tengkorak(e):
    emoji = e.pattern_match.group(1)
    tengkorak = GAMBAR_TENGKORAK
    if emoji:
        tengkorak = tengkorak.replace('😂', emoji)
    await e.edit(tengkorak)


CMD_HELP.update({
    "memes":
    ">;cowsay"
    "\nUsage: the cow that said something."
    "\n\n> .cp"
    "\nUsage: Copy paste famous memes"
    "\n\n>;vapor"
    "\nUsage: Evaporate everything!"
    "\n\n>;str"
    "\nUsage: Stretch."
    "\n\n>;10iq"
    "\nUsage: You retreat!!"
    "\n\n>;zal"
    "\nUsage: Gives off a feeling of chaos."
    "\n\n>;Oem"
    "\nUsage: Oeeeem"
    "\n\n>;fp"
    "\nUsage: Palm :P"
    "\n\n>;moon"
    "\nUsage: moon animation."
    "\n\n>;clock"
    "\nUsage: clock animation."
    "\n\n>;hi"
    "\nUsage: Say hello to everyone!"
    "\n\n>;coinflip <Head/Tail>"
    "\nUsage: Tossing a coin!!"
    "\n\n>;owo"
    "\nUsage: UwU"
    "\n\n>;react"
    "\nUsage: Make your Userbot react to everything."
    "\n\n>;slap"
    "\nUsage: slap them back with a random object!!"
    "\n\n>;cry"
    "\nUsage: if you do this, I will cry."
    "\n\n>;shg"
    "\nUsage: Shrug!"
    "\n\n>;run"
    "\nUsage: Let Me Run, Run, RUN!"
    "\n\n>;chase"
    "\nUsage: You'd better start running"
    "\n\n>;metoo"
    "\nUsage: Haha yeah"
    "\n\n>;mock"
    "\nUsage: Go ahead and find real fun."
    "\n\n>;clap"
    "\nUsage: Praise people!"
    "\n\n>;f <emoji/character>"
    "\nUsage: F."
    "\n\n>;bt"
    "\nUsage: Trust me, you will find this useful."
    "\n\n>;weeb"
    "\nUsage: To Convert Text To Weeb-ify."
    "\n\n>;type <text>"
    "\nUsage: Just a small command to turn your keyboard into a typewriter!"
    "\n\n>;lfy <query>"
    "\nUsage: Let me Google it for you quickly!"
    "\n\n>;decide [Alternative: (.yes, .no, .maybe)]"
    "\nUsage: Make a quick decision."
    "\n\n> ;nou ;bot ;rock ;gey ;tf ;paw ;tai ;nih"
    "\n> ;fag ;gtfo ;stfu ;lol ;lool ;fail ;leave"
    "\n> ;iwi ;sayhi ;koc ;gas ;earth ;love ;rain"
    "\n> ;penis ;emo ;fuck ;skull  ;monyet\nUsage: try it"
    "\n\n\n**Have a nice day**\n➥ `Alvin`"
})
