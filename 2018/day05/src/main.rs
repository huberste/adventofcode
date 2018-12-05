use std::collections::HashMap;
use std::env;
use std::fs;

fn collapse(mut units: Vec<char>) -> Vec<char> {
    let mut destroyed = true;
    while destroyed {
        destroyed = false;
        let mut length = units.len();
        let mut i:i32 = 0;
        while i < (length-1) as i32 {
            if units[i as usize].is_uppercase() {
                if units[i as usize].to_ascii_lowercase() == units[(i+1) as usize] {
                    //println!("[DEBUG]destroying {}{}", units[i as usize], units[(i+1) as usize]);
                    units.remove(i as usize);
                    units.remove(i as usize);
                    //println!("[DEBUG]length before removing: {}", length);
                    length -= 2;
                    destroyed = true;
                    if i > 1 {
                        i -= 2;
                    } else {
                        i -= 1;
                    }
                }
            } else { // not uppercase -> lower case!
                if units[i as usize].to_ascii_uppercase() == units[(i+1) as usize] {
                    //println!("[DEBUG]destroying {}{}", units[i as usize], units[(i+1) as usize]);
                    units.remove(i as usize);
                    units.remove(i as usize);
                    //println!("[DEBUG]length before removing: {}", length);
                    length -= 2;
                    destroyed = true;
                    if i > 1 {
                        i -= 2;
                    } else {
                        i -= 1;
                    }
                }
            }
            i+=1;
        }
    }
    return units;
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
    let contents = fs::read_to_string(inputfile)
        .expect("Something went wrong reading the file");
    
    /* input is one line of "polymer" */
    
    // part 1
    let mut units: Vec<char> = Vec::new();
    for char in contents.chars() {
        units.push(char);
    }

    units = collapse(units);
    println!("remaining units: {}", units.len()-1); // newline at the end of input...

    // part 2
    print!("calculating, please stand by");
    let mut polymers: HashMap<char, usize> = HashMap::new();
    for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".chars() {
        let mut units: Vec<char> = Vec::new();
            for char in contents.chars() {
            units.push(char);
        }
        let mut length = units.len();
        let mut i:i32 = 0;
        while i < (length-1) as i32 {
            if units[i as usize] == character {
                units.remove(i as usize);
                length -= 1;
                i -= 1;
            } else if units[i as usize] == character.to_ascii_lowercase() {
                units.remove(i as usize);
                length -= 1;
                i -= 1;
            }
            i += 1;
        }
        units = collapse(units);
        polymers.insert(character, units.len());
        print!(".");
    }
    println!("");
    let mut min: usize = 50000; // inputlength
    let mut minunit: char = ' ';
    for (key, value) in polymers {
        if value < min {
            minunit = key;
            min = value;
        }
    }
    println!("smallest length of polymer without unit {}: {}", minunit, min -1); // again, the newline at the end!

}