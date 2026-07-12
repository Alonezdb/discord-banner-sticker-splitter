import os
import subprocess
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog, messagebox

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    has_dnd = True
except ImportError:
    has_dnd = False

if has_dnd:
    class BaseApp(ctk.CTk, TkinterDnD.DnDWrapper):
        def __init__(self):
            super().__init__()
else:
    class BaseApp(ctk.CTk):
        def __init__(self):
            super().__init__()

class App(BaseApp):
    def __init__(self):
        super().__init__()
        self.title("Banner Sticker Splitter")
        self.geometry("840x660")
        self.resizable(False, False)
        
        self.dnd_active = False
        if has_dnd:
            try:
                self.TkdndVersion = TkinterDnD._require(self)
                self.dnd_active = True
            except Exception:
                pass

        self.tiles = []
        self.tile_images = []
        self.original_name = "banner"

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        self._build_ui()

        if self.dnd_active:
            self.drop_frame.drop_target_register(DND_FILES)
            self.drop_frame.dnd_bind("<<Drop>>", self._handle_file_drop)

    def _build_ui(self):
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        header_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(header_frame, text="Banner Sticker Splitter", font=ctk.CTkFont(size=24, weight="bold"))
        title_label.grid(row=0, column=0, sticky="w")

        subtitle_label = ctk.CTkLabel(header_frame, text="Select or drop a 960x640 banner image to split it into six 320x320 tiles for Discord.", font=ctk.CTkFont(size=13), text_color="#a1a1aa")
        subtitle_label.grid(row=1, column=0, sticky="w", pady=(2, 0))

        drop_msg = "Drag & drop your banner image here, or click to browse" if self.dnd_active else "Click here to select a banner image"
        self.drop_frame = ctk.CTkFrame(self, fg_color="#18181b", border_color="#27272a", border_width=2, corner_radius=12, height=100)
        self.drop_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        self.drop_frame.grid_propagate(False)
        self.drop_frame.grid_rowconfigure(0, weight=1)
        self.drop_frame.grid_columnconfigure(0, weight=1)

        self.drop_label = ctk.CTkLabel(self.drop_frame, text=drop_msg, font=ctk.CTkFont(size=14, weight="normal"), text_color="#d4d4d8")
        self.drop_label.grid(row=0, column=0, sticky="nsew")
        self.drop_label.bind("<Button-1>", lambda e: self._select_image_dialog())
        self.drop_frame.bind("<Button-1>", lambda e: self._select_image_dialog())

        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        
        for c in range(3):
            self.grid_frame.grid_columnconfigure(c, weight=1)
        for r in range(2):
            self.grid_frame.grid_rowconfigure(r, weight=1)

        self.tile_panels = []
        self.tile_labels = []

        for r in range(2):
            for c in range(3):
                panel = ctk.CTkFrame(self.grid_frame, fg_color="#18181b", border_color="#27272a", border_width=1, corner_radius=8)
                panel.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")
                panel.grid_rowconfigure(0, weight=1)
                panel.grid_columnconfigure(0, weight=1)

                idx = r * 3 + c + 1
                lbl = ctk.CTkLabel(panel, text=str(idx), font=ctk.CTkFont(weight="bold", size=28), text_color="#3f3f46")
                lbl.grid(row=0, column=0, sticky="nsew")

                self.tile_panels.append(panel)
                self.tile_labels.append(lbl)

        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=(10, 20))
        footer_frame.grid_columnconfigure(0, weight=1)

        self.export_btn = ctk.CTkButton(footer_frame, text="Export Stickers", fg_color="#2563eb", hover_color="#1d4ed8", font=ctk.CTkFont(weight="bold", size=15), height=44, state="disabled", command=self._export_stickers)
        self.export_btn.grid(row=0, column=0, pady=5)

    def _select_image_dialog(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp")])
        if path:
            self._load_and_process_image(path)

    def _handle_file_drop(self, event):
        path = event.data.strip()
        if path.startswith("{") and path.endswith("}"):
            path = path[1:-1]
        if os.path.isfile(path) and path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            self._load_and_process_image(path)

    def _load_and_process_image(self, path):
        try:
            img = Image.open(path)
            target_w, target_h = 960, 640
            
            img_w, img_h = img.size
            aspect_target = target_w / target_h
            aspect_img = img_w / img_h
            
            if aspect_img > aspect_target:
                new_h = target_h
                new_w = int(img_w * (target_h / img_h))
            else:
                new_w = target_w
                new_h = int(img_h * (target_w / img_w))
                
            try:
                resample_filter = Image.Resampling.LANCZOS
            except AttributeError:
                resample_filter = Image.ANTIALIAS
                
            img_resized = img.resize((new_w, new_h), resample_filter)
            
            left = (new_w - target_w) // 2
            top = (new_h - target_h) // 2
            right = left + target_w
            bottom = top + target_h
            
            img_cropped = img_resized.crop((left, top, right, bottom))
            
            self.tiles.clear()
            self.tile_images.clear()
            self.original_name = os.path.splitext(os.path.basename(path))[0]
            
            for r in range(2):
                for c in range(3):
                    tile = img_cropped.crop((c * 320, r * 320, (c + 1) * 320, (r + 1) * 320))
                    self.tiles.append(tile)
                    
                    ctk_img = ctk.CTkImage(light_image=tile, dark_image=tile, size=(160, 110))
                    self.tile_images.append(ctk_img)
            
            for idx, ctk_img in enumerate(self.tile_images):
                self.tile_labels[idx].configure(image=ctk_img, text="")
                self.tile_panels[idx].configure(border_color="#2563eb")
                
            self.drop_label.configure(text=f"Selected: {os.path.basename(path)} (Loaded & Split)")
            self.drop_frame.configure(border_color="#2563eb")
            self.export_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image:\n{str(e)}")

    def _export_stickers(self):
        if not self.tiles:
            return
            
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

        try:
            for idx, tile in enumerate(self.tiles):
                filename = f"{idx + 1}.png"
                filepath = os.path.join(output_dir, filename)
                tile.save(filepath, format="PNG")
                
            messagebox.showinfo("Export Successful", f"Successfully exported 6 stickers to:\n{output_dir}")
            
            try:
                os.startfile(output_dir)
            except Exception:
                subprocess.Popen(['explorer', os.path.normpath(output_dir)])
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save stickers:\n{str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()


