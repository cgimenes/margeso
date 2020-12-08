from PIL import Image, ImageDraw

width = 15
heigth = 15

def empty_matrix():
    matrix = []


matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    
def draw():
    im = Image.new('RGB', (151, 151))
    draw = ImageDraw.Draw(im)

    white = (255, 255, 255)
    black = (0, 0, 0)

    for i in range(0,15):
        for j in range(0,15):
            color = white
            if matrix[i][j] == 1:
                draw.rectangle((i*10, j*10, i*10+10, j*10+10), fill=color, outline=(0,0,0))
            else:
                draw.rectangle((i*10, j*10, i*10+10, j*10+10), fill=color)

    im.save('pillow_imagedraw.jpg', quality=95)

def generate():
    # 1. Choose a vertex. Any vertex.
    x = random.randint(0,15)
    y = random.randint(0,15)

    # 2. Choose a connected neighbor of the vertex and travel to it. If the neighbor has not yet been visited, add the traveled edge to the spanning tree.
    # 3. Repeat step 2 until all vertexes have been visited.



