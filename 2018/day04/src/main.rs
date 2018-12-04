use std::collections::HashMap;
use std::env;
use std::fs;

extern crate chrono;
use chrono::{NaiveDateTime, Timelike};

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

    /* sort lines */
    let mut lines = Vec::new();
    for line in contents.lines() {
        lines.push(line);
    }
    lines.sort();

    // guards are identified by their ids, which is the *key*.
    // value is Vec<(date_asleep, date_wakeup)>
    let mut database: HashMap <i32, Vec<(NaiveDateTime, NaiveDateTime)>> = HashMap::new();
    let mut minute_map: HashMap <i32, Vec<i32>> = HashMap::new();
    let mut guard_id: i32 = 0;
    let mut fallasleep: NaiveDateTime = NaiveDateTime::parse_from_str("2018-12-05 10:38", "%Y-%m-%d %H:%M").unwrap();
    let mut wakeup: NaiveDateTime;
    for line in lines {
        let first_split: Vec<&str> = line.split('[').collect();
        let second_split: Vec<&str> = first_split[1].split("] ").collect();
        //println!("{}", second_split[0]);
        let datetime = NaiveDateTime::parse_from_str(second_split[0], "%Y-%m-%d %H:%M").unwrap();
        //println!("{}", datetime.format("%Y-%m-%d %H:%M"));
        if second_split[1].starts_with("Guard") {
            // new guard
            let third_split: Vec<&str> = second_split[1].split("#").collect();
            let fourth_split: Vec<&str> = third_split[1].split(" begins").collect();
            guard_id = str::parse(fourth_split[0]).unwrap();
        } else if second_split[1].starts_with("falls") {
            fallasleep = datetime;
        } else if second_split[1].starts_with("wakes") {
            wakeup = datetime;
            let mut vector: Vec<(NaiveDateTime, NaiveDateTime)> = Vec::new();
            if database.contains_key(&guard_id) {
                // Is this supposed to work only like this in rust?
                for entry in database.get(&guard_id).unwrap() {
                    vector.push(*entry);
                }
            }
            vector.push((fallasleep, wakeup));
            database.insert(guard_id, vector);
        }
    }
    let mut max_time_asleep = 0;
    let mut sleepiest_guard = -1;
    for (key, entry) in &database {
        let mut sum = 0;
        let mut minutes = vec![0; 60];
        for (fallasleep, wakeup) in entry {
            let duration = wakeup.signed_duration_since(*fallasleep);
            sum += duration.num_minutes();
            let start = if fallasleep.hour() == 0 {fallasleep.minute()} else {0};
            let stop = if wakeup.hour() == 0 {wakeup.minute()} else {59};
            for i in start..stop {
                minutes[i as usize] += 1;
            }
        }
        minute_map.insert(*key, minutes);
        if sum > max_time_asleep {
            max_time_asleep = sum;
            sleepiest_guard = *key;
        }
    }
    
    let minutes = minute_map.get(&sleepiest_guard).unwrap();
    let mut sleepminute = 0;
    let mut sleep = 0;
    for i in 0..60 {
        if minutes[i as usize] > sleep {
            sleep = minutes[i as usize];
            sleepminute = i;
        }
    }

    println!("solution for part 1: #{} x minute {} = {}", sleepiest_guard, sleepminute, sleepiest_guard * sleepminute);

    let mut times_asleep = 0;
    let mut minute = 0;
    let mut guard = 0;
    for (key, minutes) in &minute_map {
        /* get maxmin for every guard*/
        let mut sleepminute = 0;
        let mut sleep = 0;
        for i in 0..60 {
            if minutes[i as usize] > sleep {
                sleep = minutes[i as usize];
                sleepminute = i;
            }
        }
        if sleep > times_asleep {
            guard = *key;
            times_asleep = sleep;
            minute = sleepminute;
        }
    }

    println!("solution for part 2: #{} x minute {} = {}", guard, minute, guard * minute);


}