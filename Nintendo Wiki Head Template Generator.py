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
type = input("Article type?")
quote = input("Quote?")
speaker = input("Speaker of Quote?")
stub = input("Stub? (If not, leave blank)")
article_class = input("Article class? (A-E, X)")

#Output
if which == "simple":
    
    #Output simple head template
    print("{{Head")
    if type != "":
        print("| type = " + type)
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
    if type != "":
        print("| type = " + type)
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
