/*
There are three types of edits that can be performed on strings: insert, remove,
or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

Run With:
rustc 12-12-19.rs && 12-12-19 && rm 12-12-19.exe 12-12-19.pdb
*/

fn compare(str1: String, str2: String) -> bool {
    if str1.len() != str2.len() {

    }

    else {
        let chars1 = str1.chars().collect::<Vec<char>>();
        let chars2 = str2.chars().collect::<Vec<char>>();
        for i in 0 .. str1.len() {
            println!("{} <-> {}", chars1.get(i).unwrap(), chars2.get(i).unwrap());
        }
    }
    
    false
}

fn main() {
    let str1 = String::from("Hello World!");
    let str2 = String::from("eHllo World!");
    
    println!("Comparing {} and {}", str1, str2);
    compare(str1, str2);
}
