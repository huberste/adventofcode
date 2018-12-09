use std::env;
use std::fs;

fn manhattan_distance(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
    return (x1-x2).abs() + (y1-y2).abs();
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

    /* input is list of point coordinates in "x,y" style */
    let mut points: Vec<(i32, i32)> = Vec::new();
    for line in contents.lines() {
        let split: Vec<&str> = line.split(", ").collect();
        let x: i32 = str::parse(split[0]).unwrap();
        let y: i32 = str::parse(split[1]).unwrap();
        points.push((x,y));
    }

    /* get maxima */
    let mut maxx: i32 = 0;
    let mut maxy: i32 = 0;
    for point in &points {
        if point.0 > maxx {
            maxx = point.0;
        }
        if point.1 > maxy {
            maxy = point.1;
        }
    }
    println!("[DEBUG]maxx: {}, maxy: {}", maxx, maxy);

    /* calculate which point is nearest to coordinate(x,y) */
    let mut sizes: Vec<u32> = vec![0; points.len()];
    let mut infinite: Vec<bool> = vec![false; points.len()];
    let mut closest: Vec<Vec<i32>> = vec![vec![-1; (maxy+1) as usize]; (maxx+1) as usize];
    let mut i: i32;
    let mut totalsize: i32 = 0;
    for x in 0..maxx+1 {
        for y in 0..maxy+1 {
            let mut mindist = maxx + maxy;
            let mut totaldist: i32 = 0;
            i = 0;
            for point in &points {
                let dist = manhattan_distance(x, y, point.0, point.1);
                totaldist += dist;
                if dist < mindist {
                    closest[x as usize][y as usize] = i;
                    mindist = dist;
                    if x < 1 || x >= maxx || y < 0 || y >= maxy {
                        infinite[i as usize] = true;
                    }
                } else if dist == mindist {
                    closest[x as usize][y as usize] = -1;
                }
                i += 1;
            }
            if totaldist < 10000 {
                totalsize += 1;
            }
        }
    }

    /* calculate sizes for each point's area */
    for x in 0..maxx+1 {
        for y in 0..maxy+1 {
            if closest[x as usize][y as usize] >= 0 {
                sizes[closest[x as usize][y as usize] as usize] += 1;
            }
        }
    }

    /* calculate point with max area */
    i = 0;
    let mut maxsize = 0;
    let mut maxpoint = 0;
    for size in sizes {
        if maxsize < size {
            if !infinite[i as usize] {
                maxsize = size;
                maxpoint = i;
            }
        }
        i += 1;
    }

    println!("max: size({},{}) = {}", points[maxpoint as usize].0, points[maxpoint as usize].1, maxsize);

    println!("totaldist_size = {}", totalsize);

}
