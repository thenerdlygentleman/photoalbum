#[allow(unused_imports)]
use clap::Parser;
use exif::Field;
use exif::Reader;
use exif::Tag;
use iocraft::prelude::*;
use std::fs::File;
use std::io::Read;
use std::path::Path;

#[derive(Parser)]
#[command(name = "photoalbum")]
#[command(version = "0.1.0")]
#[command(about = "photoalbum cli", long_about = None)]
struct Args {
    #[arg(short, long)]
    input: String,
}

fn main() {
    element! {
        Box(
            border_style: BorderStyle::Round,
            border_color: Color::Blue,
        ) {
            Text(content: "Welcome to the photoalbum")
        }
    }
    .print();

    let args = Args::parse();

    let _image = std::fs::read(&args.input).unwrap();

    let _file_name = Path::new(&args.input).file_name().unwrap();
    println!("Name is: {:?}", _file_name);
}
