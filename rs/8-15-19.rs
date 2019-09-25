/*
IsUnique()

Implement an algorithm that checks a string to see if it contains all unique
characters.

Hints:
 * Try a Hash Table
 * Could a bit vector be useful?
 * Can it be solved in O(n log n) time?

Run with:

rustc e.rs && e && rm e.exe e.pdb
*/

//use std::collections::HashMap;
use std::collections::HashSet;

fn is_unique(string: String) -> bool {  // O(string log string)
    let mut map = HashSet::new();

    for i in string.chars() {           // O(string)
        map.insert(i.to_string());      // O(log string)
        // If i not in map: O(log map)
    }

    map.len() == string.len()
}

fn main() {
    println!("is_unique(\"{:<10}\") == true: {}", "abcd", is_unique("abcd".to_string()));
    println!("is_unique(\"{:<10}\") == true: {}", "duffle bag", is_unique("duffle bag".to_string()));
}
