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
    let mut calories :i32 = 0;
    /* result of part 1 */
    let mut top_one_calories :i32 = 0;
    /* result of part 2 */
    let mut top_two_calories :i32 = 0;
    let mut top_three_calories :i32 = 0;
    let mut temp :i32;
    /* iterate over lines of read String */
    for element in contents.lines() {
        if element == "" {
            if calories > top_one_calories {
                temp = top_one_calories;
                top_one_calories = calories;
                calories = temp;
            }
            if calories > top_two_calories {
                temp = top_two_calories;
                top_two_calories = calories;
                calories = temp;
            }
            if calories > top_three_calories {
                top_three_calories = calories;
            }
            calories = 0;
        } else {
        let curval: i32 = element.trim().parse().expect("Not a number!");
            calories += curval;
        }
    }
    /* last elf is not delimited by empty line */
    if calories > top_one_calories {
        temp = top_one_calories;
        top_one_calories = calories;
        calories = temp;
    }
    if calories > top_two_calories {
        temp = top_two_calories;
        top_two_calories = calories;
        calories = temp;
    }
    if calories > top_three_calories {
        top_three_calories = calories;
    }

    println!("Part 1:");
    println!("How many total Calories is the Elf carrying the most Calories carrying?");
    println!("The Elf carrying the most Calories is carrying {} Calories.", top_one_calories);
    /* Part 1: Solution is 69836 (24000 for simple) */
    println!("Part 2:");
    println!("How many total Calories are the three Elves carrying the most Calories carrying?");
    println!("The Three Elves carrying the most Calories are carrying {} Calories.", top_one_calories + top_two_calories + top_three_calories);
    /*Part 2: Solution is 207968 (45000 for simple) */
}