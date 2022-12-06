use std::env;
use std::fs;

/*
--- Day 6: Tuning Trouble ---
*/

/*
  returns true if the first `len` char of `chars` are different.
  XXX: This can probably be done *way* faster.
*/ 
fn different(chars: &Vec<char>, len: usize) -> bool {
    let mut pos = 0;
    while pos < len {
        let mut pos_two = pos + 1;
        while pos_two < len {
            if chars[pos] == chars[pos_two] {
                return false;
            }
            pos_two += 1;
        }
        pos += 1;
    }
    return true;
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
    /* it's single line input this day */
    let contents = fs::read_to_string(inputfile)
        .expect("Something went wrong reading the file");

    let symbols: Vec<char> = contents.chars().collect();

    let mut pos: usize = 0;

    /* I could probably work with slices of the Vec<char> which would be way
       more memory efficient. */
    let mut packet_marker: Vec<char> = Vec::new();
    let len_packet_marker = 4;
    let mut find_packet = true;

    let mut message_marker: Vec<char> = Vec::new();
    let len_message_marker = 14;
    let mut find_message = true; /* not needed this day. Probably in future puzzles? */

    /* iterate over chars */
    while pos < symbols.len() {
        packet_marker.push(symbols[pos]);
        if packet_marker.len() > len_packet_marker {
            packet_marker.remove(0);
        }
        message_marker.push(symbols[pos]);
        if message_marker.len() > len_message_marker {
            message_marker.remove(0);
        }
        if find_packet && packet_marker.len() == 4 {
            if different(&packet_marker, len_packet_marker) {
                println!("Part 1: How many characters need to be processed before the first start-of-packet marker is detected?");
                println!("{}", pos + 1);
                /* Part 1: My solution is 1109 (7 for simple) */
                find_packet = false;
            }
        }
        if find_message && message_marker.len() == len_message_marker {
            if different(&message_marker, len_message_marker) {
                println!("Part 2: How many characters need to be processed before the first start-of-message marker is detected?");
                println!("{}", pos + 1);
                /* Part 2: My solution is 3965 (19 for simple) */
                find_message = false; /* not needed, because break directly after! */
                break;
            }
        }
        pos += 1;
    }

}