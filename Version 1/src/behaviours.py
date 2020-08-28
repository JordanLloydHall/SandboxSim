import random

def liquid_motion(px, world_grid):
    if random.random() < 0.5:
        if world_grid.is_valid_position(px.pos_x+1,px.pos_y) and world_grid.get_next_pixel(px.pos_x+1,px.pos_y).get_type() == "DEFAULT" and world_grid.get_current_pixel(px.pos_x+1,px.pos_y).get_type() == "DEFAULT":
            world_grid.move_pixel((px.pos_x,px.pos_y), (px.pos_x+1,px.pos_y))
    else:
        if world_grid.is_valid_position(px.pos_x-1,px.pos_y) and world_grid.get_next_pixel(px.pos_x-1,px.pos_y).get_type() == "DEFAULT" and world_grid.get_current_pixel(px.pos_x-1,px.pos_y).get_type() == "DEFAULT":
            world_grid.move_pixel((px.pos_x,px.pos_y), (px.pos_x-1,px.pos_y))

def flame_spread(px, world_grid, vanish = True):
    has_spread = False
    for y in [-1,0,1]:
            for x in [-1,0,1]:
                if world_grid.is_valid_position(px.pos_x+x,px.pos_y+y) and not (x==0 and y==0):
                    if world_grid.get_current_pixel(px.pos_x+x, px.pos_y+y).flammable >= 1:
                        if world_grid.get_current_pixel(px.pos_x+x, px.pos_y+y) == world_grid.get_next_pixel(px.pos_x+x, px.pos_y+y):
                            world_grid.set_pixel(px.pos_x+x, px.pos_y+y, "NONE")
                            world_grid.set_next_pixel(px.pos_x+x, px.pos_y+y, "FLAME")
                            has_spread = True
    if vanish:
        return has_spread


def gravity_fall(px, world_grid):
    if world_grid.is_valid_position(px.pos_x,px.pos_y+1) and world_grid.get_current_pixel(px.pos_x, px.pos_y+1).get_type() == "DEFAULT":
            if world_grid.get_next_pixel(px.pos_x, px.pos_y+1).get_type() == "DEFAULT":
                world_grid.move_pixel((px.pos_x,px.pos_y), (px.pos_x, px.pos_y+1))
                return True