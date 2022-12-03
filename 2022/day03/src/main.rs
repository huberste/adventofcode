use std::env;
use std::fs;

fn find_item_in_two(first: &str, second: &str) -> char {
    for char_a in first.chars() {
        for char_b in second.chars() {
            if char_a == char_b {
                return char_a;
            }
        }
    }
    return 0 as char;
}

fn find_items_in_two(first: &str, second: &str) -> String {
    let mut result: Vec<char> = Vec::new();
    for char_a in first.chars() {
        for char_b in second.chars() {
            if char_a == char_b {
                result.push(char_a);
            }
        }
    }
    return result.iter().collect();
}

fn find_item_in_three(first: &str, second: &str, third: &str) -> char {
    let double = find_items_in_two(first, second);
    return find_item_in_two(&double, third);
}

fn priority(item: char) -> u32 {
    if item.is_ascii_lowercase() {
        return item as u32 - 97 + 1;
    } else if item.is_ascii_uppercase() {
        return item as u32 - 65 + 1 + 26;
    }
    return 0;
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

    let mut sum_of_priorities :u32 = 0; // result of part 1
    let mut sum_of_priorities_two :u32 = 0; // result of part 2
    let mut first_elf = "";
    let mut second_elf = "";
    let mut third_elf = "";
    let mut elf = 0;

    /* iterate over lines of read String */
    for element in contents.lines() {
        if elf % 3 == 0 {
            first_elf = element;
        }
        if elf % 3 == 1 {
            second_elf = element;
        }
        if elf % 3 == 2 {
            third_elf = element;
        }
        let number_of_items = element.len();
        let first_compartment = element.get(..number_of_items/2).unwrap();
        let second_compartment = element.get(number_of_items/2..).unwrap();
        let common = find_item_in_two(first_compartment, second_compartment);
        sum_of_priorities += priority(common);
        if elf % 3 == 2 {
            /* find common char in all three elf lines */
            let common = find_item_in_three(first_elf, second_elf, third_elf);
            /* add priority of this char to sum_of_priorities_two */
            sum_of_priorities_two += priority(common);
        }
        elf += 1;
    }
    println!("Part 1:");
    println!("What is the sum of the priorities of those item types?");
    println!("The sum of the priorities of those items is {}.", sum_of_priorities);
    // Part 1: My solution is 7766 (157 for simple)
    println!("Part 2:");
    println!("What is the sum of the priorities of those badge item types?");
    println!("The sum of the priorities of those badge items is {}.", sum_of_priorities_two);
    // Part 2: My solution is 2415 (70 for simple)
}