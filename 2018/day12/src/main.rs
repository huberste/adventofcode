use std::env;
use std::fs;

fn print_gen(input: &Vec<bool>) {
    for val in input {
        if *val {print!("#");} else {print!(".");}
    }
    println!("");
}

/* Advent of Code 2018, Day 12: Subterranean Sustainability */
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

    let mut i = 0;
    let mut initial_state: &str = "";
    let mut instructions: Vec<((bool, bool, bool, bool, bool), bool)> = Vec::new();
    for line in contents.lines() {
        /* first line has initial state */
        if i == 0 {
            let split: Vec<&str> = line.split("initial state: ").collect();
            initial_state = split[1];
        }
        /* second line is empty */
        else if i == 1 {
            // skip
        }
        /* after the third line, every line contains instructions */
        else {
            let mut instruction = (false, false, false, false, false, false);
            for (ind, chr) in line.char_indices() {
                if ind == 0 {
                    instruction.0 = if chr == '#' { true } else { false };
                } else if ind == 1 {
                    instruction.1 = if chr == '#' { true } else { false };
                } else if ind == 2 {
                    instruction.2 = if chr == '#' { true } else { false };
                } else if ind == 3 {
                    instruction.3 = if chr == '#' { true } else { false };
                } else if ind == 4 {
                    instruction.4 = if chr == '#' { true } else { false };
                } else if ind == 9 {
                    instruction.5 = if chr == '#' { true } else { false };
                }
            }
            instructions.push(((instruction.0, instruction.1, instruction.2, instruction.3, instruction.4),instruction.5));
        }
        i += 1;
    }

    let generations: i64 = 50000000000; /* fifty billion */
    let mut previous_generation: Vec<bool> = Vec::new();
    let mut offset: i64 = 0;
    for chr in initial_state.chars() {
        if chr == '#' {
            previous_generation.push(true);
        } else {
            previous_generation.push(false);
        }
    }
    let mut lastgen = 0;
    for gen in 1..generations+1 {
        let mut generation: Vec<bool> = Vec::new();
        let mut i = 0;

        let len = previous_generation.len();
        /* the leftmost pot */
        let mut state = (false, false, false, false, false);
        state.3 = previous_generation[0];
        state.4 = previous_generation[1];
        for instruction in &instructions {
            if state == instruction.0 {
                if instruction.1 {
                    generation.push(instruction.1);
                    offset -= 1;
                }
            }
        }
        /* for every pot */
        for _pot in &previous_generation {
            let mut state = (false, false, false, false, false);
            if i > 1 {
                state.0 = previous_generation[i-2];
            }
            if i > 0 {
                state.1 = previous_generation[i-1];
            }
            state.2 = previous_generation[i];
            if i < len - 1 {
                state.3 = previous_generation[i+1];
            }
            if i < len - 2 {
                state.4 = previous_generation[i+2];
            }
            for instruction in &instructions {
                if state == instruction.0 {
                    if generation.len() == 0 && !instruction.1 {
                        offset += 1;
                    } else {
                        generation.push(instruction.1);
                    }
                }
            }
            i += 1;
        }
        /* pots to the right */
        state = (false, false, false, false, false);
        state.0 = previous_generation[&previous_generation.len()-2];
        state.1 = previous_generation[&previous_generation.len()-1];
        for instruction in &instructions {
            if state == instruction.0 {
                if instruction.1 {
                    generation.push(instruction.1);
                }
            }
        }

        if previous_generation == generation {
            println!("generation steady-state: {} (offset: {})", gen, offset);
            //print_gen(&previous_generation);
            lastgen = gen;
            i = 0;
            let mut number_sum = 0;
            for pot in &previous_generation {
                if *pot {
                    number_sum += i as i64 + offset;
                }
                i += 1;
            }
            println!("sum at generation steady state: {} (offset: {})", number_sum, offset);
            break;
        }

        previous_generation = generation;

        if gen == 20 {
            i = 0;
            let mut number_sum = 0;
            for pot in &previous_generation {
                if *pot {
                    number_sum += i as i64 + offset;
                }
                i += 1;
            }
            println!("solution part 1: {} (offset: {})", number_sum, offset);
            //print_gen(&previous_generation);
        }

    }

    offset = offset +(generations - lastgen);

    i = 0;
    let mut number_sum = 0;
    for pot in &previous_generation {
        if *pot {
            number_sum += i as i64 + offset;
        }
        i += 1;
    }

    println!("Solution Part 2: {}", number_sum);

}
