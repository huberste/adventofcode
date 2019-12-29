use std::env;

/* Advent of Code 2018, Day 11: Chronal Charge */
fn main() {

    let args: Vec<String> = env::args().collect();
    let input: i32;
    let grid_size = 300;
    
    if args.len() < 2 {
        input = 7165;
    } else {
        input = str::parse(&args[1].trim()).unwrap();;
    }

    /* initialize fuel cell grid */
    let mut fuel_cell_grid: Vec<Vec<i32>> = vec![vec![0; grid_size]; grid_size];

    /* calculate power level for every cell */
    for x in 0..grid_size {
        for y in 0..grid_size {
            let rack_id = x as i32 + 10; /* Find the fuel cell's rack ID, which is its X coordinate plus 10. */
            let mut power_level = rack_id * y as i32; /* Begin with a power level of the rack ID times the Y coordinate. */
            power_level += input; /* Increase the power level by the value of the grid serial number (your puzzle input). */
            power_level *= rack_id; /* Set the power level to itself multiplied by the rack ID. */
            power_level = (power_level / 100) % 10; /* Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0). */
            power_level -= 5; /* subtract 5 from the power level */
            fuel_cell_grid[x][y] = power_level;
        }
    }

    /* find maximum 3x3 square */
    let mut max = std::i32::MIN;
    let mut maxx = 0;
    let mut maxy = 0;
    for x in 0..grid_size-2 {
        for y in 0..grid_size-2 {
            let sum = fuel_cell_grid[x][y  ] + fuel_cell_grid[x+1][y  ] + fuel_cell_grid[x+2][y  ] +
                      fuel_cell_grid[x][y+1] + fuel_cell_grid[x+1][y+1] + fuel_cell_grid[x+2][y+1] +
                      fuel_cell_grid[x][y+2] + fuel_cell_grid[x+1][y+2] + fuel_cell_grid[x+2][y+2];
            if sum > max {
                max = sum;
                maxx = x;
                maxy = y;
            }
        }
    }

    println!("Solution fpr Part 1: Maximum Value {} in 3x3 square at {},{}.", max, maxx, maxy);

    /* Part 2: variable square size */
    let mut fuel_cell_grid_squares: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; grid_size]; grid_size]; grid_size];
    let mut max = std::i32::MIN;
    let mut maxx = 0;
    let mut maxy = 0;
    let mut maxz = 0;
    for z in 1..grid_size {
        for x in 0..grid_size-(z-1) {
            for y in 0..grid_size-(z-1) {
                let mut sum = 0;
                /* take value of square one size smaller */
                if z > 1 {
                    sum = fuel_cell_grid_squares[x][y][z-1];
                }
                /* add values of next row */
                for i in 0..z-1 {
                    sum += fuel_cell_grid[x+i][y+z-1];
                }
                /* add value of next column */
                for j in 0..z-1 {
                    sum += fuel_cell_grid[x+z-1][y+j];
                }
                /* add value of cell bottom right */
                sum += fuel_cell_grid[x+z-1][y+z-1];
                fuel_cell_grid_squares[x][y][z] = sum;
                if sum > max {
                    max = sum;
                    maxx = x;
                    maxy = y;
                    maxz = z;
                }
            }
        }
        println!("progress: Z={} done", z);
    }
    println!("Solution for Part 2: Maximum Value {} in {}x{} square {},{},{}.", max, maxz, maxz, maxx, maxy, maxz);

}
