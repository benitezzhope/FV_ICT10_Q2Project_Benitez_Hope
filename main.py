from pyscript import document

# Seatwork 1 

members = ["Hope Benitez", "Jacob Minguillo", "Maya Peters", "Anna Kone"]

def check_club(e):
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()
    name = (first + " " + last).title()

    in_club = name in members

    response = [
        "Sorry " + name + ", your name is not on the list.",
        "Congratulations " + name + "! You're in CommArts."
    ]

    final_output = response[in_club]
    document.getElementById("result1").innerText = final_output

# Drill 2 

# Define the starting sets outside the function so they persist
g7 = {'Eren Jaeger', 'Mikasa Ackermann', 'Armin Arlelt'} 
g8 = {'Sasha Braus', 'Connie Springer', 'Jean Kirstein'}
g9 = {'Levi Ackermann', 'Erwin Smith', 'Hange Zoe'} 
g10 = {'Reiner Braun', 'Bertholdt Hoover', 'Annie Leonhart', 'Pieck Finger', 'Porco Galliard'}

# Combine them once into a master set for the club
all_members = g7 | g8 | g9 | g10

def check(e): 
    # Get string values from input fields and combine into a properly capitalized full name
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()
    name = (first + " " + last).title()
    
    # Permanently add the new name
    all_members.add(name)
    
    # Sort members alphabetically
    finalmembers = "<br>".join(sorted(all_members))
   
    # Format final output with the roster and total count
    output_html = f"<div>{finalmembers}<br><br><b>Number of Members: {len(all_members)}</b></div>"
    
    # Render HTML into the results paragraph
    document.getElementById("result2").innerHTML = output_html
    
    # Make the second box appear
    document.getElementById("secondbox").style.display = "block"

#Skills Test

# Dictionary containing element information
# element symbol, element name, atomic number, atomic mass
nonmetals = {
    "H": ("H", "Hydrogen", 1, 1.008),
    "He": ("He", "Helium", 2, 4.003), 
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "F": ("F", "Fluorine", 9, 18.998),
    "Ne": ("Ne", "Neon", 10, 20.180),
    "P": ("P", "Phosphorus", 15, 30.974),
    "S": ("S", "Sulfur", 16, 32.065),
    "Cl": ("Cl", "Chlorine", 17, 35.453),
    "Ar": ("Ar", "Argon", 18, 39.948),
    "Se": ("Se", "Selenium", 34, 78.971),
    "Br": ("Br", "Bromine", 35, 79.904),
    "Kr": ("Kr", "Krypton", 36, 83.798),
    "I": ("I", "Iodine", 53, 126.904),
    "Xe": ("Xe", "Xenon", 54, 131.293),
    "Rn": ("Rn", "Radon", 86, 222),
    "At": ("At", "Astatine", 85, 210)
}

# Function to search for an element
def search_nm(e):
    # Get the input value from HTML, added capitalize() to prevent capitalization errors
    Nonmetal = document.getElementById("nonmetal").value.capitalize()
    
    # Retrieve information from Dictionary 
    # Fallback: symbol shows "Element not found", others show "-"
    result = nonmetals.get(Nonmetal, ("Element not found", "-", "-", "-"))
    
    # Display the result in HTML
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("number").innerText = result[2] 
    document.getElementById("mass").innerText = result[3]
    
    # Reveal the result box once the button is pressed
    document.getElementById("result3").style.display = "block"