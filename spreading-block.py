#!/usr/bin/env python
from samplebase import SampleBase
import random as rand


class SpreadingColour(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SpreadingColour, self).__init__(*args, **kwargs)

    def run(self):
        
        PERCENTAGE_VAC = 30
    
        matrix_mapper = start_sequence(self, PERCENTAGE_VAC)
        
        final_infection_number = spread_sequence(self, matrix_mapper)
        
        print("Number of Infected", final_infection_number)


            
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
                        
        print("Green Count", green_count)
        print("Blue Count", blue_count)
        
        rand.shuffle(matrix_mapper)
        for sublist in matrix_mapper:
            rand.shuffle(sublist)
        
        for count_x in x_coord:
            for count_y in y_coord:
                if matrix_mapper[count_x][count_y] == 1:
                    self.matrix.SetPixel(count_x, count_y, c, 0, 0)
                elif matrix_mapper[count_x][count_y] == 2:
                    self.matrix.SetPixel(count_x, count_y, 0, c, 0)
                elif matrix_mapper[count_x][count_y] == 3:
                    self.matrix.SetPixel(count_x, count_y, 0, 0, c)
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
        for i in range(32):
            self.usleep(1 * 1000)
            for j in range(32):
                self.usleep(2 * 1000)
                map_to_matrix(self, i, j, matrix_mapper, c)
                            
        for i in reversed(range(32)):
            self.usleep(1 * 1000)
            for j in reversed(range(32)):
                self.usleep(2 * 1000)
                map_to_matrix(self, i, j, matrix_mapper, c)
        end_spread_cycle_checker = countInfected(1, matrix_mapper)
        if(start_spread_cycle_checker == end_spread_cycle_checker):
            end_count += 1
            if(end_count == 5):
                return end_spread_cycle_checker
            
        

# Map Pixels to LED Matrix
def map_to_matrix(self, i, j, matrix_mapper, c):
    if 0 < i < 31 and 0 < j < 31:
        if matrix_mapper[i][j] == 1:
        # Left Side of Square
            if matrix_mapper[i-1][j-1] == 3:
                self.matrix.SetPixel(i-1, j-1, c, 0, 0)
                matrix_mapper[i-1][j-1] = 1
            if matrix_mapper[i-1][j] == 3:
                self.matrix.SetPixel(i-1, j, c, 0, 0)
                matrix_mapper[i-1][j] = 1
            if matrix_mapper[i-1][j+1] == 3:
                self.matrix.SetPixel(i-1, j+1, c, 0, 0)
                matrix_mapper[i-1][j+1] = 1
        # Right Side of Square
            if matrix_mapper[i+1][j-1] == 3:
                self.matrix.SetPixel(i+1, j-1, c, 0, 0)
                matrix_mapper[i+1][j-1] = 1
            if matrix_mapper[i+1][j] == 3:
                self.matrix.SetPixel(i+1, j, c, 0, 0)
                matrix_mapper[i+1][j] = 1
            if matrix_mapper[i+1][j+1] == 3:
                self.matrix.SetPixel(i+1, j+1, c, 0, 0)
                matrix_mapper[i+1][j+1] = 1
        # Center of Square
            if matrix_mapper[i][j-1] == 3:
                self.matrix.SetPixel(i, j-1, c, 0, 0)
                matrix_mapper[i][j-1] = 1
            if matrix_mapper[i][j+1] == 3:
                self.matrix.SetPixel(i, j+1, c, 0, 0)
                matrix_mapper[i][j+1] = 1
                
def countInfected(red, list):
    return sum([i.count(red) for i in list])


# Main function
if __name__ == "__main__":
    spreading_colour = SpreadingColour()
    if (not spreading_colour.process()):
        spreading_colour.print_help()