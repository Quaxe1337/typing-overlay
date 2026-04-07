import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk   # Pillow library for image handling

# ── Sprite frames using images ──────────────────────────────────────────────
# Replace these file paths with your actual image files

IDLE_FRAMES = [ImageTk.PhotoImage(Image.open("images/idle.png"))]

TYPING_FRAMES = [
    ImageTk.PhotoImage(Image.open("images/typing1.png")),
    ImageTk.PhotoImage(Image.open("images/typing2.png")),
]

SPECIAL_FRAMES = {
    "Key.space":     [ImageTk.PhotoImage(Image.open("images/space.png"))],
    "Key.enter":     [ImageTk.PhotoImage(Image.open("images/enter.png"))],
    "Key.backspace": [ImageTk.PhotoImage(Image.open("images/backspace.png"))],
    "Key.esc":       [ImageTk.PhotoImage(Image.open("images/esc.png"))],
}

# ── App ──────────────────────────────────────────────────────────────────────

class TypingOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self._setup_window()
        self._setup_character()
        self._setup_drag()
        self._setup_context_menu()

        self.animating = False
        self._anim_job = None

        self._start_keyboard_listener()

    def _setup_window(self):
        r = self.root
        r.overrideredirect(True)
        r.attributes("-topmost", True)
        r.configure(bg="black")
        try:
            r.attributes("-transparentcolor", "black")
        except tk.TclError:
            pass
        r.geometry("160x180+200+600")

    def _setup_character(self):
        self.char_label = tk.Label(
            self.root,
            image=IDLE_FRAMES[0],
            bg="black"
        )
        self.char_label.pack(expand=True)

        self.key_label = tk.Label(
            self.root,
            text="",
            font=("Consolas", 10),
            bg="black",
            fg="#888888",
        )
        self.key_label.pack()

    def _setup_drag(self):
        self.char_label.bind("<ButtonPress-1>", self._start_drag)
        self.char_label.bind("<B1-Motion>",     self._on_drag)

    def _start_drag(self, event):
        self._drag_x = event.x
        self._drag_y = event.y

    def _on_drag(self, event):
        dx = event.x - self._drag_x
        dy = event.y - self._drag_y
        x  = self.root.winfo_x() + dx
        y  = self.root.winfo_y() + dy
        self.root.geometry(f"+{x}+{y}")

    def _setup_context_menu(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Small  (100px)", command=lambda: self._resize(100))
        self.menu.add_command(label="Medium (160px)", command=lambda: self._resize(160))
        self.menu.add_command(label="Large  (220px)", command=lambda: self._resize(220))
        self.menu.add_separator()
        self.menu.add_command(label="Quit", command=self.root.destroy)

        self.root.bind("<ButtonPress-3>", self._show_menu)
        self.char_label.bind("<ButtonPress-3>", self._show_menu)

    def _show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def _resize(self, size):
        # Resize images dynamically if needed
        # (Optional: reload images at different sizes)
        self.root.geometry(f"{size}x{size + 20}")

    def _start_keyboard_listener(self):
        def on_press(key):
            self.root.after(0, lambda k=key: self._handle_key(k))

        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()

    def _handle_key(self, key):
        try:
            char = key.char or "?"
            display = char if char.isprintable() else "?"
        except AttributeError:
            display = str(key).replace("Key.", "").upper()

        self.key_label.config(text=f"[ {display[:6]} ]")

        key_str = str(key)
        frames = SPECIAL_FRAMES.get(key_str, TYPING_FRAMES)
        self._play_frames(frames, idx=0)

    def _play_frames(self, frames, idx):
        if self._anim_job:
            self.root.after_cancel(self._anim_job)
        self.char_label.config(image=frames[idx])
        self.char_label.image = frames[idx]  # keep reference
        next_idx = idx + 1
        if next_idx < len(frames):
            self._anim_job = self.root.after(120, lambda: self._play_frames(frames, next_idx))
        else:
            self._anim_job = self.root.after(300, self._reset_idle)

    def _reset_idle(self):
        self.char_label.config(image=IDLE_FRAMES[0])
        self.char_label.image = IDLE_FRAMES[0]
        self.key_label.config(text="")
        self._anim_job = None

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = TypingOverlay()
    app.run()
