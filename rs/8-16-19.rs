/*
See if 2 strings are permutations of each other.

Hints:
 * Define permutation
 * Use a HashTable
 * Can you sort both strings and compare them? That would give answer.

Run with:

rustc f.rs && f && rm f.exe f.pdb

Python Solution:

IsPerm = lambda a, b: set(a) | set(b) == ?
 */

use std::collections::HashMap;
use std::collections::HashSet;
use std::iter::FromIterator;


fn is_perm(a: String, b: String) -> bool {  // O(a log a + b log b)

    if a.chars().count() != b.chars().count() {
        return false;
    }
    
    let mut a_map = HashMap::new();
    let mut b_map = HashMap::new();

    for letter in a.chars() {  // O(a)
        if !a_map.contains_key(&letter.to_string()) {
            a_map.insert(letter.to_string(), 0);
        }

        else {
            *a_map.get_mut(&letter.to_string()).unwrap() += 1;
        }
    }

    for letter in b.chars() {  // O(b)
        if !b_map.contains_key(&letter.to_string()) {
            b_map.insert(letter.to_string(), 0);
        }

        else {
            *b_map.get_mut(&letter.to_string()).unwrap() += 1;
        }
    }

    a_map == b_map
}


fn is_perm2(a: String, b: String) -> bool {
    let a_set: HashSet<char> = HashSet::from_iter(a.chars());
    let b_set: HashSet<char> = HashSet::from_iter(a.chars());

    let c_set = a_set.union(&b_set);

    for c in c_set {
        let character = c.to_string();
        let character = character.as_str();
        if a.matches(&character).count() != b.matches(&character).count() {
            return false
        }
    }
    
    true
}


fn main() {
    let mut a = "hello".to_string();
    let mut b = "ehllo".to_string();
    
    println!(
        "'{}' is permutation of '{}': {}",
        a.clone(), b.clone(), is_perm2(a, b)
    );

    a = "foobarbaz".to_string();
    b = "what in the world?".to_string();

    println!(
        "'{}' is permutation of '{}': {}",
        a.clone(), b.clone(), is_perm2(a, b)
    );
}
