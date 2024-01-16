# Three methods to change the case of a string: .lower() .upper() and .title()

# The .split() returns a list of strings. It takes in a delimiter, otherwise it returns comma separated words.
# If the split is performed on a single word, it will return a list of single characters.

# For this problem, we started with a comma separated string containing names, and we created a list of last names
authors = ("Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala "
           "Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni")

author_names = authors.split(',')
print(author_names)

split_names = []
for i in range(len(author_names)):
    author_names[i].split(" ")
    split_names.append(author_names[i].split(" "))

print(split_names)

author_last_names = []
for name in split_names:
    for i in name:
        if i == name[1]:
            author_last_names.append(name[1])

print(author_last_names)

# And here is a one-liner that achieves the same result as my code above^ (provided by GPT-4)
# Split the authors string into a list of names, then split each name and take the last part as the last name
author_last_names2 = [name.split()[-1] for name in authors.split(',')]
print(author_last_names2)

# Escape sequences:
smooth_chorus = \
"""And if you said, "This life ain't good enough.
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""
chorus_lines = smooth_chorus.split('\n')  # This \n will create a list containing each line of text as an index.
print(chorus_lines)

# .join() will connect multiple strings based on a delimiter. Syntax:
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
print(''.join(my_munequita))
# => 'MySpanishHarlemMonaLisa'
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)

# You can use any string to join a list into a single string, such as a comma or \n:
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# Here, every index is turned into a new line of a single paragraph.
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio',
                            'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
print(smooth_fifth_verse)

# There is a .strip() method for cleaning up data. It removes white spaces. If you pass an argument, it will only
# remove that argument but not the white space.
featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas

# .strip()
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
stripd = ""  # create a new string for the strip because you cannot alter an existing string
for strings in love_maybe_lines:
    stripd = strings.strip()
    love_maybe_lines_stripped.append(stripd)

print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# .replace() method syntax: string_name.replace(substring_being_replaced, new_substring)

# .find() method:
print('smooth'.find('t'))
# => '4'
# It returns the location of the first index that has the given character or word
god_wills_it_line_one = "The very earth will disown you"
print(god_wills_it_line_one.find("disown"))
disown_placement = 20

# .format() method: It is like concatenation, but it is more legible and reusable in functions
def favorite_song_statement(song, artist):
    return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."

# To further increase readability of your code, use keywords to be more explicit:
def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
# ^Also, because there are keywords present, the arguments can be passed in any order and still work.
# Example 2:
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")

# Here is another example if strings in for loops since I struggle with that so much:
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []
aStr = ""
for i in highlighted_poems_list:
    aStr = i.strip()
    highlighted_poems_stripped.append(aStr)

print(highlighted_poems_stripped)

highlighted_poems_details = []
anStr = ""
for i in highlighted_poems_stripped:
    anStr = i.split(":")
    highlighted_poems_details.append(anStr)

titles = []
poets = []
dates = []

print(highlighted_poems_details)
for i in highlighted_poems_details:
    titles.append(i[0])
    poets.append(i[1])
    dates.append(i[2])
# This loop was very tricky. I should study it.
for i in range(0, len(highlighted_poems_details)):
    for j in range(len(highlighted_poems_details[i])):  # This line in particular.
        print("The poem {} was published by {} in {}.".format(titles[j], poets[j], dates[j]))

# Final Data cleaning project in Codecademy:
daily_sales = \
    """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
    09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
    white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
    ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
    ;,;   $5.13   ;,; white   ;,; 09/15/17,
    Eduardo George   ;,;$20.39;,; white&yellow 
    ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
    purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
    purple&yellow ;,;09/15/17,   Shaun Brock;,; 
    $17.98;,;purple&yellow ;,; 09/15/17 , 
    Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
    Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
    Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
    09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
    white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
    ;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
    $8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
    09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
    green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
    ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
    Israel Cummings;,;   $11.86   ;,;black;,;  
    09/15/17,   June Doyle   ;,;   $22.29 ;,;  
    black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
    $8.35;,;   white&black&yellow   ;,;   09/15/17,   
    Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
    ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
    ;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
    ;,; 09/15/17   ,Hubert Miles;,;   $3.59   
    ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
    ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
    black   ;,;   09/15/17 , Audrey Ferguson ;,; 
    $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
    $17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
    Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
    09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
    yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
    yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
    ;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
    $14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
    ;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
    black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
    ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
    $8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
    ;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
    ,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
    09/15/17 , Melody Moran ;,;   $30.84   
    ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
    $12.31 ;,; green&yellow&black;,;   09/15/17 ,
    Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
    ,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
    09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
    white&yellow&black ;,;09/15/17   ,   Dale Brady   
    ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
    Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
    ,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
    09/15/17, Angelica Garza;,;$11.60;,;white&black   
    ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
    white&black&red ;,;09/15/17   ,   Rex Hudson   
    ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
    ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
    Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
    ;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
    green&purple&yellow ;,;09/15/17   ,Stanley Holland 
    ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
    Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
    ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
    red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
    green&red ;,;   09/15/17   ,Irving Patterson 
    ;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
    Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
    Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
    Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
    ,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
    Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
    , Beatrice Newman ;,;$22.45   ;,;white&purple&red 
    ;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
    red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
    black&red;,; 09/15/17,   Javier Bailey   ;,;   
    $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
    Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
    ,   Traci Craig ;,;$0.65;,; green&yellow;,; 
    09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
    green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
    ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
    ;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
    Leonard Guerrero ;,;   $1.86   ;,;yellow  
    ;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
    09/15/17   ,Donna Ball ;,; $28.10  ;,; 
    yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
    $9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
    $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
    ;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
    Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
    ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
    green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
    green&yellow;,;09/15/17,Malcolm Morales ;,;   
    $24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
    Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
    ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
    , Leticia Manning;,;$15.70 ;,; green&purple;,; 
    09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
    09/15/17,Lewis Glover;,;   $13.66   ;,;   
    green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
    ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
    ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

# ------------------------------------------------
# Start coding below!

daily_sales_replaced = daily_sales.replace(";,;", "@")

print(daily_sales_replaced)
print("\n")
daily_transactions = daily_sales_replaced.split(",")
print(daily_transactions)

daily_transactions_split = []

for i in range(0, len(daily_transactions)):
    daily_transactions_split.append(daily_transactions[i].split("@"))

print("\n")
print(daily_transactions_split)
# We now have a 2D list of strings. Each transaction is in its own list.

transactions_clean = []

for transaction in daily_transactions_split:
    transaction_clean = []  # A temporary list to hold the cleaned data for one transaction
    for data_point in transaction:
        transaction_clean.append(data_point.strip())  # Clean and append each piece of the transaction
    transactions_clean.append(transaction_clean)  # Add the cleaned transaction to the main list
# Sometimes you have to perform operations in both loops simultaneously like this
# Also, it is very helpful to use accurate placeholder index names instead of simply i and j
print("\n")
print(transactions_clean)

customers = []
sales = []
thread_sold = []

for transactions in transactions_clean:
    # A transaction is a list containing customer, sale, and thread
    # For each transaction list in the 2D list:
    customers.append(transactions[0])
    sales.append(transactions[1])
    thread_sold.append(transactions[2])

print("\n", customers)
print("\n", sales)
print("\n", thread_sold)

total_sales = 0

for price in sales:
    no_dollar = price.strip("$")
    float_num = float(no_dollar)
    total_sales += float_num
print(total_sales)

thread_sold_split = []
for thread_order in thread_sold:
    if "&" not in thread_order:
        thread_sold_split.append(thread_order)
    else:
        # split it and use another for loop
        # to iterate and append them to the list
        # split here first
        split_order = thread_order.split("&")
        for thr in split_order:
            thread_sold_split.append(thr)

print("\n", thread_sold_split)

def color_count(color):
    count = 0
    for t in thread_sold_split:
        if t == color:
            count += 1
    return count

print(color_count("white"))

colors = ["red", "yellow", "green", "white",
          "black", "blue", "purple"]

for col in colors:
    print("There were {} {} threads sold today.".format(color_count(col), col))
