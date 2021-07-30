from speedtest import Speedtest
from pynotifier import Notification
from os import path
import sys


def notify_internet_speed():
    send_notification('Checking internet speed')
    internet_speed = get_internet_speed()
    converted_speed = bytes_to_megabytes(internet_speed)
    send_notification(f"{converted_speed} mbps")


def get_internet_speed():
    speedtest = Speedtest()
    download_speed = speedtest.download()
    return download_speed


def bytes_to_megabytes(value):
    converted_value = int(value / 1000 / 1000)
    return converted_value


def send_notification(internet_speed):
    bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
    path_to_icon = path.join(bundle_dir, "icon.ico")
    Notification(
        title="Internet Speed",
        description=str(internet_speed),
        duration=5,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL,
        icon_path=path_to_icon,
    ).send()
    pass


if __name__ == "__main__":
    notify_internet_speed()
