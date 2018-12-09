use std::env;
use std::fs;

struct Tree {
    num_of_childs: u32,
    childs: Vec<Tree>,
    metadata: Vec<u32>,
}

fn read_tree(input: Vec<u32>) -> Tree {
    let num_of_childs = input[0];
    let metadata = input[input.len() - input[1] as usize..].to_vec();
    let children = read_trees(input[2..].to_vec(),num_of_childs).0;
    let tree: Tree = Tree {num_of_childs: num_of_childs, childs: children, metadata: metadata};

    return tree;
}

fn read_trees(input: Vec<u32>, count: u32) -> (Vec<Tree>, usize) {
    let mut result: Vec<Tree> = Vec::new();
    let mut num_children = 0;
    let mut i = 0;
    while num_children < count {
        let num_of_childs = input[i];
        //println!("num_of_childs={} ", input[i]);
        i += 1;
        let num_of_metadata = input[i];
        //println!("num_of_metadata={} ", input[i]);
        i += 1;
        let (children, read) = read_trees(input[i..].to_vec(), num_of_childs);
        //for j in 0..read { print!("{} ", input[i+j]);}
        //println!("read: {}", read);
        i += read;
        result.push(Tree {
            num_of_childs: num_of_childs,
            childs: children,
            metadata: input[i..i+num_of_metadata as usize].to_vec(),
        });
        num_children += 1;
        i += num_of_metadata as usize;
    }
    //println!("return i = {}", i);
    return (result, i);
}

fn calc_meta(tree: Tree) -> u32 {
    let mut result: u32 = 0;
    for meta in tree.metadata {
        result += meta;
    }
    for child in tree.childs {
        result += calc_meta(child);
    }
    return result;
}

fn calc_value(tree: Tree) -> u32 {
    let mut result: u32 = 0;
    if tree.num_of_childs == 0 {
        /* If a node has no child nodes, its value is the sum of its metadata
         * entries.
         **/
        result += calc_meta(tree);
    } else {
        /* However, if a node does have child nodes, the metadata entries become
         * indexes which refer to those child nodes. A metadata entry of 1
         * refers to the first child node, 2 to the second, 3 to the third, and
         * so on. The value of this node is the sum of the values of the child
         * nodes referenced by the metadata entries. If a referenced child node
         * does not exist, that reference is skipped. A child node can be
         * referenced multiple time and counts each time it is referenced.
         **/
        let mut i = 1;
        for child in tree.childs {
            let value = calc_value(child);
            for metadatum in &tree.metadata {
                if *metadatum == i {
                    result += value;
                }
            }
            i += 1;
        }
    }
    return result;
}

/* Advent of Code 2018, Day 08: Memory Maneuver */
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

    let strings: Vec<&str> = contents.split(" ").collect();
    let mut numbers: Vec<u32> = Vec::new();
    for string in strings {
        numbers.push(str::parse(string.trim()).unwrap());
    }

    let root: Tree = read_tree(numbers);
    //println!("Part 1: Sum of all metadata entries: {}", calc_meta(root));
    println!("Part 2: Value of the root node: {}", calc_value(root));
}
