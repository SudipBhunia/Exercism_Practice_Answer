def color_code(color):
    return [i for i in range(len(colors())) if colors()[i] == color].pop()

def colors():
    color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    return color