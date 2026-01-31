import tkinter as tk
import subprocess
import lib.gpswatch as gpswatch
from lib.config import Config as config
from tkinter import scrolledtext


def main():
    root = tk.Tk()
    root.title("GPS Uhr Ausleseprogramm")
    root.geometry("1000x800")

    gpx = tk.IntVar()
    gpx.set(config.auto_convert_to_gpx)
    delete = tk.IntVar()
    delete.set(config.auto_delete)

    txt_frame = tk.LabelFrame(root, text="Textausgabe")
    txt_frame.grid(column=0, row=0, sticky="nswe")
    btn_frame = tk.Frame(root)
    btn_frame.grid(column=1, row=0, sticky="nswe")

    text_widget = scrolledtext.ScrolledText(txt_frame, wrap="none")
    text_widget.grid(row=0, column=0, sticky="nswe")

    tk.Button(
        btn_frame,
        text="Infos abfragen",
        command=lambda: gpswatch.show_info(text_widget),
    ).grid(column=0, row=0, sticky="ew")
    tk.Button(
        btn_frame,
        text="Daten herunterladen",
        background="green",
        foreground='white',
        command=lambda: gpswatch.read_split(text_widget, gpx.get(), delete.get()),
    ).grid(column=0, row=1, sticky="ew")
    tk.Button(
        btn_frame,
        text="Daten löschen",
        background="red",
        foreground="white",
        command=lambda: gpswatch.delete(text_widget),
    ).grid(column=0, row=2, sticky="ew")

    tk.Checkbutton(
        btn_frame,
        text="Umwandeln in GPX",
        variable=gpx,
        command=lambda: print(gpx.get()),
    ).grid(column=0, row=5, sticky="ew")
    tk.Checkbutton(
        btn_frame,
        text="Löschen beim Herunterladen",
        foreground='red',
        variable=delete,
        command=lambda: print(delete.get()),
    ).grid(column=0, row=6, sticky="ew")

    tk.Button(
        btn_frame,
        text="Aufzeichungsverzeichnis öffnen",
        command=lambda: subprocess.Popen(["xdg-open", config.target_dir]),
    ).grid(column=0, row=7, sticky="ew")

    tk.Button(btn_frame, text="Beenden", command=root.destroy).grid(
        column=0, row=8, sticky="ew"
    )

    # set column weights for scaling to work
    txt_frame.columnconfigure(0, weight=1)  # scale text output to container
    txt_frame.rowconfigure(0, weight=1)

    btn_frame.rowconfigure(4, weight=1)  # scale spacer row in buttons

    root.columnconfigure(0, weight=1)  # scale text output container
    root.rowconfigure(0, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
