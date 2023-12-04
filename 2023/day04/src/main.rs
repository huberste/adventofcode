use std::env;
use std::fs;

#[derive(Debug)]
struct Card {
    nr: usize,
    numbers: Vec<usize>,
    winning: Vec<usize>,
    copies: usize,
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let inputfile = if args.len() < 2 { "input" } else { &args[1] };

    // read file
    let contents = fs::read_to_string(inputfile).expect("Something went wrong reading the file");

    let mut cards: Vec<Card> = vec![];

    // parse input file
    for line in contents.lines() {
        let (cardstr, numbersstr) = line.split_once(':').unwrap();
        let (_card, cardnr) = cardstr.split_once(' ').unwrap();
        let cardnr: usize = cardnr.trim().parse().unwrap();
        let (numbers_have_str, numbers_winning_str) = numbersstr.trim().split_once('|').unwrap();
        let mut numbers_have: Vec<usize> = vec![];
        let mut numbers_winning: Vec<usize> = vec![];
        for element in numbers_have_str.split_whitespace() {
            numbers_have.push(element.parse().unwrap());
        }
        for element in numbers_winning_str.split_whitespace() {
            numbers_winning.push(element.parse().unwrap());
        }
        cards.push(Card {
            nr: cardnr,
            numbers: numbers_have,
            winning: numbers_winning,
            copies: 1,
        });
    }

    // get solution for part 1
    let mut sum: usize = 0;
    let mut sum_cards: usize = 0;
    for current_card in 0..cards.len() {
        let mut matches: usize = 0;
        for num1 in &cards[current_card].numbers {
            for num2 in &cards[current_card].winning {
                if num1 == num2 {
                    matches += 1;
                    break;
                }
            }
        }
        if matches > 0 {
            sum += 2_usize.pow(matches.try_into().unwrap()) / 2;
        }
        for match_nr in 1..=matches {
            let nextcard = cards[current_card].nr + match_nr - 1;
            if nextcard > cards.len() - 1 {
                println!("can't create copies of cards that don't exist: only have {} cards, but should copy card nr {}!", cards.len(), nextcard);
            } else {
                cards[nextcard].copies += cards[current_card].copies;
            }
        }
        sum_cards += cards[current_card].copies;
    }

    println!("Total points: {}", sum); // example: 13, input: 21568
    println!("Total scratchcards: {}", sum_cards); // example: 30, input: 11827296
}
