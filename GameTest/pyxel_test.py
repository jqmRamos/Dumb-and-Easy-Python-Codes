import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="SapooGame")
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_PEACH)
        pyxel.text(65, 55, 'Hello World', pyxel.frame_count % 16)
        pyxel.text(, 55, 'Hello World', pyxel.frame_count % 16)
        

App()
 

 