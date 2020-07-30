use std::io;
use std::fs::File;
use std::io::prelude::*;

fn start(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Главная функция
	imprint(_f1, _f2); //Вывод изображений
	println!("\n1 - Пересечение\n2 - Слияние\n3 - Исключающее или\n4 - Отрицание 1\n5 - Отрицание 2\n6 - Выход");
	let mut string = String::new();
	io::stdin().read_line(&mut string)
		.expect("Что-то не так");

	let num: i32 = string.trim().parse::<i32>()
		.expect("Что-то не так");

	match num { //Выбор действия
		1 => one(_f1, _f2),
		2 => second(_f1, _f2),
		3 => third(_f1, _f2),
		4 => fourth(_f1, _f2),
		5 => fourth(_f2, _f1),
		6 => exit(),
		_ => start(_f1, _f2),
	}
}

fn imprint(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Вывод изображений
	let mut i = 0;
	let mut j = 0;
	let mut l = 79;
	while i < 3082 {
		if i == 0 && j == 0 {
			print!("");
		} else if i < l && j == 0 {
			if _f1[i] == 0 {
				print!("▓");
			} else {
				print!("░");
			}
		} else if i == l && j == 0 {
			print!(" | ");
			j = 1;
			i = l - 79;
		} else if i < l && i >= 0 && j == 1 {
			if _f2[i] == 0 {
				print!("▓");
			} else {
				print!("░");
			}
		} else if i == l && j == 1 {
			j = 0;
			print!("\n");
			l = l + 79;
		}
		i = i + 1;
	}
	print!("\n");
}

fn one(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Пересечение
	for i in 0..3081 {
		_f1[i] = _f1[i] * _f2[i];
	}
	start(_f1, _f2);
}

fn second(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Слияние
	for i in 0..3081 {
		if _f1[i] == 1 || _f2[i] == 1 {
			_f1[i] = 1;
		} else {
			_f1[i] = 0;
		}
	}
	start(_f1, _f2);
}

fn third(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Исключающее или
	for i in 0..3081 {
		_f1[i] = (_f1[i] - _f2[i]).pow(2);
	}
	start(_f1, _f2);
}

fn fourth(_f1: &mut [i32; 3081], _f2: &mut [i32; 3081]) { //Отрицание
	for i in 0..3081 {
		if _f1[i] == 0 {
			_f1[i] = 1;
			continue;
		} else {
			_f1[i] = 0;
		}
	}
	start(_f1, _f2);
}

fn exit() {
	std::process::exit(0);
}

fn main() {
	let _i1: &'static str = "i1.txt";
	let _i2: &'static str = "i2.txt";

	let mut v1: [i32; 3081] = [0; 3081];
	let mut v2: [i32; 3081] = [0; 3081];

    let mut f1 = File::open(_i1).expect("Файл 1 не найден");
	let mut _file1 = String::new();
	f1.read_to_string(&mut _file1)
	    .expect("Файл 1 не прочитан");
    let mut j = 0;
	for i in _file1.chars() {
	    if i == '0' || i == '1'{
	    	if i == '1' {
	    		v1[j] = 1;
	    	} else if i == '0' {
	    		v1[j] = 0;
	    	}
	    	j = j + 1;
	    }
	}

    let mut f2 = File::open(_i2).expect("Файл 2 не найден");
	let mut _file2 = String::new();
	f2.read_to_string(&mut _file2)
	    .expect("Файл 2 не прочитан");
	let mut k = 0;
	for i in _file2.chars() {
	    if i == '0' || i == '1'{
	    	if i == '1' {
	    		v2[k] = 1;
	    	} else if i == '0' {
	    		v2[k] = 0;
	    	}
	    	k = k + 1;
	    }
	}
	start(&mut v1, &mut v2);
}