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
    const WINDOW_SIZE: usize = 3;
    let mut window: [i32; WINDOW_SIZE] = [666; WINDOW_SIZE]; /* very large number */
    /* result of part 1 */
    let mut counter_part1 :i32 = 0;
    let mut counter_part2 :i32 = 0;
    /* iterate over lines of read String */
    for element in contents.lines() {
        let curval: i32 = element.trim().parse().expect("Not a number!");
        if curval > window[WINDOW_SIZE-1] {
            /* println!("{} is larger than {}", curval, window[WINDOW_SIZE - 1]); */
            counter_part1 += 1;
        }
        let mut sum :i32 = 0;
        let mut sum2 :i32 = 0;
        for i in 0..WINDOW_SIZE-1 {
            sum += window[i];
            window[i] = window[i+1];
            sum2 += window[i];
        }
        sum += window[WINDOW_SIZE-1];
        window[WINDOW_SIZE-1] = curval;
        sum2 += window[WINDOW_SIZE-1];
        if sum2 > sum {
            /* println!("{} is larger than {}", sum2, sum); */
            counter_part2 += 1;
        }
    }
    println!("Part 1:");
    println!("How many measurements are larger than the previous measurement?");
    println!("{} measurements are larger than the previous measurement.", counter_part1);
    /* Part 1: Solution is 1400 */
    println!("Part 2:");
    println!("How many sums are larger than the previous sum?");
    println!("{} sums are larger than the previous sum.", counter_part2);
    /* Part 2: Solution is 1400 */
}