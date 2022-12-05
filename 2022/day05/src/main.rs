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

    let mut stacks: Vec<Vec<char>> = Vec::new();

    let mut lines = contents.lines();
    let mut created_vec = false;
    let mut read_crates = true;
    while read_crates {
        let line = lines.next().unwrap();
        if !created_vec {
            stacks = vec![Vec::new(); (line.len() + 1) / 4];
            created_vec = true;
        }
        if line.contains("1") {
            read_crates = false;
            assert_eq!(lines.next().unwrap(), "");
            continue;
        }
        let mut index = 0;
        let mut items = line.chars();
        let mut item = items.next();
        while !item.is_none() {
            // assert_eq!(item.unwrap(), ' ', "asdf");
            let var: char = items.next().unwrap();
            if var != ' ' {
                stacks[index].insert(0, var);
            }
            // assert_eq!(items.next().unwrap(), ' ', "ghjk");
            items.next();
            items.next();
            item = items.next();
            index += 1;
        }
    }
    let mut stacks_two = stacks.clone();

    for line in lines {
        /* each line is a rearrangement like this:
           move 1 from 2 to 1 */
        let mut split = line.split(" ");
        split.next();
        let count: usize = split.next().unwrap().parse().unwrap();
        split.next();
        let from: usize = split.next().unwrap().parse().unwrap();
        split.next();
        let to: usize = split.next().unwrap().parse().unwrap();
        let mut index = 0;
        while index < count {
            let item = stacks[from - 1].pop().unwrap();
            stacks[to - 1].push(item);
            index += 1;
        }
        let start = stacks_two[from - 1].len() - count;
        let mut slice = stacks_two[from - 1].split_off(start);
        stacks_two[to - 1].append(&mut slice);
    }

    
    println!("After the rearrangement procedure completes, what crate ends up on top of each stack?");
    println!("Part 1: The StackMover 9000");
    for stack in stacks {
        print!("{}", stack.last().unwrap());
    }
    println!();
    /* Part 1: My solution is CFFHVVHNC (CMZ for simple) */
    println!("Part 2: The StackMover 9001");
    for stack in stacks_two {
        print!("{}", stack.last().unwrap());
    }
    println!();
    /* Part 2: My solution is FSZWBPTBG (MCD for simple) */
}