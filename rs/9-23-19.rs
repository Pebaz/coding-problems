/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation
in-place?

Run with:
rustc i.rs && i && rm i.exe i.pdb
*/

// Worst case: O(n*2)
fn reverse_words(words: String) -> String {
    let mut last_space = 0;
    let chars = words.chars().collect::<Vec<char>>();
    let mut buf = Vec::with_capacity(words.len());
    
    for i in 0 .. words.len() {  // O(words)
        let letter = chars.get(i).unwrap();
        let at_end = i == words.len() - 1;
        
        if at_end || *letter == ' ' {
            let end_index = i + if at_end { 1 } else { 0 };
            
            for index in last_space .. end_index {  // O(words)
                let reverse = last_space + end_index - index - 1;
                let reverse = chars.get(reverse).unwrap();
                buf.push(*reverse);
            }

            last_space = i + 1;
            if !at_end {
                buf.push(' ');
            }
        }
    }

    buf.into_iter().collect()
}

fn main() {
    let string = String::from("Hello World!");
    println!("Original: \"{}\"", &string);
    println!("Reversed: \"{}\"", reverse_words(string));

    let string = String::from("How is everything going?");
    println!("Original: \"{}\"", &string);
    println!("Reversed: \"{}\"", reverse_words(string));
}
