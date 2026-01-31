import os

class Config:
    watch_client = os.path.realpath(os.path.join(".", "lib", "crane_gps_watch", "src", "crane_gps_watch_client"))
    target_dir = os.path.expanduser('~/GPS_Aufzeichnungen')
    auto_convert_to_gpx = 1
    auto_delete = 0