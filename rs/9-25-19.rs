/*
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in
sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

Run With:
rustc 9-25-19.rs && 9-25-19 && rm 9-25-19.exe 9-25-19.pdb
*/

fn sorted_square(mut list: Vec<i32>) -> Vec<i32> {
    let any_negatives = *list.first().unwrap() < 0;
    
    for i in list.iter_mut() {
        *i = *i * *i;
    }

    // Have to sort if any of the values were negative
    if any_negatives {
        
    }

    list
}

fn main() {
    println!("Hello World!");

    println!("{:?}", sorted_square(vec![-9, -2, 0, 2, 3]));
}
