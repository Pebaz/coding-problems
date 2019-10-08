/*
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in
chronological order and an integer k, return the maximum profit you can make
from k buys and sells. You must buy the stock before you can sell it, and you
must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

Run With:
cls; rustc .\10-8-19.rs ; ./10-8-19
*/

//use std::collections::HashMap;

// BTreeMap allows sorted iteration *BY KEY* NOT BY INSERTION ORDER
// However, this works since the keys *ARE* the insertion order =)
use std::collections::BTreeMap;

fn trade(shares: Vec<u32>, trade_count: u32) -> u32 {
	let mut data = BTreeMap::new();

	for (i, item) in shares.iter().rev().enumerate() {
		data.insert((shares.len() - i - 1) as u32, item.clone());
	}

	let mut profit = 0u32;

	for _ in 0 .. trade_count {
		// Find Lowest
		let mut lindex = 0;
		let mut lowest = data[&0u32].clone();

		for (i, v) in &data {
			if *v < lowest {
				lowest = *v;
				lindex = *i;
			}
		}

		// Find Highest
		let mut hindex = lindex;
		let mut highest = lowest;

		for (i, v) in &data {
			if *i > lindex {
				if *v > highest {
					highest = *v;
					hindex = *i;
				}
			}
		}

		profit += shares[hindex as usize] - shares[lindex as usize];

		for index in lindex .. hindex + 1 {	
			data.remove(&index).unwrap();
		}
	}

	profit
}


fn main() {
	println!("Hello World!");

	assert!(trade(vec![5, 2, 4, 0, 1, 3], 2) == 5);
	assert!(trade(vec![5, 2, 4, 0, 1], 2) == 3);
	assert!(trade(vec![10, 0, 10, 2, 1, 2, 8], 2) == 17);
	assert!(trade(vec![1, 0, 1, 0, 1, 0, 1], 3) == 3);
	assert!(trade(vec![3, 0, 1, 0, 1, 0, 1], 4) == 3);

	println!("Done!");
}
