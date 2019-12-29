use std::collections::VecDeque;
use std::env;
use std::fs;

/* Advent of Code 2018, Day 09: Marble Mania */
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

    let split_1: Vec<&str> = contents.split(" players; last marble is worth ").collect();
    let players: u32 = str::parse(split_1[0]).unwrap();
    let split_2: Vec<&str> = split_1[1].split(" points").collect();
    let last_marble: u32 = str::parse(split_2[0]).unwrap();

    /* game preparation */
    /* VecDeque is about twice as fast for long collections, because it has
     * O(min(i,n-i)).
     * This could be solved by many adjacent LinkedLists, which would
     * probably be *way* faster, but more work to implement.
     * The problem is Insert / Deletion in the "middle" of the large VecDeque */
    let mut marbles: VecDeque<u32> = VecDeque::with_capacity(last_marble as usize * 100); /* circle of the marbles: clockwise is index++, ccw is index-- */
    let mut scores: Vec<u32> = vec![0; players as usize]; /* scores[i] = score of player i*/
    let mut current_marble = 0; /* current marble */
    let mut current_marble_index = 0;
    let mut current_player = 0;
    marbles.push_back(current_marble);
    let mut marbles_length = 1;

    /* game starts */
    while current_marble < last_marble * 100 {
        current_marble += 1;
        current_player = (current_player + 1) % players;

        if current_marble % 23 == 0 {
            scores[current_player as usize] += current_marble;
            current_marble_index = (current_marble_index + marbles_length - 7) % marbles_length;
            scores[current_player as usize] += marbles[current_marble_index];
            marbles.remove(current_marble_index);
            marbles_length -= 1;
        } else {
            /* insert next marble */
            current_marble_index = (current_marble_index + 2) % marbles_length;
            /* insert at last index, not 0 (would not change outcome, but looks better that way and is faster) */
            if current_marble_index == 0 { current_marble_index = marbles_length;}
            marbles.insert(current_marble_index, current_marble);
            marbles_length += 1;
        }
        // print!("[{}] ", current_marble);
        // for i in 0..marbles_length {
        //     if i == current_marble_index {print!("(")}
        //     print!("{}", marbles[i]);
        //     if i == current_marble_index {print!(")")}
        //     print!(" ");
        // }
        // println!("");
        if current_marble % 70848 == 0 { println!("current marble: {} of {}", current_marble, last_marble * 100); }
    }

    /* find max score */
    let mut max = 0;
    for score in scores {
        if score > max {
            max = score;
        }
    }

    println!("Part 1: Winning Elf's score: {}", max);
}
