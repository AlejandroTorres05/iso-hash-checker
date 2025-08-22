
#!/usr/bin/env python3
"""
Verificador de Hash para ISOs - Interfaz Gráfica
Este programa permite arrastrar y soltar archivos para verificar la integridad de una ISO.
"""

import tkinter as tk
import tkinterdnd2 as tkdnd

class DropFrame(tk.Frame):
    """Frame que acepta archivos arrastrados y soltados"""
    def __init__(self, parent, text, file_types=None):
        super().__init__(parent, relief=tk.RAISED, borderwidth=2, bg='lightgray')
        self.file_types = file_types or []
        self.file_path = ""

        # Label principal
        self.label = tk.Label(self, text=text, bg='lightgray', 
                             font=('Arial', 10), wraplength=300)
        self.label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Drag and drop
        self.drop_target_register(tkdnd.DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)
        self.dnd_bind('<<DragEnter>>', self.on_drag_enter)
        self.dnd_bind('<<DragLeave>>', self.on_drag_leave)

        # Click para seleccionar archivo
        self.bind('<Button-1>', self.on_click)
        self.label.bind('<Button-1>', self.on_click)

    def on_drag_enter(self, event):
        """Cambiar apariencia cuando se arrastra un archivo encima"""
        self.configure(bg='lightblue')
        self.label.configure(bg='lightblue')

    def on_drag_leave(self, event):
        """Restaurar apariencia cuando se sale del área"""
        self.configure(bg='lightgray')
        self.label.configure(bg='lightgray')

