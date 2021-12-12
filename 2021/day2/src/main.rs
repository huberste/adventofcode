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
    let mut depth: i64 = 0;
    let mut depth_aimed: i64 = 0;
    let mut forward: i64 = 0;
    let mut aim: i64 = 0;
    /* iterate over lines of read String */
    for line in contents.lines() {
        let mut split = line.split_whitespace();
        /* All Input is evil!
         * I should make some sanity checks here. 
         * Maybe some pattern matching would be the right way? */
        /* Also, unwrap() might panic. This is bad. */
        let instruction = split.next().unwrap();
        let arg: i64 = split.next().unwrap().trim().parse().expect("Not a number!");
        if instruction == "down" {
            depth += arg;
            aim += arg;
        } else if instruction == "up" {
            depth -= arg;
            aim -= arg;
        } else if instruction == "forward" {
            forward += arg;
            depth_aimed = depth_aimed + arg * aim;
        }
    }
    println!("Part 1:");
    println!("depth * forward = {}", depth * forward);
    /* Part 1: Solution is 2215080 */
    println!("Part 2:");
    println!("depth_aimed * forward = {}", depth_aimed * forward);
    /* Part 2: Solution is 1864715580 */
}