use std::env;
use std::fs;


/*
--- Day 7: No Space Left On Device ---
*/

struct Node
{
    idx: usize,
    val: String,
    size: usize,
    parent: Option<usize>,
    children: Vec<usize>,
}

impl Node
{
    fn new(idx: usize, val: String, size: usize, parent: Option<usize>) -> Self {
        Self {
            idx,
            val,
            size,
            parent,
            children: vec![],
        }
    }
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

    let mut nodes: Vec<Node> = vec![];
    let root: Node = Node::new(nodes.len(), "/".to_string(), 0, None);
    nodes.push(root);
    let mut cur_dir: usize = 0;

    let total_disk_space: usize = 70000000;
    let needed_free_space: usize = 30000000;

    for line in contents.lines() {
        let mut args = line.split(" ");
        let arg = args.next().unwrap(); /* either "$", a size or "dir" */
        if arg == ("$") { /* command */
            let command = args.next().unwrap();
            if command == "ls" {
                // next line ist listing
            } else if command == "cd" {
                let new_dir = args.next().unwrap();
                if new_dir == ".." {
                    cur_dir = nodes[nodes[cur_dir].parent.unwrap()].idx;
                } else if new_dir == "/" {
                    cur_dir = 0;
                } else {
                    for child in &nodes[cur_dir].children[..] {
                        if nodes[*child].val == new_dir {
                            cur_dir = nodes[*child].idx;
                            break;
                        }
                    }
                }
            }
        } else { /* arg != "$" */
            //let arg = args.next().unwrap();
            /* directory listing */
            let new_node: Node;
            let idx: usize = nodes.len();
            if arg == "dir" {
                let new_folder_name = args.next().unwrap();
                new_node = Node::new (idx, new_folder_name.to_string(), 0, Some(cur_dir));
                nodes.push(new_node);
                nodes[cur_dir].children.push(idx);
            } else { /* arg is size */
                let size: usize = arg.parse().unwrap();
                let filename = args.next().unwrap();
                new_node = Node::new(idx, filename.to_string(), size, Some(cur_dir));
                nodes.push(new_node);
                nodes[cur_dir].children.push(idx);
                let mut parent: usize = idx;
                while parent > 0 {
                    parent = nodes[parent].parent.unwrap();
                    nodes[parent].size += size;

                }
            }

        }
    }

    let mut sum: usize = 0;
    let free_space = total_disk_space - nodes[0].size;
    let need_to_free = needed_free_space - free_space;
    let mut min_space: usize = total_disk_space;
    for node in nodes {
        if node.size <= 100000 && node.children.len() > 0 {
            sum += node.size;
        }
        if node.children.len() > 0 { /* check if directory */
            if node.size > need_to_free {
                if node.size < min_space {
                    min_space = node.size;
                }
            }
        }
    }

    println!("Part 1: What is the sum of the total sizes of those directories of total size <= 100000?");
    println!("The sum of total sizes of directories of size <= 100000 is {}.", sum);
    /* My puzzle answer was 1989474. (95437 for simple) */

    println!("Part 2: What is the total size of that directory?");
    println!("The total sizes of the smalles directory to delete is {}.", min_space);
    /* My puzzle answer was 1989474. (95437 for simple) */

}