use std::env;
use std::fs;


/*
--- Day 8: Treetop Tree House ---
*/

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

    let mut trees: Vec<Vec<u32>> = vec![];
    let mut scenic_score: Vec<Vec<u32>> = vec![];
    let mut visible_trees: usize = 0;

    for line in contents.lines() {
        let mut tree_line: Vec<u32> = vec![];
        for char in line.chars() {
            tree_line.push(char.to_digit(10).unwrap())
        }
        trees.push(tree_line);
        scenic_score.push(vec![]);
        assert_eq!(trees[0].len(), trees[trees.len()-1].len());
    }

    // for tree_line in &trees {
    //     for tree in tree_line {
    //         print!("{}", tree);
    //     }
    //     println!("");
    // }

    for x in 0..trees.len() {
        for y in 0..trees[x].len() {
            /* tree to look at: (x,y) */
            let mut is_visible = false;
            let mut visible_north = 0;
            let mut visible_east = 0;
            let mut visible_south = 0;
            let mut visible_west = 0;
            if x == 0|| x == trees.len()-1 || y == 0 || y == trees[x].len()-1  {
                is_visible = true;
            }
            if y > 0 {
                /* go north (y-)*/
                for tree_north in 0..y {
                    visible_north += 1;
                    if trees[x][y-tree_north-1] >= trees[x][y] {
                        break;
                    }
                    if tree_north == y-1 {
                        is_visible = true;
                    }
                }
            }
            if y < trees[x].len() {
                /* go south (y+)*/
                for tree_south in y+1..trees[x].len() {
                    visible_south += 1;
                    if trees[x][tree_south] >= trees[x][y] {
                        break;
                    }
                    if tree_south == trees[x].len()-1 {
                        is_visible = true;
                    }
                }
            }
            if x > 0{
                /* go west (x-)*/
                for tree_west in 0..x {
                    visible_west += 1;
                    if trees[x-tree_west-1][y] >= trees[x][y] {
                        break;
                    }
                    if tree_west == x-1 {
                        is_visible = true;
                    }
                }
            }
            if x < trees.len() {
                /* go east (x+)*/
                for tree_east in x+1..trees.len() {
                    visible_east += 1;
                    if trees[tree_east][y] >= trees[x][y] {
                        break;
                    }
                    if tree_east == trees.len()-1 {
                        is_visible = true;
                    }
                }
            }
            scenic_score[x].push(visible_north * visible_east * visible_south * visible_west);
            if is_visible {
                visible_trees += 1;
            }
        }
    }

    let mut max_scenic_score = 0;
    for tree_line in &scenic_score {
        for tree in tree_line {
            if *tree > max_scenic_score {
                max_scenic_score = *tree;
            }
        }
    }

    println!("Part 1: How many trees are visible from outside the grid?");
    println!("{} trees are visible from outside the grid.", visible_trees);
    /* My puzzle answer was 1703. (21 for simple) */

    println!("Part 2: What is the highest scenic score possible for any tree?");
    println!("The highest scenic score possible for any tree is {}.", max_scenic_score);
    /* My puzzle answer was 496650. (8 for simple) */

}