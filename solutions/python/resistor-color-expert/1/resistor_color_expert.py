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
    val = str(COLOR.index(colors[0]))
    if len(colors) == 4:
        val =  str(int(str(COLOR.index(colors[0])) + str(COLOR.index(colors[1]))) * (10 ** COLOR.index(colors[2])))
    if len(colors) == 5:
        val =  str(int(str(COLOR.index(colors[0])) + str(COLOR.index(colors[1])) + str(COLOR.index(colors[2]))) * (10 ** COLOR.index(colors[3])))
    if 3 < len(val) < 7:
        if int(val) % 1000 != 0:
            return str(int(val) / 1000) + " kiloohms"
        else: return str(int(val) // 1000) + " kiloohms"
    if 7 <= len(val) < 9:
        if int(val) % 1000000 != 0:
            return str(int(val) / 1000000) + " megaohms"
        else: return str(int(val) // 1000000) + " megaohms"
    if len(val) >= 9:
        if int(val) % 1000000000 != 0:
            return str(int(val) / 1000000000) + " gigaohms"
        else: return str(int(val) // 1000000000) + " gigaohms"
    return val + " ohms"

def resistor_label(colors):
    return value(colors) + " ±" + TOLERANCE[colors[-1]] if colors[-1] in TOLERANCE else value(colors)
