COLOR = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
def label(colors):
    val =  str(int(str(COLOR.index(colors[0])) + str(COLOR.index(colors[1]))) * (10 ** COLOR.index(colors[2])))
    if 3 < len(val) < 8: return str(int(val) // 1000) + " kiloohms"
    if 8 <= len(val) < 9: return str(int(val) // 1000000) + " megaohms"
    if len(val) >= 9: return str(int(val) // 1000000000) + " gigaohms"
    return val + " ohms"