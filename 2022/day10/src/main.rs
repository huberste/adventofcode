use std::collections::HashMap;
use std::env;
use std::fs;


/*
--- Day 10: Cathode-Ray Tube ---
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

    let mut cycles_needed: HashMap<String, usize> = HashMap::new();
    cycles_needed.insert("noop".to_string(), 1);
    cycles_needed.insert("addx".to_string(), 2);

    let signal_cycle_start = 20;
    let signal_cycle = 40;
    let mut cycle = 0;
    let cycle_max = 240;
    let mut register: i32 = 1;

    let mut sum_of_signal_strengths = 0;

    let mut lines = contents.lines();
    let mut line = lines.next();
    let mut new_instruction = true;
    let mut instruction_line = "noop".split_whitespace();
    let mut instruction = "noop";
    let mut wait_cycles:usize = 0;

    let mut sprite_position = 0;
    while cycle <= cycle_max && line != None {
        cycle += 1;
        /* parse */
        if new_instruction {
            instruction_line = line.unwrap().split_whitespace();
            instruction = instruction_line.next().unwrap();
            wait_cycles = *cycles_needed.get(instruction).unwrap();
            new_instruction = false;
            line = lines.next();
        }
        if (cycle - signal_cycle_start) % signal_cycle == 0 {
            sum_of_signal_strengths += cycle * register;
        }
        if register-1 <= sprite_position && register+1 >= sprite_position {
            print!("#");
        } else {
            print!(".");
        }
        sprite_position = (sprite_position + 1) % 40;
        if cycle % 40 == 0 {
            println!();
        }
        wait_cycles -= 1;
        if wait_cycles < 1 {
            if instruction == "noop" {
                // do nothing
            }
            if instruction == "addx" {
                let arg: i32 = instruction_line.next().unwrap().parse().unwrap();
                register += arg
            }
            new_instruction = true;
        }
    }

    println!("Part 1: What is the sum of these six signal strengths?");
    println!("The sum is \"{}\".", sum_of_signal_strengths);
    /* My puzzle answer was 14620. (13140 for simple) */

    // println!("Part 2: How many positions does the tail of the rope visit at least once?");
    // println!("The tail visited {} positions.", visited[num_knots-1].len());
    /* My puzzle answer was BJFRHRFU:
    ###....##.####.###..#..#.###..####.#..#.
    #..#....#.#....#..#.#..#.#..#.#....#..#.
    ###.....#.###..#..#.####.#..#.###..#..#.
    #..#....#.#....###..#..#.###..#....#..#.
    #..#.#..#.#....#.#..#..#.#.#..#....#..#.
    ###...##..#....#..#.#..#.#..#.#.....##..
    */

}