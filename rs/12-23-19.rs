/*
rustc 12-23-19.rs && ./12-23-19 && rm 12-23-19
*/

use std::collections::{HashMap, HashSet};

fn combos(numbers: HashMap::<String, Vec<String>>, num: String) -> Vec<String> {
	let mut result = Vec::new();
	let mut mem = HashSet::<String>::new();

	for digit in num.chars() {
		println!("{:?}", numbers[&digit.to_string()]);

		result.push(String::from(""));
	}

	result
}

fn main() {
	let mut numbers = HashMap::<String, Vec<String>>::new();

	numbers.insert("2".to_string(), vec!["a".to_string(), "b".to_string(), "c".to_string()]);
	numbers.insert("3".to_string(), vec!["d".to_string(), "e".to_string(), "f".to_string()]);
	numbers.insert("4".to_string(), vec!["g".to_string(), "h".to_string(), "i".to_string()]);
	numbers.insert("5".to_string(), vec!["j".to_string(), "k".to_string(), "l".to_string()]);
	numbers.insert("6".to_string(), vec!["m".to_string(), "n".to_string(), "o".to_string()]);
	numbers.insert("7".to_string(), vec!["p".to_string(), "q".to_string(), "r".to_string(), "s".to_string()]);
	numbers.insert("8".to_string(), vec!["t".to_string(), "u".to_string(), "v".to_string()]);
	numbers.insert("9".to_string(), vec!["w".to_string(), "x".to_string(), "y".to_string(), "z".to_string()]);

	println!("{:?}", combos(numbers, "234".to_string()));

	println!("Hello World!");
}
