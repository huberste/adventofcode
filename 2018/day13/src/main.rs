use std::env;
use std::fs;

/* Advent of Code 2018, Day 13: Mine Cart Madness */
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

    let up = 0;
    let right = 1;
    let down = 2;
    let left = 3;

    let turn_left = 0;
    let turn_straight = 1;
    let turn_right = 2;

    let mut carts: Vec<(usize, usize, u32, u32)> = Vec::new(); // X, Y, direction, decision
    let mut rails: Vec<Vec<char>> = Vec::new();
    let mut y = 0;
    for line in contents.lines() {
        let mut chars: Vec<char> = Vec::new();
        let mut x = 0;
        for chrr in line.chars() {
            if chrr == 'v' {
                carts.push((x,y,down,turn_left));
                chars.push('|');
            } else if chrr == '^' {
                carts.push((x,y,up
        ,turn_left));
                chars.push('|');
            } else if chrr == '<' {
                carts.push((x,y,left,turn_left));
                chars.push('-');
            } else if chrr == '>' {
                carts.push((x,y,right,turn_left));
                chars.push('-');
            } else {
                chars.push(chrr);
            }
            x += 1;
        }
        rails.push(chars);
        y += 1;
    }

    let height = rails.len();
    let width = rails[0].len();

    /* print tick 0 */
    /*
    for y in 0..height {
        for x in 0..width {
            let mut chrr = rails[y][x];
            for cart in &carts {
                if cart.0 == x && cart.1 == y {
                    if cart.2 == up { chrr = '^'; }
                    else if cart.2 == left {chrr = '<';}
                    else if cart.2 == down {chrr = 'v';}
                    else if cart.2 == right {chrr = '>';}
                }
            }
            print!("{}", chrr);
        }
        println!("");
    }
    */

    let mut collision = false;
    let mut tick = 0;
    while carts.len() > 1 {
        // Sort cars so the move from the upperleftmost first
        carts.sort_by(|a, b| a.0.cmp(&b.0));
        carts.sort_by(|a, b| a.1.cmp(&b.1));
        let mut num_carts = carts.len();
        let mut i: i32 = 0;
        while i < num_carts as i32 {
            //println!("[DEBUG]cart{}: {},{}", i, carts[i as usize].0, carts[i as usize].1);
            let mut x = 0;
            let mut y = 0;
            if carts[i as usize].2 == up {
                x = carts[i as usize].0;
                y = carts[i as usize].1-1;
            } else if carts[i as usize].2 == right {
                x = carts[i as usize].0+1;
                y = carts[i as usize].1;
            } else if carts[i as usize].2 == down {
                x = carts[i as usize].0;
                y = carts[i as usize].1+1;
            } else if carts[i as usize].2 == left {
                x = carts[i as usize].0-1;
                y = carts[i as usize].1;
            }
            if rails[y][x] == '\\' {
                if carts[i as usize].2 == up {
                    carts[i as usize].2 = left;
                } else if carts[i as usize].2 == right {
                    carts[i as usize].2 = down;
                } else if carts[i as usize].2 == down {
                    carts[i as usize].2 = right;
                } else if carts[i as usize].2 == left {
                    carts[i as usize].2 = up;
                }
            } else if rails[y][x] == '/' {
                if carts[i as usize].2 == up {
                    carts[i as usize].2 = right;
                } else if carts[i as usize].2 == right {
                    carts[i as usize].2 = up;
                } else if carts[i as usize].2 == down {
                    carts[i as usize].2 = left;
                } else if carts[i as usize].2 == left {
                    carts[i as usize].2 = down;
                }
            } else if rails[y][x] == '+' {
                if carts[i as usize].3 == turn_left {
                    carts[i as usize].2 = (carts[i as usize].2 + 3) % 4;
                } else if carts[i as usize].3 == turn_right {
                    carts[i as usize].2 = (carts[i as usize].2 + 1) % 4;
                }
                carts[i as usize].3 = (carts[i as usize].3 + 1) % 3;
            }
            carts[i as usize].0 = x;
            carts[i as usize].1 = y;
            // check for collisions
            let mut j = 0;
            while j < num_carts {
                if i == j as i32 { j += 1; continue; }
                if carts[i as usize].0 == carts[j].0 && carts[i as usize].1 == carts[j].1 {
                    if !collision {
                        println!("First Collision: {},{}", x, y);
                    }
                    collision = true;
                    if i < j as i32 {
                        carts.remove(j);
                        carts.remove(i as usize);
                    } else {
                        carts.remove(i as usize);
                        carts.remove(j);
                    }
                    num_carts = num_carts - 2;
                    if i > j as i32 { i -= 1; }
                    i -= 1;
                    break;
                }
                j += 1;
            }
            i += 1;
        }
        tick += 1;
        /*
        println!("tick: {}", tick);
        for y in 0..height {
            for x in 0..width {
                let mut chrr = rails[y][x];
                for cart in &carts {
                    if cart.0 == x && cart.1 == y {
                        if cart.2 == up { chrr = '^'; }
                        else if cart.2 == left {chrr = '<';}
                        else if cart.2 == down {chrr = 'v';}
                        else if cart.2 == right {chrr = '>';}
                    }
                }
                print!("{}", chrr);
            }
            println!("");
        }
        */
    }
    if carts.len() > 0 {
        println!("last cart: {},{}", carts[0].0, carts[0].1);
    }
}
