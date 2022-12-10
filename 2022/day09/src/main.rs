use std::env;
use std::fs;


/*
--- Day 9: Rope Bridge ---
*/

fn main() {

    let args: Vec<String> = env::args().collect();
    let inputfile;

    if args.len() < 2 {
        /* input file name */
        inputfile = "input";
    } else {
        inputfile = &args[1];
    }

    /* read file */
    let contents = fs::read_to_string(inputfile)
        .expect("Something went wrong reading the file");

    let num_knots:usize=10;
    let mut visited: Vec<Vec<(i32, i32)>> = vec![vec![]; num_knots];
    let mut knot_x: Vec<i32> = vec![0; num_knots];
    let mut knot_y: Vec<i32> = vec![0; num_knots];

    for line in contents.lines() {
        /* parse */
        let mut movement = line.split_whitespace();
        let direction = movement.next().unwrap();
        let mut steps: usize = movement.next().unwrap().parse().unwrap();
        /* move */
        while steps > 0 {
            steps -= 1;
            /* move head = knot[0]*/
            if direction == "U" {
                knot_x[0] -= 1;
            } else if direction == "D" {
                knot_x[0] += 1;
            } else if direction == "L" {
                knot_y[0] -= 1;
            } else if direction == "R" {
                knot_y[0] += 1;
            } else {
                panic!("unknown direction");
            }
            /* move knots */
            for knot in 1..num_knots {
                if knot_x[knot-1] == knot_x[knot]  {
                    /* move on y axis only */
                    if (knot_y[knot-1] - knot_y[knot]).abs() > 1 {
                        knot_y[knot] += (knot_y[knot-1] - knot_y[knot]).signum();
                    }
                } else if knot_y[knot-1] == knot_y[knot] {
                    /* move on x axis only */
                    if (knot_x[knot-1] - knot_x[knot]).abs() > 1 {
                        knot_x[knot] += (knot_x[knot-1] - knot_x[knot]).signum();
                    }
                } else {
                    /* move diagonnaly */
                    if (knot_y[knot-1] - knot_y[knot]).abs() + (knot_x[knot-1] - knot_x[knot]).abs()  > 2 {
                        knot_x[knot] += (knot_x[knot-1] - knot_x[knot]).signum();
                        knot_y[knot] += (knot_y[knot-1] - knot_y[knot]).signum();
                    }
                }
                /* update visited */
                visited[knot].push((knot_x[knot], knot_y[knot]));

            }
        }
    }

    visited[1].sort();
    visited[1].dedup();
    println!("Part 1: How many positions does the tail of the rope visit at least once?");
    println!("The tail visited {} positions.", visited[1].len());
    /* My puzzle answer was 6284. (13 for simple) */

    visited[num_knots-1].sort();
    visited[num_knots-1].dedup();
    println!("Part 2: How many positions does the tail of the rope visit at least once?");
    println!("The tail visited {} positions.", visited[num_knots-1].len());
    /* My puzzle answer was 2661. */

}