import subprocess
import re
import time
from PIL import Image, ImageDraw  # This is actually importing Pillow

while True:
    output = subprocess.check_output("ping 8.8.8.8", shell=True)
    output = output.decode("utf-8")  # Convert bytes to string

    # Use regular expression to find 'time=xx' pattern
    times = re.findall("time=\d+\.?\d*", output)

    times = [float(t.split("=")[1]) for t in times]
    average = int(sum(times) / len(times))

    print("Average: ", average)
    if average < 80:
        font_color = (0, 255, 0)  # green
    if 80 <= average <= 150:
        font_color = (255, 255, 0)  # yellow
    if average > 150:
        font_color = (255, 0, 0)  # red
    # Create an image
    img = Image.new("RGBA", (30, 30), color=(0, 0, 0, 0))  # bg color

    d = ImageDraw.Draw(img)
    d.text((10, 10), str(average), fill=font_color, align="center")  # text color

    img.save("average.png")
    time.sleep(5)
