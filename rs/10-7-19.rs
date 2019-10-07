/*
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
*/

struct HitCounter {
	hits: Vec<u32>
}


impl HitCounter {
	fn new() -> HitCounter {
		HitCounter {
			hits: Vec::<u32>::new()
		}
	}

	fn record(&mut self, timestamp: u32) {
		self.hits.push(timestamp);
	}

	fn total(&self) -> u32 {
		self.hits.len() as u32
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
}
