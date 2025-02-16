def process_cuboid(a, b, c):
    #base case: If any dimension is zero, no cubes can be cut

    if a == 0 or b == 0 or c == 0:
        return 0, 0
    
    #the size of the largest cube that can be cut from the cuboid

    cube_size = min(a, b, c)
    
    #number of cubes that can be cut from the cuboid

    num_cubes = (a // cube_size) * (b // cube_size) * (c // cube_size)
    
    #volume of one cube

    cube_volume = cube_size ** 3
    
    #volume of a sphere

    pi = 355 / 113
    sphere_volume = (pi * cube_size ** 3) / 6
    
    #scrap for each cube 

    scrap_per_cube = cube_volume - sphere_volume
    
    #calculate the remaining cuboids after cutting out cubes:

    remaining_a = a % cube_size
    remaining_b = b % cube_size
    remaining_c = c % cube_size
    
    #calculate the remaining sub-cuboids

    remaining_cubes_a, scrap_a = process_cuboid(remaining_a, b, c)
    remaining_cubes_b, scrap_b = process_cuboid(a, remaining_b, c)
    remaining_cubes_c, scrap_c = process_cuboid(a, b, remaining_c)
    
    #now subtract the overlaps

    overlap_ab, scrap_ab = process_cuboid(remaining_a, remaining_b, c)
    overlap_ac, scrap_ac = process_cuboid(remaining_a, b, remaining_c)
    overlap_bc, scrap_bc = process_cuboid(a, remaining_b, remaining_c)
    
    #add the cubes and scraps from all the cuboids
    
    total_cubes = num_cubes + remaining_cubes_a + remaining_cubes_b + remaining_cubes_c - overlap_ab - overlap_ac - overlap_bc
    total_scraps = (num_cubes * scrap_per_cube + scrap_a + scrap_b + scrap_c 
                    - scrap_ab - scrap_ac - scrap_bc)
    
    return total_cubes, total_scraps

def main():
    T = int(input()) 
    for _ in range(T):
        a, b, c = map(int, input().split())
        cubes, scraps = process_cuboid(a, b, c)
        print(cubes)
        print(int(scraps)) 

if __name__ == "__main__":
    main()
