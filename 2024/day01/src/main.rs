use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let inputfile = if args.len() < 2 { "input" } else { &args[1] };

    /* read file */
    let contents = fs::read_to_string(inputfile).expect("Something went wrong reading the file");

    let mut first_list: Vec<i32> = Vec::new();
    let mut second_list: Vec<i32> = Vec::new();
    for line in contents.lines() {
        let mut parts = line.split_whitespace();
        if let (Some(l), Some(r)) = (parts.next(), parts.next()) {
            first_list.push(l.parse().unwrap());
            second_list.push(r.parse().unwrap());
        }
    }

    /* sort lists
      When applicable, unstable sorting is preferred because it is generally
      faster than stable sorting and it doesn’t allocate auxiliary memory.
    */
    first_list.sort_unstable();
    second_list.sort_unstable();
    assert_eq!(first_list.len(), second_list.len());

    let mut total_distance = 0;
    let mut similarity_score = 0;
    for pos_one in 0..first_list.len() {
        let left_number = first_list[pos_one];
        total_distance += (left_number - second_list[pos_one]).abs();
        let mut count = 0;
        for right_number in &second_list {
            if left_number == *right_number {
                count += 1;
            } else if left_number < *right_number {
                break; // can do this because list is sorted
            }
        }
        similarity_score += left_number * count;
    }
    println!(
        "The total distance of the two lists is {} .",
        total_distance
    );
    println!(
        "The similarity score of the two lists is {} .",
        similarity_score
    );
}
