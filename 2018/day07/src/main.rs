use std::collections::HashSet;
use std::collections::HashMap;
use std::env;
use std::fs;

/* Advent of Code 2018, Day 07: The Sum of Its Parts */
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

    /* input is list of point coordinates in "x,y" style */
    let mut instructions: Vec<(char, char)> = Vec::new();
    for line in contents.lines() {
        let split_1: Vec<&str> = line.split("Step ").collect();
        let split_2: Vec<&str> = split_1[1].split(" must be finished before step ").collect();
        let before = split_2[0].chars().next().unwrap();
        let split_3: Vec<&str> = split_2[1].split(" can begin.").collect();
        let after = split_3[0].chars().next().unwrap();
        instructions.push((before, after));
        //println!("{} -> {}", before, after);
    }

    /* get which instructions are there */
    let mut steps: HashSet<char> = HashSet::new();
    for (before, after) in &instructions {
        steps.insert(*before);
        steps.insert(*after);
    }

    let mut available: HashSet<char> = HashSet::new();

    for step in &steps {
        available.insert(*step);
    }

    let mut done: Vec<char> = Vec::new();
    let length = steps.len();

    /* big while loop */
    while done.len() < length {
        /* in every loop check every step */
        //let mut ready: Vec<char> = Vec::new();
        let mut canbedone: Vec<char> = Vec::new();
        for step in &steps {
            if done.contains(step) {
                continue;
            }
            let mut test = true;
            for (before, after) in &instructions {
                if *step == *after {
                    if !done.contains(&before) {
                        test = false;
                    }
                }
            }
            if test {
                canbedone.push(*step);
            }
        }
        canbedone.sort();
        done.push(canbedone[0]);
    }

    print!("instruction order: ");
    for step in done {
        print!("{}", step);
    }
    println!("");

    done = Vec::new();
    let mut doing = HashMap::new(); /* (step, time_left) */
    let mut working = 0;
    let mut seconds: i32 = 0;
    let workers = 5;
    /* big while loop */
    while done.len() < length {
        /* in every loop check every step */
        //let mut ready: Vec<char> = Vec::new();
        let mut doing_new = HashMap::new();
        for (key, value) in &doing {
            if *value == 0 {
                //ready.push(*key);
                done.push(*key);
                working -= 1;
            } else {
                doing_new.insert(*key, *value-1);
            }
        }
        doing = doing_new;
        let mut canbedone: Vec<char> = Vec::new();
        for step in &steps {
            if done.contains(step) {
                continue;
            }
            if doing.contains_key(step) {
                continue;
            }
            let mut test = true;
            for (before, after) in &instructions {
                if *step == *after {
                    if !done.contains(&before) {
                        test = false;
                    }
                }
            }
            if test {
                canbedone.push(*step);
            }
        }
        canbedone.sort();
        let mut i = 0;
        while canbedone.len() > i && working < workers {
            doing.insert(canbedone[i], 60+canbedone[i] as u32 - 65);
            working += 1;
            i+=1
        }

        seconds += 1;

    }

    println!("{}", seconds-1);

}
