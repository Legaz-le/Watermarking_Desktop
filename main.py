from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageFont,ImageTk

global add_image,label,label_or,select_image_button,heading,panel,filename,my_entry
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.buttons_and_labels()





    def buttons_and_labels(self):
        global add_image, label, label_or, select_image_button,heading
        heading = Frame(root, bg='black')
        heading.pack(fill=BOTH)
        button = Button(heading,text="Close App", command=root.destroy,width=15)
        button.pack(side=LEFT,pady=10,padx=5)
        label = Label(root,text="Drag your Images here")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        add_image = Button(heading,text="Select Images",width=15,command=lambda:[self.open_images(),
                                                                         select_image_button.place_forget(),
                                                                         label.place_forget(),
                                                                         label_or.place_forget(),
                                                                         self.next_button(),
                                                                         add_image.place_forget()])
        add_image.place(relx=0.52, rely=0.5, anchor=CENTER)
        label_or = Label(root,text="or")
        label_or.place(relx=0.5, rely=0.53, anchor=CENTER)
        select_image_button = Button(root,text="Select Images", width=15,height=2,command=self.window)
        select_image_button.place(relx=0.5, rely=0.57, anchor=CENTER)


    def window(self):
        interface = Toplevel(root)
        interface.geometry("200x200")
        from_my_compute_button = Button(interface, text="From you computer",width=20, command=lambda:[self.open_images(),
                                                                                                      interface.destroy(),
                                                                                                      add_image.place_forget(),
                                                                                                      select_image_button.place_forget(),
                                                                                                      label.place_forget(),
                                                                                                      label_or.place_forget(),
                                                                                                      self.next_button()])
        from_my_compute_button.pack(pady = 10)


    def open_image(self):
        save_files =filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
        return save_files

    def open_logo(self):
        global save_logo
        save_logo = filedialog.askopenfilename(title="Open Image File",filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
        return save_logo

    def open_images(self):
        global  filename, my_entry,panel
        filename = self.open_image()
        img_ = Image.open(filename).resize((800,800))
        img = ImageTk.PhotoImage(img_)
        panel = Label(root,image=img)
        panel.image = img
        panel.place(relx=0.5, rely=0.5, anchor=CENTER)
        img_.save(filename)
        my_entry = Entry(root, font=("Helvetica", 24))
        my_entry.pack(pady=20)

    def next_button(self):
        next_step_button = Button(heading, text="Next Step", width=15, command=lambda: [add_image.place_forget(),
                                                                                        select_image_button.place_forget(),
                                                                                        label.place_forget(),
                                                                                        label_or.place_forget(),])
        next_step_button.pack(side=RIGHT, pady=10, padx=5)
        add_text = Button(heading, text="Add Text", width=13, command=self.add_it)
        add_text.place(relx=0.4, rely=0.5, anchor=CENTER)
        add_logo = Button(heading, text="Add Logo", width=13,command=lambda:[self.open_logo(),add_logo.place_forget()])
        add_logo.place(relx=0.6, rely=0.5, anchor=CENTER)
        display = Button(heading, text="Display",width=13, command=self.add_logo)
        display.place(relx=0.5, rely=0.5, anchor=CENTER)

    def add_it(self):
        # Open our image

        my_image = Image.open(filename)
        edit_image = ImageDraw.Draw(my_image)
        # Define The Font
        text_font = ImageFont.truetype("arial.ttf", 46)
        # Get text to add to image
        text_to_add = my_entry.get()
        # Edit the Image
        edit_image.text((150, 300), text_to_add, "green", font=text_font)

        # Save The Image
        my_image.save(filename)

        # Clear the entry box
        my_entry.delete(0, END)
        my_entry.insert(0, "Saving File...")

        # Wait a couple seconds and then show image
        panel.after(2000, self.show_pic)

    def add_logo(self):
        global  filename, save_logo  # Ensure these variables are accessible
        if not filename or not save_logo:
            print("Logo or image file not selected.")
            return

        try:
            # Open the background image and the logo
            background_image = Image.open(filename).convert("RGBA")  # Ensure background is in RGBA mode
            logo_image = Image.open(save_logo).convert("RGBA")  # Ensure logo is in RGBA mode

            # Resize the logo if necessary
            logo_size = (100, 100)  # Example size, adjust as needed
            logo_image = logo_image.resize(logo_size, Image.Resampling.LANCZOS)

            # Calculate the position to paste the logo (e.g., bottom-right corner)
            position = (
                background_image.width - logo_image.width - 10,  # 10 pixels from the right
                background_image.height - logo_image.height - 10  # 10 pixels from the bottom
            )

            # Paste the logo onto the background image with transparency
            background_image.paste(logo_image, position, logo_image)  # Use logo_image as the mask

            # Save the result (convert back to RGB if saving as JPEG)
            background_image.convert("RGB").save(filename)
            print("Logo added successfully!")

            # Refresh the displayed image (assuming `panel` is a GUI element)
            panel.after(2000, self.show_pic)

        except Exception as e:
            print(f"An error occurred: {e}")


    def show_pic(self):
        # Show New Image
        global aspen2
        aspen2 = Image.open(filename)
        aspen2 = ImageTk.PhotoImage(aspen2)
        panel.config(image=aspen2)
        panel.image = aspen2
        panel.place(relx=0.5, rely=0.5, anchor=CENTER)
        # Clear the entry box
        my_entry.delete(0, END)


















root = tk.Tk()
root.geometry("800x800")
myapp = App(root)
myapp.mainloop()