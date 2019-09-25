/*
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of
times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is
acb, return false.

Run With:
rustc h.rs && h && rm h.exe h.pdb
*/

fn main() {
    let str1 = String::from("Hello World!");
    let str2 = String::from("eHllo World!");

    println!("a < b: {}", 'a' < 'b');

    let new: Vec<char> = Vec::with_capacity(str1.len());

    let string = str1.as_str();
    
    for i in 0 .. string.len() - 1 {
        for j in i + 1 .. string.len() {
            if string[i] > string[j] {
                let temp = string[i];
                string[i] = string[j];
                string[j] = temp;
            }
        }
    }
}
