#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="30%")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        textColor = graphics.Color(230, 230, 230)
        pos = offscreen_canvas.width
        my_text = self.args.text
        bottom_text = "immune"

        while True:
            offscreen_canvas.Clear()
            font.LoadFont("./fonts/10x20.bdf")
            graphics.DrawText(offscreen_canvas, font, 1, 18, textColor, my_text)
            font.LoadFont("./fonts/5x8.bdf")
            graphics.DrawText(offscreen_canvas, font, 2, 26, textColor, bottom_text)
            
            time.sleep(2)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(5)
            offscreen_canvas.Clear()
            break



# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
