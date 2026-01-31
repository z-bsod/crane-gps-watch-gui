from glob import glob
import subprocess
import os
import shutil
from lib.config import Config as conf


def convert_to_gpx(tempdir):
    tcx_files = glob("*.tcx", root_dir=tempdir)

    for file in tcx_files:
        try:
            print(f"converting {file}...")
            subprocess.run(
                [
                    "gpsbabel",
                    "-i",
                    "gtrnctr",
                    "-f",
                    file,
                    "-o",
                    "gpx",
                    "-F",
                    f"{os.path.splitext(file)[0]}.gpx",
                ],
                cwd=tempdir,
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"error converting {file}")
            print(e.message)
    print("conversion done")
    gpx_files = glob("*.gpx", root_dir=tempdir)
    move_files(tempdir=tempdir, files=gpx_files)


def move_file(filename, tempdir):
    date = filename.split("T")[0]
    year = date.split("-")[0]
    month = date.split("-")[1]

    target_path = os.path.join(conf.target_dir, year, month)
    os.makedirs(target_path, exist_ok=True)

    shutil.copy(src=os.path.join(tempdir, filename), dst=os.path.join(target_path, filename))


def move_files(tempdir, files):
    for file in files:
        move_file(filename=file, tempdir=tempdir)
