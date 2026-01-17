COLOR = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}
def value(colors):
    val = COLOR.index(colors[0])
    if len(colors) == 4:
        val =  int(str(COLOR.index(colors[0])) + str(COLOR.index(colors[1]))) * (10 ** COLOR.index(colors[2]))
    if len(colors) == 5:
        val =  int(str(COLOR.index(colors[0])) + str(COLOR.index(colors[1])) + str(COLOR.index(colors[2]))) * (10 ** COLOR.index(colors[3]))
    if val >= 1_000_000_000: return f"{int(val) / 1000000000:g} gigaohms"
    if val >= 1_000_000: return f"{int(val) / 1000000:g} megaohms"
    if val >= 1_000: return f"{int(val) / 1000:g} kiloohms"
    return f"{val} ohms"

def resistor_label(colors):
    return value(colors) + " ±" + TOLERANCE[colors[-1]] if colors[-1] in TOLERANCE else value(colors)
