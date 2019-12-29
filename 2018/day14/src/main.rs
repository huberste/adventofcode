use std::env;

/* Advent of Code 2018, Day 14: Chocolate Charts */
fn main() {
    let args: Vec<String> = env::args().collect();
    let input;

    if args.len() < 2 {
        input = 209231;
    } else {
        input = str::parse(&args[1].trim()).unwrap();;
    }

    let mut recipes: Vec<usize> = vec![3, 7];
    let mut scores: Vec<usize> = Vec::new();
    let mut elf1 = 0;
    let mut elf2 = 1;

    /* get vector of the input score for part2 */
    let mut test = input;
    while test > 0 {
        scores.push(test % 10);
        test = test / 10;
    }
    scores.reverse();

    let mut part1 = false;
    let mut part2 = false;

    while !(part1 && part2) {
        let sum = recipes[elf1] + recipes[elf2];
        if sum >= 10 {
            recipes.push(sum/10);
            /* compare last scores */
            if recipes.len() >= scores.len() {
                let mut test = true;
                for i in 0..scores.len() {
                    if recipes[recipes.len() - 1 - i] != scores[scores.len() -1 -i] {
                        test = false;
                        break;
                    }
                }
                if test {
                    part2 = true;
                    println!("Solution Part 2: {}", recipes.len()-scores.len());
                }
            }
            
        }
        recipes.push(sum%10);
        /* compare last scores */
        if recipes.len() >= scores.len() {
            let mut test = true;
            for i in 0..scores.len() {
                if recipes[recipes.len() - 1 - i] != scores[scores.len() -1 -i] {
                    test = false;
                    break;
                }
            }
            if test {
                part2 = true;
                println!("Solution Part 2: {}", recipes.len()-scores.len());
            }
        }
        elf1 = (elf1 + 1 + recipes[elf1]) % recipes.len();
        elf2 = (elf2 + 1 + recipes[elf2]) % recipes.len();

        if recipes.len() >= (input + 10)  && !part1 {
            print!("Solution Part 1: ");
            for i in 0..10 {
                print!("{}", recipes[input + i]);
            }
            println!("");
            part1 = true;
        }
    }

}
