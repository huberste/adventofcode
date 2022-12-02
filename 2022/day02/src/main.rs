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
    /* result of part 1 */
    let mut score :i32 = 0;
    /* result of part 2 */
    let mut score_two :i32 = 0;
    /* iterate over lines of read String */
    for element in contents.lines() {
        /* A Y */
        /* A,X=Rock(1), B,Y=Paper(2), C,Z=Scissors(3) */
        let mut split = element.split_whitespace();
        let elf_play = split.next().unwrap();
        let my_response = split.next().unwrap();
        if my_response == "X" {
            score += 1;
            score_two += 0;
            if elf_play == "A" {
                score += 3; /* draw */
                score_two += 3; /* lose with scissors */
            } else if elf_play == "B" {
                score += 0; /* lost */
                score_two += 1; /* lose with rock */
            } else if elf_play == "C" {
                score += 6; /* won */
                score_two += 2; /* lose with paper */
            }
        } else if my_response == "Y" {
            score += 2;
            score_two += 3;
            if elf_play == "A" {
                score += 6; /* win */
                score_two += 1; /* draw with rock */
            } else if elf_play == "B" {
                score += 3; /* draw */
                score_two += 2; /* draw with paper */
            } else if elf_play == "C" {
                score += 0; /* lost */
                score_two += 3; /* draw with scissors */
            }
        } else if my_response == "Z" {
            score += 3;
            score_two += 6;
            if elf_play == "A" {
                score += 0; /* lose */
                score_two += 2; /* win with paper */
            } else if elf_play == "B" {
                score += 6; /* win */
                score_two += 3; /* win with scissors */
            } else if elf_play == "C" {
                score += 3; /* draw */
                score_two += 1; /* win with rock */
            }
        }
    }

    println!("Part 1:");
    println!("What would your total score be if everything goes exactly according to your strategy guide?");
    println!("My total score would be {}.", score);
    /* Part 1: My solution is 8392 (15 for simple) */
    println!("Part 2:");
    println!("What would your total score be if everything goes exactly according to your strategy guide?");
    println!("My total score would be {}.", score_two);
    /*Part 2: My solution is 10116 (12 for simple) */
}