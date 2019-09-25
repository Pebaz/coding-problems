/*

*/

fn encode(s: String) -> String {
	let mut ret = String::new();
	let mut last = s[0 .. 1].to_string();
	let mut count = 0;

	for c in s.chars() {
		if c.to_string() == last {
			count += 1;
		} else {
			ret += format!("{}{}", count, last).as_str();
			last = c.to_string();
			count = 1;
		}
	}

	ret += format!("{}{}", count, last).as_str();

	ret
}

fn decode(s: String) -> String {
	let mut ret = String::new();

	let mut foo = s.chars();
	
	loop {
		let count = foo.next();

		match count {
			Some(ref _foo) => {}
			None => break
		}

		let letter = foo.next();

		for _ in 0 .. count.unwrap().to_string().parse::<i32>().unwrap() {
			ret += format!("{}", letter.unwrap()).as_str();
		}
	}

	ret += format!("").as_str();
	ret
}

fn main()  {
	println!("Hello World!");

	println!("{}", encode("AAAABBBCCDAA".to_string()));

	println!("{}", decode(encode("AAAABBBCCDAA".to_string())));

	assert_eq!("AAAABBBCCDAA", decode(encode("AAAABBBCCDAA".to_string())));



	let b = String::from("4");

	for i in 0 .. b.parse::<i32>().unwrap() {
		println!("{}", i);
	}
}
