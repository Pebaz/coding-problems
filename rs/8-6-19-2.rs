fn modulus(a: u32, b: u32) -> u32 {
	((a % b) + b) % b
}


fn next_digit(num: u32) -> (u32, bool) {
	if num < 10 {
		(num, false)
	} else {
		(modulus(num, 10), true)
	}
}


fn is_perfect(mut num: u32) -> bool{
	let mut digits = Vec::new();
	 
	let (mut digit, mut not_done) = next_digit(num);
	
	digits.push(digit);
	
	num /= 10;
	
	while not_done {
		let tuple = next_digit(num);
		
		digit = tuple.0;
		
		digits.push(digit);
		
		not_done = tuple.1;
		
		num /= 10;
	}
	
	
	let sum = digits.iter().sum::<u32>();
	
	sum == 10
}


fn nth_perfect(n: u32) -> u32 { 
	let mut count = 0;
	let mut num = 0;
	
	while count < n {
		num += 1;  // Since 0 is not perfect, pre-increment
		
		if is_perfect(num) {
			count += 1;
		}
	}
	
	return num;
}


fn main() {
	println!("Hello World!");
	
	println!("19 is perfect: {}", is_perfect(19));
	
	let mut perfects = Vec::new();

	for i in 0 .. 100 {
		let num = nth_perfect(i);
		println!("Perfect({}): {}", i, num);
		perfects.push(num);
	}

	println!("\nPerfect numbers:");

	let cols = 10;
	let mut count = 0;

	for i in &perfects {
		count += 1;

		if count >= cols {
			println!("{}", i);
			count = 0;
		} else {
			print!("{:<5}", i);
		}
	}
	
	println!("Done");
}


























