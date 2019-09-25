/*
Urlify a string.

Replace all spaces with %20.

Run with:

rustc g.rs && g && rm g.exe g.pdb
 */

use std::{thread, time};


fn urlify(url: &mut Vec<char>, length: u32) {
    let mut spaces = 0;

    for i in 0 .. length {
        if url[i as usize] == ' ' {
            spaces += 1;
        }
    }

    println!("Number of spaces: {}", spaces);

    let mut index = length + spaces * 2;
    let mut i = length - 1;
    loop {
        if i <= 0 { break; }

        thread::sleep(time::Duration::from_millis(150));
        
        if url[i as usize] == ' ' {
            url[(index - 1) as usize] = '0';
            url[(index - 2) as usize] = '2';
            url[(index - 3) as usize] = '%';
            index -= 3;
            println!("\"{}\"", url.iter().collect::<String>());
        } else {
            url[(index - 1) as usize] = url[i as usize];
            index -= 1;
            println!("\"{}\"", url.iter().collect::<String>());            
        }

        i -= 1;
    }
}


fn main() {
    let url = "hello world!  ".to_string();

    println!("\"{}\"", url);
    let mut chars: Vec<char> = url.chars().collect();
    urlify(&mut chars, 12);
    let string: String = chars.iter().collect();
    println!("\"{}\"", string);
}
