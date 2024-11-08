"""
    Program to auto calculate gross margin
    Formula: COST_PRICE / ( 1 - MARGIN / 100 )
"""

from customtkinter import *

app = CTk()
app.minsize(320, 350)
app.maxsize(320, 350)
app.title("Gross Margin Calculator")


def enter_pressed(event):
    # Janky but does work, re-vist this at a later date
    calculate_gm()


def calculate_gm():

    try:
        cost_price = float(price_entry.get())
        margin = float(markup_entry.get())

    except ValueError:
        output_label.configure(
            app, text=f"Numbers Only", text_color="red", font=("Arial", 12, "bold")
        )
        price_entry.delete(0, END)
        markup_entry.delete(0, END)
        price_entry.focus_set()

    else:

        # Another fix that needs address in the future to be able to calculate over 100% gross margin
        if float(markup_entry.get()) > 99:
            output_label.configure(
                app,
                text=f"Please enter a markup value between 1-99",
                text_color="red",
                font=("Arial", 12, "bold"),
            )
        else:
            selling_price = cost_price / (1 - (margin / 100))

            # Used format as it's easier than importing another package to do it with floats
            # This just formats the string, good enough for who it's for.

            formatted_selling_price = f"£ {format(selling_price, '.2f')}"

            output_label.configure(
                app, text=formatted_selling_price, text_color="green"
            )

            price_entry.delete(0, END)
            markup_entry.delete(0, END)
            markup_entry.insert(END, 60)
            price_entry.focus_set()


# |-------------------------------- Gross Margin Calculator UI --------------------------------|


heading = CTkLabel(app, text="Gross Margin Calculator")
heading.configure(font=("Arial", 22, "bold"))
heading.pack(padx=20, pady=20, fill="x")


price_label = CTkLabel(app, text="Enter the cost price: ")
price_label.configure(font=("Arial", 12, "bold"))
price_label.pack(
    padx=20,
    pady=0,
    fill="y",
    anchor="w",
)
price_entry = CTkEntry(app, placeholder_text="00.00")
price_entry.pack(padx=20, pady=10, fill="x")

markup_label = CTkLabel(app, text="Enter the mark up amount: ")
markup_label.configure(font=("Arial", 12, "bold"))
markup_label.pack(padx=20, pady=0, fill="y", anchor="w")
markup_entry = CTkEntry(app)
markup_entry.insert(END, 60)
markup_entry.pack(padx=20, pady=10, fill="x")

output_label = CTkLabel(app, text="")
output_label.configure(font=("Arial", 22, "bold"))
output_label.pack(padx=20, pady=10)

calculate_btn = CTkButton(app, text="Calculate", command=calculate_gm)
calculate_btn.pack(padx=20, pady=0, fill="x")

footer_label = CTkLabel(app, text=f"Created by James Chance\nhttps://github.com/JDJC3D")
footer_label.configure(font=("Arial", 10, "italic"))
footer_label.pack(padx=20, pady=0, side="bottom")

# Add the enter button to calculate
app.bind("<Return>", enter_pressed)

app.mainloop()

# Program Icon from https://www.flaticon.com/free-icons/calculator
