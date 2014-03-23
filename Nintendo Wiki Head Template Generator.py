"""

Nintendo Wiki Head Template Generator

Purpose: Generates code for head templates for Nintendo Wiki articles
Programer: ExcaliburZero / Rocketslime_1_1

"""
##Check if a basic or complex head template is wanted
which = input("Would you like a simple or complex head template?")
which = which.lower()

print("If one or more of the following categories do not apply to the article, or if the answer to them is no, then simply press enter to skip them.")

#Simple Inputs
article_type = input("Article type?")

#Check article type
if not (article_type == "" or article_type == "Character" or article_type == "Location" or article_type == "Item" or article_type == "Person" or article_type == "System" or article_type == "Accessory" or article_type == "Game" or article_type == "Species" or article_type == "Organization" or article_type == "Company" or article_type == "Product" or article_type == "Soundtrack" or article_type == "Fan Website" or article_type == "Attack" or article_type == "Group" or article_type == "Event" or article_type == "Year" or article_type == "Terminology" or article_type == "Magazine" or article_type == "Class" or article_type == "Series" or article_type == "Chapter" or article_type == "Ability" or article_type == "Other"):
    print ("Incorrect article type! A list of the correct article types can be found at http://nintendo.wikia.com/wiki/Template:Head#Types \n Remeber that you must input it with correct spelling and the first letter of each word capitalized.")
    article_type = input("Article type?")
    
quote = input("Quote?")
speaker = input("Speaker of Quote?")
stub = input("Stub? (If not, leave blank)")
article_class = input("Article class? (A-E, X)")

#Check article class
if not (article_type == "" or article_type == "A" or article_type == "B" or article_type == "C" or article_type == "D" or article_type == "E" or article_type == "X" or article_type == "?"):
    print ("Incorrect article class! A list of the correct article classes can be found at http://nintendo.wikia.com/wiki/Nintendo_Wiki:Page_Classification \n Remeber that you must input it as a capital letter.")
    article_class = input("Article class? (A-E, X)")

#Output
if which == "simple":
    
    #Output simple head template
    print("{{Head")
    if article_type != "":
        print("| type = " + article_type)
    if quote != "":
        print("| quote = " + quote)
    if speaker != "":
        print("| speaker = " + speaker)
    if stub != "":
        print("| stub = x")
    if article_class != "":
        print("| class = " + article_class)
    print("}}")
    
elif which == "complex":

    #Complex template variables
    featured = input("Is this a featured article?")
    protected = input("Is this article protected?")
    unreleased = input("Is this article about an unreleased game?")
    hfor = input("Does this article require a for section?")
    if hfor != "":
        for1 = input("for1?")
        for2 = input("for2")
        for3 = input("for3?")
    
    #Output complex head template
    print("{{Head")
    if article_type != "":
        print("| type = " + article_type)
    if quote != "":
        print("| quote = " + quote)
    if speaker != "":
        print("| speaker = " + speaker)
    if stub != "":
        print("| stub = x")
        
    if featured != "":
        print("| featured = x")
    if protected != "":
        print("| protected = x")
    if article_class != "":
        print("| class = " + article_class)
    if unreleased != "":
        print("| unreleased = x")
    if hfor != "":
        print("| for = x")
    if for1 != "":
        print("| for1 = " + for1)
    if for2 != "":
        print("| for2 = " + for2)
    if for3 != "":
        print("| for3 = " + for3)    
    print("}}")
    
else:
    print("Invalid template version input, you must either input either simple or complex.")
