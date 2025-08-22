
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

    def on_drop(self, event):
        """Manejar archivos soltados"""
        file_path = event.data
        # Limpiar la ruta (tkdnd puede agregar {} o espacios extra)
        if file_path.startswith('{') and file_path.endswith('}'):
            file_path = file_path[1:-1]
        file_path = file_path.strip()
        
        self.set_file(file_path)
        self.configure(bg='lightgreen')
        self.label.configure(bg='lightgreen')
    
    def on_click(self, event):
        """Permitir seleccionar archivo haciendo click"""
        filetypes = []
        if '.iso' in str(self.file_types).lower():
            filetypes.append(("Archivos ISO", "*.iso"))
        if 'hash' in str(self.file_types).lower():
            filetypes.extend([("Archivos de Hash", "*.txt"), ("SHA256SUMS", "*SUMS*")])
        filetypes.append(("Todos los archivos", "*.*"))
        
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            self.set_file(file_path)
    
    def set_file(self, file_path):
        """Establecer archivo seleccionado"""
        self.file_path = file_path
        filename = os.path.basename(file_path)
        self.label.configure(text=f"✓ {filename}\n\n{file_path}")
        self.configure(bg='lightgreen')
        self.label.configure(bg='lightgreen')

    def get_file_path(self):
        """Obtener ruta del archivo seleccionado"""
        return self.file_path
    
    def reset(self):
        """Resetear el frame"""
        self.file_path = ""
        self.configure(bg='lightgray')
        self.label.configure(bg='lightgray')