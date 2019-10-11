/*
def show_matrix(matrix):
    for row in matrix:
        print('{} {} {}'.format(*row))

def rotate_matrix(matrix):
    return [
        [matrix[col][len(matrix) - 1 - row] for col in range(len(matrix[0]))]
        for row in range(len(matrix))
    ]

m = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

show_matrix(rotate_matrix(m))

def foo(m):
    for r in m: print(('{:<3}' * len(r)).format(*r))
    print()
    side = len(m[0])
    zones = side // 2
    print(f'There are {zones} zones')
    for i in range(zones):
        buffer = [None] * (side - i - i)
        
        # Save each side
        top  = [m[i][r] for r in range(i, side - i)]
        left = [m[side - r - 1][i] for r in range(i, side - i)]
        bot  = [m[side - i - 1][side - r - 1] for r in range(i, side - i)]
        right = [m[r][side - i - 1] for r in range(i, side - i)]
        
        print(top, left, bot, right)
        
        # Swap them
        for buf_index, r in enumerate(range(i, side - i)):
            m[side - r - 1][i]            = top  [buf_index]  # Left = Top
            m[side - i - 1][side - r - 1] = left [buf_index]  # Bot = Left
            m[r][side - i - 1]            = bot  [buf_index]  # Right = Bot
            m[i][r]                       = right[buf_index]  # Top = Right
            

    print()
    for r in m: print(('{:<3}' * len(r)).format(*r))
    print()

foo([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

Given a matrix of size NxN, rotate the matrix in place by 90 degrees.

Run With:
cls; rustc .\10-11-19.rs ; ./10-11-19
*/

use std::collections::HashSet;

fn rotate_matrix(matrix: &mut Vec<i32>, n: i32) {
	let mut processed = HashSet::with_capacity(n as usize);

	for index in 0 .. matrix.len() {
		if processed.contains(&index) {continue;}
		processed.insert(index);

		let x = index as i32 % n;
		let y = index as i32 / n;
		let original_index = x + y * n;
		let new_x = n - y;
		let new_y = x;
		let new_index = (new_x + new_y * n) - 1;
		//println!("({}, {}) == ({}, {}) | {}, {}", x, y, new_x, new_y, index, new_index - 1);

		// Swap the indices
		//staging = matrix[new_index as usize].clone();
		//matrix[new_index as usize] = matrix[original_index as usize];

		let mut staging = matrix[original_index as usize].clone();
		for dir in 0 .. 4 {
			let x = index as i32 % n;
			let y = index as i32 / n;
			let original_index = x + y * n;
			let new_x = n - y;
			let new_y = x;
			let new_index = (new_x + new_y * n) - 1;

			if processed.contains(&(index as usize)) {continue;}
			processed.insert(index as usize);

			// Swap the indices
			matrix[original_index as usize] = staging;
			staging = matrix[new_index as usize].clone();
		}
	}
}


fn main() {

	let mut matrix = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
	let side_length = (matrix.len() as f32).sqrt() as i32;

	println!("Before:");
	for y in 0 .. side_length {
		for x in 0 .. side_length {
			let index = x + y * side_length;
			print!("{:<2}", matrix[index as usize]);
		}
		print!("\n");
	}

	rotate_matrix(&mut matrix, side_length);

	println!("\nAfter:");
	for x in 0 .. side_length {
		for y in 0 .. side_length {
			let index = x + y * side_length;
			print!("{:<2}", matrix[index as usize]);
		}
		print!("\n");
	}
}
