use std::env;
use std::fs;

fn find_first_number(line: String, numbers: Vec<&str>) -> u32 {
    // replace words with numbers
    let mut newline = line.clone();
    let mut replaced = ""; // number to be replaced
    let mut replace_pos = std::usize::MAX; // position of number to be replaced

    // search first occurence of written number
    for number in &numbers {
        let found = line.find(number);
        if found.is_some() {
            let pos = found.unwrap();
            if pos < replace_pos {
                replace_pos = pos;
                replaced = number;
            }
        }
    }
    // if at least one number was found
    if replace_pos < std::usize::MAX {
        // replace written number with it's position in the numbers vector
        // which is incidentally it's digit
        newline = newline.replace(
            replaced,
            &numbers
                .iter()
                .position(|&r| r == replaced)
                .unwrap()
                .to_string(),
        );
    }

    // find first number
    for c in newline.chars() {
        if c.is_ascii_digit() {
            return c.to_digit(10).unwrap();
        }
    }
    0
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let inputfile = if args.len() < 2 { "input" } else { &args[1] };

    /* read file */
    let contents = fs::read_to_string(inputfile).expect("Something went wrong reading the file");

    let mut sum: u32 = 0;

    /* iterate over lines */
    for element in contents.lines() {
        let mut first: u32 = 0;
        let mut last: u32 = 0;
        let mut found_first: bool = false;
        for c in element.chars() {
            if c.is_ascii_digit() {
                if !found_first {
                    first = c.to_digit(10).unwrap();
                    found_first = true;
                }
                last = c.to_digit(10).unwrap();
            }
        }
        sum = sum + (10 * first) + last;
    }

    println!("Part 1:");
    println!("What is the sum of all of the calibration values?");
    println!("The sum of all calibration values is {} .", sum);
    /* Part 1: Solution is 54450 (142 for example) */

    sum = 0;
    /* iterate over lines */
    for element in contents.lines() {
        let line = element.to_string();

        /* forward search for written out numbers */
        let numbers = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ];
        let first = find_first_number(line.clone(), numbers.to_vec());

        /* backward search */
        let reverse_numbers = [
            "orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin",
        ];
        let last = find_first_number(line.chars().rev().collect(), reverse_numbers.to_vec());

        sum = sum + (10 * first) + last;
    }

    println!("Part 2:");
    println!("What is the sum of all of the calibration values?");
    println!("The sum of all the calibration values is {} .", sum);
    /*Part 2: Solution is 54265 (281 for example) */
}
