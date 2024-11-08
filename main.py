from customtkinter import *

app = CTk()
app.geometry("320x320")
app.title("Gross Margin Calculator")

# Formula COST_PRICE / ( 1 - MARGIN / 100 )

def calculate_gm():

    cost_price = float(price_entry.get())
    margin = float(markup_entry.get())
    selling_price = round(cost_price / (1 - ( margin / 100) ), 2)

    output_label.configure(app, text=f"£{selling_price}")

# Gross Margin Calculator

heading = CTkLabel(app, text="Gross Margin Calculator")
heading.pack(padx=20, pady=20)

price_entry = CTkEntry(app, placeholder_text="Price in Pounds")
price_entry.pack(padx=20, pady=10)

markup_entry = CTkEntry(app, placeholder_text="60")
markup_entry.pack(padx=20, pady=10)

output_label = CTkLabel(app, text="£")
output_label.pack(padx=20, pady=10)

calculate_btn = CTkButton(app, text="Calculate", command=calculate_gm)
calculate_btn.pack(padx=20, pady=10)

formula_label = CTkLabel(app, text="Formula: COST_PRICE / ( 1 - MARGIN / 100 )")
formula_label.pack(padx=20, pady=10)

app.mainloop()

# TODO 1: Redo UI with labels (Add footer with my details as well (name, copright, github))
# TODO 2: Move from Pack to Grid
# TODO 3: Add Error catching
# TODO 4: Fix bug with number missing 0 when using 10.00 and 60% markup
# TODO 5: Add a custom font
# TODO 6: Create a custom Icon (Get Canva for this)
# TODO 7: Create exe for desktop use (see notes on customtkinter site)
# TODO 8: Add Exit button
