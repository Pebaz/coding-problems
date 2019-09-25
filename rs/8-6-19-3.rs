

fn main() {
	let age = 24;

	match age {
		21 => println!("Can drink."),
		22 => println!("22"),
		24 => println!("That's my age!"),
		_ => ()
	}

	let foo = vec![1, 2, 3];

	if let Some(first) = foo.get(10) {
		println!("{}", first);
	} else {
		println!("Uh oh.");
	}

	match foo.get(2) {
		Some(first) => println!("{}", first),
		None => println!("Does not exist!")
	}
}

