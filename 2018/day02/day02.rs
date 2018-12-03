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
    /* result of part 2 = "checksum" */
    //let mut checksum :i32;
    let mut twice :i32 = 0;
    let mut thrice :i32 = 0;
    for line in contents.lines() {
        let mut letters: [u32; 26] = [0; 26];
        let mut hastwice = false;
        let mut hasthrice = false;
        for character in line.chars() {
            letters[character as usize - 97] += 1;
        }
        for number in letters.iter() {
            if *number == 2 {
                hastwice = true;
            } else if *number == 3 {
                hasthrice = true;
            }
        }
        if hastwice {
            twice += 1;
        }
        if hasthrice {
            thrice += 1;
        }
    }
    println!("Checksum (result of part 1): {}", twice * thrice);


    let mut lines = Vec::new();
    for line in contents.lines() {
        lines.push(line);
    }
    let num_lines = lines.len();
    let line_len = lines[0].len();
    println!("[DEBUG]num_lines {}", num_lines);
    for n in 0..=num_lines-1 {
        for m in n+1..=num_lines-1 {
            let mut common :String = String::new();
            let mut differences = 0;
            let mut linea = lines[n].chars();
            let mut lineb = lines[m].chars();
            for chara in linea {
                //println!("{}", lineb.next());
                if chara != lineb.next().unwrap() {
                    differences += 1;
                    if differences > 1 {
                        break;
                    }
                } else {
                    common.push(chara);
                }
            }
            if differences == 1 {
                println!("found the two lines: \n{}\n{}\ncommon: {}", lines[n], lines[m], common);
            }
            if differences > 1 {
                continue;
            }
        }
    }

}