from tkinter import Tk
from modulos import logueo

########################################################################
class Aplicacion(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""

        self.root = parent
        self.root.withdraw()

        subFrame = logueo.logueo1_Ingreso_de_usuario(self, 500, 400, 'Ingreso de usuario')

#----------------------------------------------------------------------
def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()

