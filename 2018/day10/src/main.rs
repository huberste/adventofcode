use std::env;
use std::fs;

/* Advent of Code 2018, Day 09: The Stars Align */
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

    let mut points: Vec<(i64, i64, i64, i64)> = Vec::new(); /* posx, posy, velx, vely */
    for line in contents.lines() {
        let split_1: Vec<&str> = line.split("<").collect();
        let split_2: Vec<&str> = split_1[1].split(">").collect();
        let split_3: Vec<&str> = split_2[0].split(",").collect();
        // println!("[DEBUG]posx: \"{}\"", split_3[0]);
        let posx: i64 = str::parse(split_3[0].trim()).unwrap();
        // println!("[DEBUG]posy: \"{}\"", split_3[1]);
        let posy: i64 = str::parse(split_3[1].trim()).unwrap();
        let split_4: Vec<&str> = split_1[2].split(">").collect();
        let split_5: Vec<&str> = split_4[0].split(",").collect();
        // println!("[DEBUG]posx: \"{}\"", split_5[0]);
        let velx: i64 = str::parse(split_5[0].trim()).unwrap();
        // println!("[DEBUG]posx: \"{}\"", split_5[1]);
        let vely: i64 = str::parse(split_5[1].trim()).unwrap();
        // println!("[DEBUG] adding point ({},{}->{},{})", posx, posy, velx, vely);
        points.push((posx, posy, velx, vely));
    }

    /* the values we want are probably around when the summed up distance is pretty low */
    let mut condition = true;
    let mut last_distance = std::i64::MAX; /* Thats 2^63-1. Thats a lot. */
    let mut loop_counter = 0;
    while condition {
        /* advance stars */
        for i in 0..points.len() {
            points[i].0 = points[i].0 + points[i].2;
            points[i].1 = points[i].1 + points[i].3;
        }
        /* calculate distances */
        /* with my input this yields the same result as the calculation of the
         * least y-height, though the latter is much faster to calculate!
         */
        /*
        let mut sum = 0;
        for i in 0..points.len() {
            for j in i+1..points.len() {
                sum += (points[i].0 - points[j].0).abs();
                sum += (points[i].1 - points[j].1).abs();
            }
        }
        if sum > last_distance {
            condition = false;
        } else {
            last_distance = sum;
        }
        */

        let mut posy_min = std::i64::MAX;
        let mut posy_max = std::i64::MIN;
        for point in &points {
            if point.1 < posy_min {posy_min = point.1;}
            if point.1 > posy_max {posy_max = point.1;}
        }
        let distance = posy_max - posy_min;

        if distance > last_distance {
            condition = false;
        } else {
            last_distance = distance;
        }

        loop_counter += 1;
    }

    /* jump back 5 steps */
    for i in 0..points.len() {
        points[i].0 = points[i].0 + points[i].2 * -3;
        points[i].1 = points[i].1 + points[i].3 * -3;
    }
    loop_counter += -3;

    for _i in 1..4 {
        for i in 0..points.len() {
            points[i].0 = points[i].0 + points[i].2;
            points[i].1 = points[i].1 + points[i].3;
        }
        loop_counter += 1;

        /* find min and max posx / posy */
        let mut posx_min = std::i64::MAX;
        let mut posy_min = std::i64::MAX;
        let mut posx_max = std::i64::MIN;
        let mut posy_max = std::i64::MIN;
        for point in &points {
            if point.0 < posx_min {posx_min = point.0;}
            if point.0 > posx_max {posx_max = point.0;}
            if point.1 < posy_min {posy_min = point.1;}
            if point.1 > posy_max {posy_max = point.1;}
        }
        /* draw star map */
        println!("Second: {}", loop_counter);
        for y in posy_min..posy_max+1 {
            for x in posx_min..posx_max+1 {
                let mut point_here = false;
                for point in &points {
                    if point.0 == x && point.1 == y {point_here = true; break;}
                }
                if point_here {print!("#");} else {print!(".");}
            }
            println!("");
        }
        println!("");
    }

}
