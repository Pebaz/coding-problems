/*
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?

Run With:
cls; rustc .\10-7-19.rs ; ./10-7-19
*/

use std::fs::OpenOptions;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;


struct HitCounter {
	hits: Vec<u32>,
	count: u32
}


/// Assumes timestamps are recorded in chronological order.
impl HitCounter {
	fn new() -> HitCounter {
		HitCounter {
			hits: Vec::<u32>::new(),
			count: 0
		}
	}

	fn new_file() -> HitCounter {
		File::create("timestamps");
		HitCounter {
			hits: Vec::<u32>::new(),
			count: 0
		}
	}

	fn record(&mut self, timestamp: u32) {
		self.count += 1;
		self.hits.push(timestamp);
	}

	fn total(&self) -> u32 {
		self.count
	}

	fn range(&self, lower: u32, upper: u32) -> u32 {
		//self.hits[lower as usize .. upper as usize].len() as u32
		let mut count = 0;
		for hit in &self.hits {
			if *hit >= lower && *hit <= upper { count += 1; }
			if *hit > upper { break; }
		}
		count
	}

	fn record_file(&mut self, timestamp: u32) {
		self.count += 1;
		let mut file = OpenOptions::new()
			.write(true)
			.append(true)
			.open("timestamps")
			.unwrap();
		
		file.write(&timestamp.to_be_bytes());
	}

	fn range_file(&self, lower: u32, upper: u32) -> u32 {
		let mut file = File::open("timestamps").unwrap();
		let mut reader = BufReader::new(file);
		let mut count = 0;
		let mut the_hit = [0u8; 4];

		loop {
			if let Err(e) = reader.read(&mut the_hit) {
				break;
			}

			let hit = u32::from_be_bytes(the_hit);
			if hit >= lower && hit <= upper { count += 1; }
			if hit > upper { break; }
		}


		println!("COUNT {}", count);
		count
	}
}


fn main() {
	println!("Hello World!");

	let mut counter = HitCounter::new();

	counter.record(1);
	counter.record(10);
	counter.record(20);
	counter.record(24);
	counter.record(30);

	assert!(counter.total() == 5);

	assert!(counter.range(3, 14) == 1);
	assert!(counter.range(19, 29) == 2);

	// Test file api
	let mut counter = HitCounter::new_file();
	
	counter.record_file(1);
	counter.record_file(10);
	counter.record_file(20);
	counter.record_file(24);
	counter.record_file(30);

	assert!(counter.total() == 5);

	assert!(counter.range_file(3, 14) == 1);
	assert!(counter.range_file(19, 29) == 2);

	// Cleanup
	std::fs::remove_file("timestamps").unwrap();
}
