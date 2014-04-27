"""

Nintendo Wiki Head Template Generator

Purpose: Generates code for head templates for Nintendo Wiki articles
Programer: ExcaliburZero / Rocketslime_1_1

"""

#Imports
from tkinter import *

#Generate Head Template Function
def generate_head():

    #Grab SIMPLE variables
    narticle_type = article_type.get()
    nquote = quote.get()
    nspeaker = speaker.get()
    nstub = stub.get()
    narticle_class = article_class.get()

    #Grab COMPLEX variables
    nfeatured = featured.get()
    nprotected = protected.get()
    nunreleased = unreleased.get()
    nfor1 = for1.get()
    nfor2 = for2.get()
    nfor3 = for3.get()

    #Put together output
    output = "{|"
    if not narticle_type == "":
        output = output + "\n| type = " + narticle_type
    if not nquote == "":
        output = output + "\n| quote = \"" + nquote + "\""
    if not nspeaker == "":
        output = output + "\n| speaker = " + nspeaker
    if not nstub == "":
        output = output + "\n| stub = " + "x"
    if not narticle_class == "":
        output = output + "\n| class = " + narticle_class
    if not nfeatured == "":
        output = output + "\n| featured = x"
    if not nprotected == "":
        output = output + "\n| protected = x"
    if not nunreleased == "":
        output = output + "\n| unreleased = x"
    if not nfor1 == "":
        output = output + "\n| for = x"
        output = output + "\n| for1 = " + nfor1
    if not nfor2 == "":
        output = output + "\n| for2 = " + nfor2
    if not nfor3 == "":
        output = output + "\n| for3 = " + nfor3
    output = output + "\n|}"

    #Output template code
    output_template = Text(theGUI, height = 16, width = 23)
    output_template.grid(row = 14, column = 1)
    output_template.insert(END, output)
    #output_template.config(state = DISABLED)
    #output_template = Label(theGUI, text = output).grid(row = 7, column = 1)

    return

#Generate GUI
theGUI = Tk()
theGUI.geometry("400x550+100+200")
theGUI.title("Head Template Generator")

#Setup SIMPLE variables
article_type = StringVar()
quote = StringVar()
speaker = StringVar()
stub = StringVar()
article_class = StringVar()

#Setup SIMPLE labels
label_intro = Label(theGUI, text="Welcome to the Head Template Generator").grid(row = 0, columnspan = 2)
label_article_type = Label(theGUI, text="type").grid(row = 1, column = 0)
label_quote = Label(theGUI, text="quote").grid(row = 2, column = 0)
label_speaker = Label(theGUI, text="speaker").grid(row = 3, column = 0)
label_stub = Label(theGUI, text="stub").grid(row = 4, column = 0)
label_article_class = Label(theGUI, text="class").grid(row = 5, column = 0)

#Setup SIMPLE entry boxes
article_type = Entry(theGUI, textvariable = article_type)
article_type.grid(row = 1, column = 1)
quote = Entry(theGUI, textvariable = quote)
quote.grid(row = 2, column = 1)
speaker = Entry(theGUI, textvariable = speaker)
speaker.grid(row = 3, column = 1)
stub = Entry(theGUI, textvariable = stub)
stub.grid(row = 4, column = 1)
article_class = Entry(theGUI, textvariable = article_class)
article_class.grid(row = 5, column = 1)

#Setup COMPLEX variables
featured = StringVar()
protected = StringVar()
unreleased = StringVar()
for1 = StringVar()
for2 = StringVar()
for3 = StringVar()

#Setup COMPLEX labels
label_blank = Label(theGUI, text="").grid(row = 6, column = 0)
label_featured = Label(theGUI, text="featured").grid(row = 7, column = 0)
label_protected = Label(theGUI, text="protected").grid(row = 8, column = 0)
label_unreleased = Label(theGUI, text="unreleased").grid(row = 9, column = 0)
label_for1 = Label(theGUI, text="for1").grid(row = 10, column = 0)
label_for2 = Label(theGUI, text="for2").grid(row = 11, column = 0)
label_for3 = Label(theGUI, text="for3").grid(row = 12, column = 0)

#Setup COMPLEX entry boxes
featured = Entry(theGUI, textvariable = featured)
featured.grid(row = 7, column = 1)
protected = Entry(theGUI, textvariable = protected)
protected.grid(row = 8, column = 1)
unreleased = Entry(theGUI, textvariable = unreleased)
unreleased.grid(row = 9, column = 1)
for1 = Entry(theGUI, textvariable = for1)
for1.grid(row = 10, column = 1)
for2 = Entry(theGUI, textvariable = for2)
for2.grid(row = 11, column = 1)
for3 = Entry(theGUI, textvariable = for3)
for3.grid(row = 12, column = 1)

#Setup button
button_generate = Button(theGUI, text = "Generate", command = generate_head).grid(row = 13, column = 1)

#Add GUI to main loop
theGUI.mainloop()
