def value(colors):
    color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    colors = colors[:2]
    for i in range(len(colors)):
        colors[i] = str(color.index(colors[i]))
    return int(''.join(colors))