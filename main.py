from pyscript import display, document

# Dictionary storing Boba & Milkshakes: Drink Name -> (Code, Base Type, Price)
placeholder = {
    "GOLDEN BUBBLE MILK TEA": ("GBT", "Milk Tea", "₱160"),
    "BROWN SUGAR BOBA": ("BRM", "Milk Tea", "₱160"),
    "STRAWBERRY MILK TEA": ("SMT", "Milk Tea", "₱160"),
    "STRAWBERRY MILKSHAKE": ("STM", "Milkshake", "₱155"),
    "OREO CHEESECAKE SHAKE": ("OCH", "Milkshake", "₱155"),
    "MATCHA GREEN TEA": ("MTG", "Milk Tea", "₱155"),
    "MANGO SMOOTHIE": ("MNG", "Fruit Tea", "₱155"),
}

def element_checker(e):
    document.getElementById('result').innerHTML = ""
    
    # Get user input and convert to uppercase to match the uppercase dictionary keys
    drink_name = document.getElementById('element_Name').value.strip().upper()
    
    result = placeholder.get(
        drink_name, ("-", "Drink not found", "-")
    )
    
    document.getElementById('result').innerHTML = f"""
    <b>Code:</b> {result[0]}<br>
    <b>Drink Name:</b> {drink_name.title()}<br>
    <b>Base Type:</b> {result[1]}<br>
    <b>Price:</b> {result[2]}<br>
    """
