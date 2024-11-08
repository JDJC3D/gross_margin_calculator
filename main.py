from customtkinter import *

"""
    Program to auto calculate gross margin 
    
    Formula: COST_PRICE / ( 1 - MARGIN / 100 )
"""

app = CTk()
app.geometry("320x340")
app.title("Gross Margin Calculator")




def calculate_gm():
    try:
        cost_price = float(price_entry.get())
        margin = float(markup_entry.get())
    except ValueError:
        output_label.configure(app, text=f"Please only use numbers", text_color="red")
    else:
        selling_price = cost_price / (1 - ( margin / 100) )

        # Used format as its easier than importing another package to do it with floats
        # This just formats the string, good enough for who its for.

        formatted_selling_price = f"£{format(selling_price, '.2f')}"

        output_label.configure(app, text=formatted_selling_price, text_color="black")

        price_entry.delete(0, END)
        markup_entry.delete(0, END)

# Gross Margin Calculator

heading = CTkLabel(app, text="Gross Margin Calculator")
heading.configure(font=("Arial", 20, "bold"))
heading.pack(padx=20, pady=20)

price_entry = CTkEntry(app, placeholder_text="Price in £")
price_entry.pack(padx=20, pady=10)

markup_entry = CTkEntry(app, placeholder_text="Percentage Mark Up")
markup_entry.pack(padx=20, pady=10)

output_label = CTkLabel(app, text="£")
output_label.configure(font=("Arial", 16, "bold"))
output_label.pack(padx=20, pady=10)

calculate_btn = CTkButton(app, text="Calculate", command=calculate_gm)
calculate_btn.pack(padx=20, pady=10)

footer_label = CTkLabel(app, text=f"Created by James Chance https://github.com/JDJC3D")
footer_label.configure(font=("Arial", 10, "italic"))
footer_label.pack(padx=20, pady=20)


app.mainloop()

# TODO: Redo UI with labels
# TODO: Move from Pack to Grid
# TODO: Add a custom font
# TODO: Create a custom Icon (Get Canva for this)
# TODO: Create exe for desktop use (see notes on customtkinter site)
# TODO: Add Exit button
# TODO: Add hyperlink to the footer https://www.tutorialspoint.com/how-to-create-hyperlink-in-a-tkinter-text-widget
