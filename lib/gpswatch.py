import subprocess
import tempfile
import tkinter as tk
import lib.convert as convert
from glob import glob
from tkinter import messagebox
from lib.config import Config


def show_info(widget):
    widget.delete("1.0", tk.END)
    client = subprocess.run(
        [Config.watch_client, "--output", "/dev/null"], capture_output=True
    )
    output = client.stdout.decode("utf-8")
    print(client.stderr.decode("utf-8"))
    widget.insert(tk.END, output)


def delete(widget):
    confirm = messagebox.Message(
        message="Aufzeichnungen auf der Uhr wirklich löschen?",
        title="Wirklich löschen?",
        type="yesno",
    )
    yes = confirm.show()
    print(yes)
    if yes == "yes":
        widget.delete("1.0", tk.END)
        client = subprocess.run(
            [Config.watch_client, "--output", "/dev/null", "--clear"],
            capture_output=True,
        )
        output = client.stdout.decode("utf-8")
        print(client.stderr.decode("utf-8"))
        widget.insert(tk.END, output)


def read_split(widget, convert_to_gpx, delete):
    print(f"GPX: {convert_to_gpx}")
    print(f"DELETE: {delete}")
    with tempfile.TemporaryDirectory(prefix="watch_trk") as tempdir:
        widget.delete("1.0", tk.END)
        if delete == 1:
            command = [ Config.watch_client, '--split', '--clear']
        else:
            command = [ Config.watch_client, '--split']
            
        client = subprocess.run(
            command,
            capture_output=True,
            cwd=tempdir,
            check=True,
        )
        widget.insert(tk.END, client.stdout.decode("utf-8"))
        print(client.stderr.decode("utf-8"))

        if convert_to_gpx == 1:
            convert.convert_to_gpx(tempdir)
        else:
            tcx_files = glob('*.tcx', root_dir=tempdir)
            convert.move_files(tempdir=tempdir, files=tcx_files)
        
