#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from itertools import chain
import random as rand
import numpy as np
import time


class SpreadingColour(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SpreadingColour, self).__init__(*args, **kwargs)
        self.parser.add_argument("--protected", help="The Percentage protected",type=int, default=60)

    def run(self):

        PERCENTAGE_VAC = self.args.protected
        
        print("Percentage Protected:  ", PERCENTAGE_VAC)
    
        matrix_mapper = start_sequence(self, PERCENTAGE_VAC)
        
        final_infection_number = spread_sequence(self, matrix_mapper)
        
        print("Number of Infected", final_infection_number)
        
        printToSreen(self, final_infection_number)


            
# Start Sequence
def start_sequence(self, percentage_vac):
   
    max_brightness = self.matrix.brightness
    count = 0
    c = 255
    # red = 1, green = 2, blue = 3
    colours = [1, 2, 3]
    red_complete = False
    blue_count = 0
    green_count = 0
    PERCENTAGE_GREEN = (1024 * percentage_vac) / 100
    PERCENTAGE_BLUE = 1024 - PERCENTAGE_GREEN
    x_coord = rand.sample(range(32), 32)
    y_coord = rand.sample(range(32), 32)
    matrix_mapper = [[0 for x in range(32)] for y in range(32)]
    
    print(PERCENTAGE_GREEN)

    while (True):     
        for count_x in x_coord:
            for count_y in y_coord:
                random_colour_choice = rand.choice(colours)
                if random_colour_choice == 1 and red_complete == False:
                    matrix_mapper[count_x][count_y] = 1
                    red_complete = True
                    colours.remove(1)
                elif random_colour_choice == 2:
                    matrix_mapper[count_x][count_y] = 2
                    green_count += 1
                    if green_count >= PERCENTAGE_GREEN:
                        colours.remove(2)
                elif random_colour_choice == 3:
                    matrix_mapper[count_x][count_y] = 3
                    blue_count += 1
                    if blue_count >= PERCENTAGE_BLUE:
                        colours.remove(3)
        
        matrix_mapper = list(chain.from_iterable(matrix_mapper))
        rand.shuffle(matrix_mapper)
        
        matrix_mapper = np.array(matrix_mapper).reshape(32, 32).tolist()
                        
        print("Green Count", green_count)
        print("Blue Count", blue_count)
        
        rand.shuffle(matrix_mapper)
        for sublist in matrix_mapper:
            rand.shuffle(sublist)
        
        for count_x in x_coord:
            for count_y in y_coord:
                if matrix_mapper[count_x][count_y] == 1:
                    self.matrix.SetPixel(count_x, count_y, 255, 51, 51)
                elif matrix_mapper[count_x][count_y] == 2:
                    self.matrix.SetPixel(count_x, count_y, 51, 255, 51)
                elif matrix_mapper[count_x][count_y] == 3:
                    self.matrix.SetPixel(count_x, count_y, 0, 170, 255)
        break
    return matrix_mapper
    
# Start Sequence
def spread_sequence(self, matrix_mapper):
    
    max_brightness = self.matrix.brightness
    count = 0
    c = 255
    end_count = 0
    while (True):
        start_spread_cycle_checker = countInfected(1, matrix_mapper)
        
        infected_mapper = np.array(matrix_mapper)
        infected_mapper = np.where(infected_mapper == 1)
        
        list_of_infected = list(zip(infected_mapper[0], infected_mapper[1]))
        rand.shuffle(list_of_infected)
        
        for indice in list_of_infected:
            self.usleep(1 * 3000)
            map_to_matrix(self, indice[0], indice[1], matrix_mapper)
        
        
        end_spread_cycle_checker = countInfected(1, matrix_mapper)
        if(start_spread_cycle_checker == end_spread_cycle_checker):
            end_count += 1
            if(end_count == 6):
                return end_spread_cycle_checker
            
        

# Map Pixels to LED Matrix
def map_to_matrix(self, i, j, matrix_mapper):
    if 0 < i < 31 and 0 < j < 31:
        if matrix_mapper[i][j] == 1:
        # Left Side of Square
            if matrix_mapper[i-1][j-1] == 3:
                self.matrix.SetPixel(i-1, j-1, 255, 51, 51)
                matrix_mapper[i-1][j-1] = 1
            if matrix_mapper[i-1][j] == 3:
                self.matrix.SetPixel(i-1, j, 255, 51, 51)
                matrix_mapper[i-1][j] = 1
            if matrix_mapper[i-1][j+1] == 3:
                self.matrix.SetPixel(i-1, j+1, 255, 51, 51)
                matrix_mapper[i-1][j+1] = 1
        # Right Side of Square
            if matrix_mapper[i+1][j-1] == 3:
                self.matrix.SetPixel(i+1, j-1, 255, 51, 51)
                matrix_mapper[i+1][j-1] = 1
            if matrix_mapper[i+1][j] == 3:
                self.matrix.SetPixel(i+1, j, 255, 51, 51)
                matrix_mapper[i+1][j] = 1
            if matrix_mapper[i+1][j+1] == 3:
                self.matrix.SetPixel(i+1, j+1, 255, 51, 51)
                matrix_mapper[i+1][j+1] = 1
        # Center of Square
            if matrix_mapper[i][j-1] == 3:
                self.matrix.SetPixel(i, j-1, 255, 51, 51)
                matrix_mapper[i][j-1] = 1
            if matrix_mapper[i][j+1] == 3:
                self.matrix.SetPixel(i, j+1, 255, 51, 51)
                matrix_mapper[i][j+1] = 1
                
def printToSreen(self, infected):
    #TODO Should be percentage Vulnerbale not total population
    offscreen_canvas = self.matrix.CreateFrameCanvas()
    font = graphics.Font()
    textColor = graphics.Color(230, 230, 230)
    bottom_text = "infected"
    
    print("Develop", str(infected))
    percentage_infected = str((infected*100)//1024) + "%"
    print("percentage infected", percentage_infected)

    while True:
        offscreen_canvas.Clear()
        font.LoadFont("./fonts/10x20.bdf")
        graphics.DrawText(offscreen_canvas, font, 1, 18, textColor, percentage_infected)
        font.LoadFont("./fonts/4x6.bdf")
        graphics.DrawText(offscreen_canvas, font, 1, 26, textColor, bottom_text)
        
        time.sleep(2)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        time.sleep(5)
        offscreen_canvas.Clear()
        return
    
                
def countInfected(red, list):
    return sum([i.count(red) for i in list])


# Main function
if __name__ == "__main__":
    spreading_colour = SpreadingColour()
    if (not spreading_colour.process()):
        spreading_colour.print_help()