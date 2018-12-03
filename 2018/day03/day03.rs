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
    
    /* fabric is the 1000 x 1000 square inch fabric
     * 0 means that the fabric is not claimed yet at this position
     * positive numbers mean this suqareinch is claimed by the claim with this
     * id.
     * negative numbers mean this sqareinch is claimed by the claim with the
     * negative ID and at least one other claim. */
    /* This will allocate a 1000x1000 i32 array, resulting in
     * 1000000*4 bytes memory = 4MB. */
    let mut fabric: [[i32; 1000]; 1000] = [[0;1000];1000];
    let mut claimed: i32 = 0;
    let mut overlapping: Vec<bool> = Vec::new();

    /* each line is "#claimid @ posx,posy: widthxheight" */
    let mut claims_id:     Vec<i32> = Vec::new();
    // let mut claims_posx:   Vec<i32> = Vec::new();
    // let mut claims_posy:   Vec<i32> = Vec::new();
    // let mut claims_width:  Vec<i32> = Vec::new();
    // let mut claims_height: Vec<i32> = Vec::new();

    for line in contents.lines() {
        let mut ol = false;
        let first_split: Vec<&str> = line.split('#').collect();
        let second_split: Vec<&str> = first_split[1].split(" @ ").collect();
        let id: i32 = str::parse(second_split[0]).unwrap();
        let third_split: Vec<&str> = second_split[1].split(",").collect();
        let posx: i32 = str::parse(third_split[0]).unwrap();
        let fourth_split: Vec<&str> = third_split[1].split(": ").collect();
        let posy: i32 = str::parse(fourth_split[0]).unwrap();
        let fifth_split: Vec<&str> = fourth_split[1].split("x").collect();
        let width:i32 = str::parse(fifth_split[0]).unwrap();
        let height:i32 = str::parse(fifth_split[1]).unwrap();
        claims_id.push(id);
        // claims_posx.push(posx);
        // claims_posy.push(posy);
        // claims_width.push(width);
        // claims_height.push(height);

        for x in posx..=posx+width-1 {
            for y in posy..=posy+height-1 {
                let test = fabric[x as usize][y as usize];
                if test == 0 {
                    fabric[x as usize][y as usize] = id;
                } else if test > 0 {
                    // fabric was already claimed
                    fabric[x as usize][y as usize] = -test;
                    claimed += 1;
                    overlapping[(test-1) as usize] = true;
                    ol = true;
                } else {
                    // fabric already was doubly claimed
                    ol = true;
                }
            }
        }
        if ol {
            overlapping.push(true);
        } else {
            // not overlapping (yet)
            overlapping.push(false);
        }
    }

    println!("Square inches of fabric within two or more claims: {}", claimed);
    for i in 0..=overlapping.iter().count()-1 {
        if !overlapping[i] {
            println!("Non-overlapping claim: {}", claims_id[i])
        }
    }
}