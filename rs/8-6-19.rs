

/*
It is assumed that the passed word is never longer than the grid width/height.
*/
fn exists(grid: &Vec<Vec<String>>, word: String) -> bool {
	// Check each row

	for row in grid {
		let mut row_word = String::new();

		for c in row {
			row_word.extend(c.chars());
		}

		if row_word == word {
			return true
		}
	}


	for col in 0 .. grid[0].len() {
		let mut col_word = String::new();

		for y in 0 .. grid.len() {
			col_word.extend(grid[y][col].chars());
		}

		if col_word == word {
			return true
		}
	}

	// Check each col

	false
}


fn main() {
	println!("Hello World!");

	let grid = vec![
		vec!["F".to_string(), "A".to_string(), "C".to_string(), "I".to_string()],
		vec!["O".to_string(), "B".to_string(), "Q".to_string(), "P".to_string()],
		vec!["A".to_string(), "N".to_string(), "O".to_string(), "B".to_string()],
		vec!["M".to_string(), "A".to_string(), "S".to_string(), "S".to_string()],
	];

	for word in vec!["FOAM".to_string(), "MASS".to_string(), "STOP".to_string()] {
		println!("{} in grid: {}", word, exists(&grid, word.clone()));
	}
}
