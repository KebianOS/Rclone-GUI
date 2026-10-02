import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Rclone_GUI:
    def __init__(self):
        self.ventana = Gtk.Window(title="Rclone GUI")
        self.ventana.set_default_size(900, 550)
        self.ventana.set_position(Gtk.WindowPosition.CENTER)
        self.ventana.connect("destroy", Gtk.main_quit)

        self.caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.ventana.add(self.caja)
        self.etiqueta = Gtk.Label(label="Preciona el boton para cargar los remotos")
        self.boton = Gtk.Button(label="Haga click")
        self.boton.connect("clicked", self.cargar)

        self.modelo = Gtk.ListStore(str)
        self.vista = Gtk.TreeView(model=self.modelo)
        columna = Gtk.TreeViewColumn("Remotos")
        celda = Gtk.CellRendererText()
        columna.pack_start(celda, True)
        columna.add_attribute(celda, "text", 0)
        self.vista.append_column(columna)

        self.caja.pack_start(self.etiqueta, True, True, 0)
        self.caja.pack_start(self.boton, False, False, 0)
        self.caja.pack_start(self.vista, True, True, 0)
        

        self.ventana.show_all()

    def cargar(self, widget):
        self.modelo.clear()
        try:
            salida = subprocess.check_output(
                ["rclone", "listremotes"], 
                text=True,
                stderr=subprocess.STDOUT
            )
            for remoto in salida.splitlines():
                remoto = remoto.strip()
                if remoto:
                    self.modelo.append([remoto])
            self.etiqueta.set_text("Remotos cargados correctamente.")
        except Exception as e:
            self.etiqueta.set_text(f"No se encontraron remotos. \nError al cargar remotos: {e}")

    def ejecutar(self):
        Gtk.main()

Rclone_GUI().ejecutar()