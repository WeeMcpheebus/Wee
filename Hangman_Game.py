import random
from time import sleep as s
print("Let's play Hangman!")
s(1)
print("You have 1 more incorrect guesses than there are letters in the word")
s(2)
print("You may guess the whole word, but you will lose if you guess wrong")
s(2)
print("Here we go")
s(2)
repeat=""
fruits=[("apple",5),("apricot",8),("avocado",6),("banana",4),("blackcurrant",10),("blueberry",7),("carambola",8),("cherry",6),("coconut",6),("cranberry",8),
        ("feijoa",7),("fig",4),("gooseberry",8),("grapefruit",10),("grape",6),("melon",6),("kiwi",4),("lemon",6),("lime",5),("mandarin",7),("mango",6),
        ("nectarine",8),("orange",7),("papaya",4),("peach",6),("pear",5),("pineapple",7),("plum",5),("pomegranate",10),("pummelo",7),("raspberry",8),
        ("strawberry",9),("tangerine",8),("watermelon",10)] #always will be expanded, all themes
sports=[("soccer",6),("football",7),("baseball",6),("basketball",7),("tennis",6),("hockey",7)]
countries=[("Afghanistan",10),("Albania",7),("Algeria",8),("Andorra",7),("Angola",7),("Anguilla",8),("Antarctica",8),("Argentina",9),("Armenia",8),
           ("Aruba",6),("Australia",9),("Austria",8),("Azerbaijan",10),("Bahamas",6),("Bahrain",7),("Bangladesh",10),("Barbados",8),("Belarus",8),
           ("Belgium",8),("Belize",6),("Benin",5),("Bermuda",8),("Bhutan",7),("Bolivia",7),("Botswana",8),("Brazil",7),("Brunei",7),("Bulgaria",8),
           ("Burundi",7),("Cambodia",8),("Cameroon",8),("Canada",5),("Chad",5),("Chile",6),("China",6),("Columbia",9),("Comoros",6),("Congo",5),
           ("Croatia",7),("Cuba",5),("Cyprus",7),("Denmark",8),("Djibouti",8),("Dominica",8),("Ecuador",8),("Egypt",6),("Eritrea",7),("Estonia",8),
           ("Ethiopia",8),("Fiji",4),("Finland",7),("France",7),("Gabon",6),("Gambia",6),("Georgia",8),("Germany",8),("Ghana",5),("Gibraltar",8),
           ("Greece",5),("Greenland",8),("Grenada",7),("Guadeloupe",9),("Guatemala",8),("Guinea",7),("Guyana",6),("Haiti",5),("Vatican",7),("Honduras",9),
           ("Hungary",8),("Iceland",8),("India",6),("Indonesia",9),("Iran",5),("Iraq",5),("Ireland",8),("Israel",7),("Italy",6),("Jamaica",6),("Japan",5),
           ("Jordan",7),("Kazakstan",8),("Kenya",6),("Kiribati",7),("North Korea",10),("South Korea",11),("Kosovo",5),("Kuwait",7),("Kyrgyzstan",10),
           ("Latvia",6),("Lebanon",7),("Lesotho",7),("Liberia",7),("Liechtenstein",9),("Lithuania",8),("Luxembourg",10),("Macau",5),("Macedonia",9),
           ("Madagascar",8),("Malaysia",7),("Maldives",9),("Mali",5),("Malta",5),("Martinique",10),("Mauritania",8),("Mexico",7),("Micronesia",10),
           ("Moldova",7),("Monaco",6),("Mongolia",8),("Montenegro",8),("Morocco",5),("Mozambique",11),("Myanmar",7),("Namibia",6),("Nauru",5),("Nepal",6),
           ("Netherlands",11),("Nicaragua",8),("Niger",6),("Norway",7),("Oman",5),("Pakistan",8),("Panama",5),("Paraguay",7),("Peru",5),("Philippines",9),
           ("Poland",7),("Portugal",9),("Qatar",5),("Reunion",7),("Romania",7),("Russia",6),("Rwanda",6),("Samoa",5),("Senegal",7),("Serbia",7),
           ("Seychelles",8),("Singapore",10),("Slovakia",8),("Slovenia",9),("Somalia",7),("SAR",4),("Spain",6),("Sudan",6),("Suriname",9),("Swaziland",9),
           ("Sweden",6),("Switzerland",12),("Syria",6),("Taiwan",6),("Tajikistan",9),("Tanzania",6),("Thailand",8),("Togo",4),("Tokelau",8),("Tonga",6),
           ("Tunisia",7),("Turkey",7),("Turkmenistan",12),("Tuvalu",6),("Uganda",6),("Ukraine",8),("UAE",4),("UK",3),("USA",4),("Uruguay",7),
           ("Uzbekistan",11),("Vanuatu",6),("Venezuela",8),("Yemen",5),("Zambia",6),("Zimbabwe",8),]
themes=[fruits,sports,countries]
#final message setup
tick=0
cross=0
#game
while repeat=="":
    s(1)
    try:
        r=int(input("We have 3 themes to choose from: Type 0 to for fruits: Type 1 for sports: Type 2 for Countries:"))
        choice=themes[r]
    except IndexError:
        print("Whoops, Choose a number from 0 to 2.")
        repeat=''
        continue
    i=random.choice(choice)
    (word,turns)=i
    word=word.lower()
    s(1.5)
    print("The word is ready! You have",turns,"guesses... Good Luck")
    wrong=0
    guess=["-"]*len(word)
    letters="abcdefghijklmnopqrstuvwxyz"
    while wrong<=turns:
        curr=''
        print(wrong,"Guesses wrong so far",end='')
        let=input(":")
        let=let.lower()
        s(1)
        if len(let)>1:
            print("You decided to guess the whole word")
            s(1)
            if let==word:
                print("Congratulations!")
                break
            else:
                print("You guessed wrong...")
                break
        if let.isalpha()==False:
            print("Obviously, something is here.")
        elif len(let)==0:
            print("Please guess a letter")
        else:
            if (let in word) and (let in letters):
                print("Correct")
                letters=letters.replace(let,"")
                for count in range(len(word)):
                    if word[count]==let:
                        guess[count]=let
                s(1)
                print("The word is now", sep='')
            else:
                print("Wrong")
                wrong+=1
                print("Here's what you have so far:",end='')
            for l in guess:
                curr+=l
            print(curr)
            if curr==word:
                print("You've guessed it!")
                tick+=1
                cross-=1
                break
            else:
                s(1)
    cross+=1
    print("The word is:",word)
    print("Game Over")
    repeat=input("Hit ENTER to play again. Type anything to end game:")
print("Thank you for playing!")
s(1)
print("You guessed...", tick, " wrong")
print("You guessed...", cross, " right")