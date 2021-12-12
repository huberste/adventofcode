use std::env;
use std::fs;

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
    let num_lines = contents.lines().count();
    // println!("[DEBUG] read {} lines.", num_lines);
    let binary_length :usize = contents.lines().next().unwrap().len();
    // println!("[DEBUG] line length: {}.", binary_length);
    let mut count: Vec<usize> = vec![0; binary_length];
    let mut gamma: i32 = 0;
    let mut epsilon: i32 = 0;
    let mut oxygen_possible: Vec<&str>;
    let mut cotwo_possible: Vec<&str>;
    /* iterate over lines of read String */
    for line in contents.lines() {
        oxygen_possible.push(line);
        cotwo_possible.push(line);
        let mut i: usize = 0;
        for number in line.chars() {
            if number == '1' {
                count[i] += 1;
            }
            i += 1;
        }
    }
    /* find most common / least common bits */
    for i in 0..count.len() {
        let ones: usize = count[i];
        let zeroes: usize = num_lines - ones;
        // println!("[DEBUG] ones: {}, zeroes: {}.", ones, zeroes);
        if ones > zeroes {
            gamma = 2 * gamma + 1;
            epsilon = 2 * epsilon;

        } else if zeroes > ones {
            gamma = 2 * gamma;
            epsilon = 2 * epsilon + 1;
        } else {
            println!("ENDEF: 0 as often as 1 on column {}", i);
        }
    }
    println!("Part 1:");
    println!("Power Consumption = gamma rate ({}) * epsilon rate ({}) = {}", gamma, epsilon, gamma * epsilon);
    /* Part 1: Power Consumption = gamma rate (3004) * epsilon rate (1091) = 3277364 */

    while oxygen_possible.len() > 1 {
        let mut deleted: usize = 0;
        for pos in 0..binary_length {
            // count ones
            let mut ones: usize = 0;
            for line in oxygen_possible {
                if line.chars().nth(pos).unwrap() == '1' {
                    ones += 1;
                }
            }
            // calculate zeroes
            let zeroes: usize = oxygen_possible.len() - ones;
            // println!("[DEBUG] ones: {}, zeroes: {}.", ones, zeroes);
            let mut good = '0';
            if ones >= zeroes {
                good = '1';
            }
            let mut i: usize = 0;
            while i < oxygen_possible.len() {
                let mut line = oxygen_possible.get(i).unwrap().chars();
                if line.nth(pos).unwrap() != good {
                    oxygen_possible.remove(i);
                } else {
                    i += 1;
                }
            }
        }
    }

    let mut cotwo_possible = contents.lines();

    // println!("Part 2:");
    // println!("depth_aimed * forward = {}", depth_aimed * forward);
    /* Part 2: Solution is 1864715580 */
}