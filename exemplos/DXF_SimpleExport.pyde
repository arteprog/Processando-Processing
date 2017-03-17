""" Simple DXF Export
    by Simon Greenwold.
    
    Use a tecla'R' para exportar um arquivo DXF.
    """

add_library('dxf')  # equivale ao import processing.dxf.*
gravar = False

def setup():
    size(400, 400, P3D)
    noStroke()
    sphereDetail(12)

def draw():
    global gravar
    if gravar:
        beginRaw(DXF, "output.dxf")  # Incicia a gravação no arquivo

    lights()
    background(0)
    translate(width / 3, height / 3, -200)
    rotateZ(map(mouseY, 0, height, 0, PI))
    rotateY(map(mouseX, 0, width, 0, HALF_PI))
    for y in range(-2, 2):
        for x in range(-2, 2):
            for z in range(-2, 2):
                pushMatrix()
                translate(120 * x, 120 * y, -120 * z)
                sphere(30)
                popMatrix()
    if gravar:
        endRaw()
        gravar = False  # Para de gravar no arquivo

def keyPressed():
    global gravar
    if key == 'R' or key == 'r':
        # Tecla R para salvar o arquivo
        gravar = True
