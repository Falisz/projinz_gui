import tkinter as tk
import customtkinter as ctk
from mod1 import *

color_bg = "#222"
color_bg_br = "#333"
color_acc = "#d68f13"
color_acc2 = "#ffab17"


class NavButton(ctk.CTkFrame):
    def __init__(self, master, text, command, font):
        super().__init__(master)

        text_width = font.measure(text)
        button_width = text_width + 25

        self.main_button = ctk.CTkButton(self)
        self.main_button.configure(
            width=button_width,
            corner_radius=0,
            fg_color=color_bg,
            bg_color=color_bg,
            hover_color=color_acc,
            text=text,
            command=command,
            font=font)
        self.main_button.pack()

        self.bottom_border = ctk.CTkFrame(self, height=3, width=self.main_button.winfo_reqwidth(), fg_color=color_bg)
        self.bottom_border.pack(side="bottom", fill="x")

        self.selected = False

    def set_selected(self, value):
        self.selected = value
        if self.selected:
            self.main_button.configure(fg_color=color_bg_br)
            self.bottom_border.configure(fg_color=color_acc)
        else:
            self.main_button.configure(fg_color=color_bg)
            self.bottom_border.configure(fg_color=color_bg)


class GUIDash(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.target_title = ctk.CTkLabel(self, text="DASHBOARD PLACEHOLDER.")
        self.target_title.pack(pady=5)


class GUITarget(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")

        self.targetnav = ctk.CTkFrame(self, fg_color=color_bg)
        self.targetnav.pack(side="top", fill="x", padx=0, pady=0)

        buttons_set = {
            "Site Map": self.show_sitemap,
            "Scope": self.show_scope,
            "Issue Definitions": self.show_definitions
        }

        self.navbuttons = {}

        for name, command in buttons_set.items():
            self.navbuttons[name] = NavButton(self.targetnav, text=name, command=command, font=ctk.CTkFont(family="Calibri", size=14, weight="normal"))
            self.navbuttons[name].pack(side="left")

        self.content_wrapper = ctk.CTkFrame(self, fg_color="transparent")
        self.content_wrapper.pack(side="top", fill="both", expand=True)

        self.show_sitemap()

    def show_sitemap(self):
        self.clear_content_frame()

        self.paned_window = tk.PanedWindow(self.content_wrapper, orient=tk.HORIZONTAL, background=color_bg)
        self.paned_window.pack(fill="both", expand=True)

        # Left pane (vertical)
        self.left_pane = ctk.CTkFrame(self.paned_window, bg_color="transparent", width=self.winfo_reqwidth() // 3)
        self.paned_window.add(self.left_pane, stretch="always")

        # Right PanedWindow (vertical orientation)
        self.right_paned_window = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.right_paned_window, stretch="always")

        # Top right pane
        self.top_right_pane = ctk.CTkFrame(self.right_paned_window, bg_color="transparent")
        self.right_paned_window.add(self.top_right_pane, stretch="always")

        # Bottom right pane
        self.bottom_right_pane = ctk.CTkFrame(self.right_paned_window, bg_color="transparent")
        self.right_paned_window.add(self.bottom_right_pane, stretch="always")

        # Example content for the panes
        self.left_label = ctk.CTkLabel(self.left_pane, text="Sitemap content here", anchor="center")
        self.left_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.top_right_label = ctk.CTkLabel(self.top_right_pane, text="Top Right Pane", anchor="center")
        self.top_right_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.bottom_right_label = ctk.CTkLabel(self.bottom_right_pane, text="Bottom Right Pane", anchor="center")
        self.bottom_right_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.select_button(self.navbuttons["Site Map"])

        self.update_idletasks()  # Ensure the window is fully drawn before configuring panes
        self.paned_window.paneconfigure(self.left_pane, minsize=self.winfo_reqwidth() // 3)

    def show_scope(self):
        self.clear_content_frame()
        self.target_title = ctk.CTkLabel(self.content_wrapper, text="Scope content here")
        self.target_title.pack(pady=5)
        self.select_button(self.navbuttons["Scope"])

    def show_definitions(self):
        self.clear_content_frame()
        self.target_title = ctk.CTkLabel(self.content_wrapper, text="Definitions content here")
        self.target_title.pack(pady=5)
        self.select_button(self.navbuttons["Issue Definitions"])

    def clear_content_frame(self):
        for widget in self.content_wrapper.winfo_children():
            widget.pack_forget()

    def select_button(self, selected_button):
        for button in self.navbuttons.values():
            if button == selected_button:
                button.set_selected(True)
            else:
                button.set_selected(False)


class GUIProxy(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.target_title = ctk.CTkLabel(self, text="Proxy tab content here")
        self.target_title.pack(pady=5)
        self.scan_button = ctk.CTkButton(self, text="Start Scan", command=self.scan)
        self.scan_button.pack(pady=5)
        self.scan_textbox = ctk.CTkTextbox(self, width=700, height=450)

    def scan(self):
        output = test1()
        self.scan_textbox.pack(side="right",padx=10,pady=5)
        self.scan_textbox.insert("0.0", f"{output}")

class GUIIntruder(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")


class GUIRepeater(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.inspect_label = ctk.CTkLabel(self, text="Inspecting HTTP requests and responses...")
        self.inspect_label.pack(pady=5)
        self.inspect_button = ctk.CTkButton(self, text="Start Inspection", command=self.inspect)
        self.inspect_button.pack(pady=5)

    def inspect(self):
        self.inspect_label.configure(text="Inspection started...")


class GUILogs(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")

        self.logs_label = ctk.CTkLabel(self, text="Displaying logs...")
        self.logs_label.pack(pady=5)
        self.logs_button = ctk.CTkButton(self, text="Show Logs", command=self.show_logs_content)
        self.logs_button.pack(pady=5)

    def show_logs_content(self):
        self.logs_label.pack_forget()
        self.logs_label.configure(text="Logs displayed.")
        self.logs_button.pack(pady=25)
        self.logs_label.pack(pady=5)


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Security Testing App")
        self.geometry("1880x900+10+20")
        self.configure(fg_color=color_bg, bg_color=color_bg)

        self.mainnav = ctk.CTkFrame(self, bg_color=color_bg, fg_color=color_bg)
        self.mainnav.pack(side="top", fill="x", padx=0, pady=0)

        buttons_set = {
            "Dashboard": self.show_dashboard,
            "Target": self.show_target,
            "Proxy": self.show_proxy,
            "Intruder": self.show_intruder,
            "Repeater": self.show_repeater,
            "Logs": self.show_logs
        }

        self.navbuttons = {}

        for name, command in buttons_set.items():
            self.navbuttons[name] = NavButton(self.mainnav, text=name, command=command,
                                              font=ctk.CTkFont(family="Calibri", size=15, weight="bold"))
            self.navbuttons[name].pack(side="left")

        self.content_wrapper = ctk.CTkFrame(self, fg_color=color_bg_br, bg_color=color_bg_br)
        self.content_wrapper.pack(side="top", fill="both", expand=True)

        self.dashboard_frame = GUIDash(self.content_wrapper)
        self.target_frame = GUITarget(self.content_wrapper)
        self.proxy_frame = GUIProxy(self.content_wrapper)
        self.intruder_frame = GUIIntruder(self.content_wrapper)
        self.repeater_frame = GUIRepeater(self.content_wrapper)
        self.logs_frame = GUILogs(self.content_wrapper)

        self.show_target()

    def show_dashboard(self):
        self.clear_content_frame()
        self.dashboard_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Dashboard"])

    def show_target(self):
        self.clear_content_frame()
        self.target_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Target"])

    def show_proxy(self):
        self.clear_content_frame()
        self.proxy_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Proxy"])

    def show_intruder(self):
        self.clear_content_frame()
        self.intruder_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Intruder"])

    def show_repeater(self):
        self.clear_content_frame()
        self.repeater_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Repeater"])

    def show_logs(self):
        self.clear_content_frame()
        self.logs_frame.pack(side="top", fill="both", expand=True)
        self.select_button(self.navbuttons["Logs"])

    def clear_content_frame(self):
        for widget in self.content_wrapper.winfo_children():
            widget.pack_forget()

    def select_button(self, selected_button):
        for button in self.navbuttons.values():
            if button == selected_button:
                button.set_selected(True)
            else:
                button.set_selected(False)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
