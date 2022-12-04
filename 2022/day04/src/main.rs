use std::env;
use std::fs;

fn fully_contains(first_begin: u32, first_end: u32,
                  second_begin: u32, second_end: u32) -> bool {
    if first_begin <= second_begin && first_end >= second_end {
        return true;
    } else if first_begin >= second_begin && first_end <= second_end {
        return true;
    }
    return false;
}

fn overlaps(first_begin: u32, first_end: u32,
            second_begin: u32, second_end: u32) -> bool {
    if first_begin <= second_begin && second_begin <= first_end {
        return true;
    } else if second_begin <= first_begin && first_begin <= second_end {
        return true;
    }
    return false;
}

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

    let mut contained_pairs :u32 = 0; // result of part 1
    let mut overlapping_pairs :u32 = 0; // result of part 1

    /* iterate over lines of read String */
    for element in contents.lines() {
        let mut elves = element.split(",");
        let mut elf_one = elves.next().unwrap().split("-");
        let elf_one_begin :u32 = elf_one.next().unwrap().parse().unwrap();
        let elf_one_end :u32 = elf_one.next().unwrap().parse().unwrap();
        let mut elf_two = elves.next().unwrap().split("-");
        let elf_two_begin :u32 = elf_two.next().unwrap().parse().unwrap();
        let elf_two_end :u32 = elf_two.next().unwrap().parse().unwrap();
        if fully_contains(elf_one_begin, elf_one_end, elf_two_begin, elf_two_end) {
            contained_pairs += 1;
        }
        if overlaps(elf_one_begin, elf_one_end, elf_two_begin, elf_two_end) {
            overlapping_pairs += 1;
        }
    }
    println!("Part 1:");
    println!("In how many assignment pairs does one range fully contain the other?");
    println!("{} pairs.", contained_pairs);
    /* Part 1: My solution is 464 (2 for simple) */
    println!("Part 2:");
    println!("In how many assignment pairs do the ranges overlap?");
    println!("{} pairs.", overlapping_pairs);
    /* Part 2: My solution is 770 (4 for simple) */
}