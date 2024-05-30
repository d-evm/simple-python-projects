import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, font
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")
        
        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack()

        self.watermark_entry = tk.Entry(root, width=50)
        self.watermark_entry.pack()
        self.watermark_entry.insert(0, "Enter watermark text here")

        self.font_size_label = tk.Label(root, text="Font Size:")
        self.font_size_label.pack()
        self.font_size = tk.IntVar(value=36)
        self.font_size_spinbox = tk.Spinbox(root, from_=10, to=100, textvariable=self.font_size)
        self.font_size_spinbox.pack()

        self.font_style_label = tk.Label(root, text="Font Style:")
        self.font_style_label.pack()
        self.font_style = tk.StringVar(value="Arial")
        self.font_style_combobox = tk.OptionMenu(root, self.font_style, *font.families())
        self.font_style_combobox.pack()

        self.font_color_btn = tk.Button(root, text="Select Font Color", command=self.select_color)
        self.font_color_btn.pack()
        self.font_color = (255, 255, 255, 128)

        self.position_label = tk.Label(root, text="Watermark Position:")
        self.position_label.pack()
        self.position_options = ["Bottom-Right", "Bottom-Left", "Top-Right", "Top-Left", "Center"]
        self.position = tk.StringVar(value="Bottom-Right")
        self.position_menu = tk.OptionMenu(root, self.position, *self.position_options)
        self.position_menu.pack()

        self.add_watermark_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_btn.pack()

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack()

        self.image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def select_color(self):
        color_code = colorchooser.askcolor(title="Choose font color")
        if color_code:
            self.font_color = color_code[0] + (128,)

    def get_position(self, width, height, textwidth, textheight):
        if self.position.get() == "Bottom-Right":
            return width - textwidth - 10, height - textheight - 10
        elif self.position.get() == "Bottom-Left":
            return 10, height - textheight - 10
        elif self.position.get() == "Top-Right":
            return width - textwidth - 10, 10
        elif self.position.get() == "Top-Left":
            return 10, 10
        elif self.position.get() == "Center":
            return (width - textwidth) // 2, (height - textheight) // 2

    def add_watermark(self):
        if self.image:
            watermark_text = self.watermark_entry.get()
            self.watermarked_image = self.image.copy()
            draw = ImageDraw.Draw(self.watermarked_image)
            font_path = "arial.ttf"
            font_size = self.font_size.get()
            font_style = self.font_style.get()
            try:
                font = ImageFont.truetype(font_style, font_size)
            except IOError:
                font = ImageFont.truetype(font_path, font_size)
            textwidth, textheight = draw.textsize(watermark_text, font)

            width, height = self.watermarked_image.size
            x, y = self.get_position(width, height, textwidth, textheight)

            draw.text((x, y), watermark_text, font=font, fill=self.font_color)
            self.display_image(self.watermarked_image)
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if file_path:
                self.watermarked_image.save(file_path)
                messagebox.showinfo("Info", "Image saved successfully.")
        else:
            messagebox.showwarning("Warning", "Please add a watermark first.")


root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()
