use std::env;
use std::fs;

#[derive(Debug)]
struct PartNumber {
    y: usize,
    start_x: usize,
    end_x: usize,
    number: u32,
}

fn is_symbol(input: char) -> bool{
    if input.is_ascii_digit() {
        return false
    } else if input == '.' {
        return false
    }
    true
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let inputfile = if args.len() < 2 { "input" } else { &args[1] };

    // read file
    let contents = fs::read_to_string(inputfile).expect("Something went wrong reading the file");

    let mut schematic: Vec<Vec<char>> = vec![];

    // iterate over lines
    for line in contents.lines() {
        schematic.push(line.chars().collect());
    }

    let mut sum_of_part_numbers = 0;
    let mut part_numbers: Vec<PartNumber> = vec![];
    let mut sum_of_gear_ratios = 0;

    let mut y = 0;
    while y < schematic.len() {
        let mut x = 0;
        let mut num_start = 0;
        let mut part_number = 0;
        while x < (&schematic[0]).len() {
            let is_digit = schematic[y][x].is_digit(10);
            if is_digit {
                part_number *= 10;
                part_number += schematic[y][x].to_digit(10).unwrap();
            }
            if x == (&schematic[0]).len() -1 || !is_digit {
                if part_number > 0 {
                    // part_number is from num_start til x-1
                    part_numbers.push(PartNumber { y: y, start_x: num_start, end_x: x-1, number: part_number });
                    // check it there is symbol left to part number
                    let start_x = if num_start > 0 { num_start - 1 } else {num_start};
                    let end_x = if x >= (&schematic[y]).len() -1 { x } else {x+1};
                    let start_y = if y > 0 { y - 1 } else {y};
                    let end_y = if y >= schematic.len() -1 { y } else {y+1};
                    'test: for i in start_x..end_x {
                        for j in start_y..=end_y {
                            if is_symbol(schematic[j][i]) {
                                sum_of_part_numbers += part_number;
                                break 'test;
                            }
                        }
                    }
                }
                num_start = x+1;
                part_number = 0;
            }
            x += 1;
        } // while x
        y += 1;
    } // while y

    println!("The sum of all part numbers is {} .", sum_of_part_numbers); //467835

    let mut y = 0;
    while y < schematic.len() {
        let mut x = 0;
        while x < (&schematic[0]).len() {
            if schematic[y][x]== '*' {
                let mut adjacent_parts: usize = 0;
                let mut gear_ratio = 1;
                for part in &part_numbers {
                    let start_x = if part.start_x > 0 { part.start_x - 1 } else {part.start_x};
                    let end_x = if part.end_x < schematic[y].len()-1 { part.end_x + 1 } else {part.end_x};
                    let start_y = if part.y > 0 { part.y - 1 } else {part.y};
                    let end_y = if part.y < schematic.len() -1 { part.y + 1 } else {part.y};
                    if start_y <= y && y <= end_y {
                        if start_x <= x && x <= end_x {
                            adjacent_parts += 1;
                            gear_ratio *= part.number;
                            if adjacent_parts > 2 {
                                break;
                            }
                        }
                    }
                }
                if adjacent_parts == 2 {
                    sum_of_gear_ratios += gear_ratio;
                }
            }
            x += 1;
        } // while x
        y += 1;
    } // while y

    println!("The sum of all of the gear ratios is {} .", sum_of_gear_ratios); // example: 467835

    

}
