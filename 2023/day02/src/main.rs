use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let inputfile = if args.len() < 2 { "input" } else { &args[1] };

    /* read file */
    let contents = fs::read_to_string(inputfile).expect("Something went wrong reading the file");

    let mut sum_of_possible_game_nrs: u32 = 0;
    let mut sum_of_possible_game_powers: u32 = 0;

    /* iterate over lines */
    for line in contents.lines() {
        // Game 1: 5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 19 blue; 1 red, 17 blue
        let mut impossible = false;
        let (game_str, hands_str) = line.trim().split_once(':').unwrap();
        let (_unneeded, game_nr) = game_str.trim().split_once(' ').unwrap();

        let hands = hands_str.trim().split(';');
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for hand in hands {
            let cubes = hand.trim().split(',');
            for cube in cubes {
                let (number, color) = cube.trim().split_once(' ').unwrap();
                if color.trim().eq("red") {
                    let red_hand = number.parse().unwrap();
                    if red_hand > red {
                        red = red_hand;
                    }
                }
                if color.trim().eq("green") {
                    let green_hand = number.parse().unwrap();
                    if green_hand > green {
                        green = green_hand;
                    }
                }
                if color.trim().eq("blue") {
                    let blue_hand = number.parse().unwrap();
                    if blue_hand > blue {
                        blue = blue_hand;
                    }
                }
            }
            if red > 12 || green > 13 || blue > 14 {
                impossible = true;
            }
        }
        if !impossible {
            sum_of_possible_game_nrs += game_nr.parse::<u32>().unwrap();
        }
        sum_of_possible_game_powers += red * green * blue;
    }
    println!("Part 1: Sum of possible game numbers: {}", sum_of_possible_game_nrs);/* 2617 */
    println!(
        "Part 2: Sum of possible game powers: {}",
        sum_of_possible_game_powers
    ); /* 59795 */
}
