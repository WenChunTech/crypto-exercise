use openssl::symm::{Cipher, Crypter, Mode};

fn main() {
    let l = "061cecfd897548208c76c04b6e7fb".as_bytes();
    let f: &mut Vec<u8> = &mut "parentFolderId=11463310842361563&fileName=conf.xml&fileSize=369&sliceSize=10485760&fileMd5=bfb07d9b177e301db54230699a735f15&sliceMd5=bfb07d9b177e301db54230699a735f15".as_bytes().to_vec();
    let block_size = Cipher::aes_128_cbc().block_size();
    // pkcs7_padding(f, block_size);
    let mut output = vec![0; 1024];
    let mut encrypter = Crypter::new(Cipher::aes_128_ecb(), Mode::Encrypt, &l[..16], None).unwrap();
    encrypter.pad(true);

    match encrypter.update(&f, &mut output) {
        Ok(size) => {
            eprintln!("size is: {size}");
            println!("{:?}", &output[..size]);
            println!("{:02x?}", &output[..size]);


        }
        Err(_) => {}
    };
}

fn pkcs7_padding(data: &mut Vec<u8>, block_size: usize) {
    let padding_num = block_size - data.len() % block_size;
    let padding = padding_num as u8;
    data.append(&mut [padding].repeat(padding_num));
    
}
