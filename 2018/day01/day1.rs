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
    /* result of part 1 = "frequency" = sum of all values */
    let mut frequency :i32 = 0;
    let mut vec = Vec::new();
    vec.push(frequency);
    let mut found_twice :bool = false;
    let mut iterated_once :bool = false;
    /* iterate over lines of read String */
    while !found_twice {
        for element in contents.lines() {
            let number: i32 = element.trim().parse().expect("Not a number!");
            frequency += number;
            //println!("Frequency right now: {}", frequency);
            if !found_twice {
                for x in &vec {
                    //println!("frequency: {}", x);
                    if frequency == *x {
                        found_twice = true;
                        println!("First frequency to be reached twice (solution for part 2): {}", frequency);
                    }
                }
                vec.push(frequency);
            }
        }
        if !iterated_once {
            iterated_once = true;
            println!("Frequency after one iteration (solution for part 1): {}", frequency);
        }

        //println!("iterated");
    }


}