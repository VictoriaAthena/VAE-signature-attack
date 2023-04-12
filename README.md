# VAE-signature-attack

The repository contains codes for IJCB 2023 submission "Robustness of signature authentication models against synthetic attacks". 

*****insert abstract*****

The datasets used in the paper are CEDAR and UTSig
Link to generated images from CEDAR real samples https://drive.google.com/drive/folders/1H-PlCRsjYI4pTvx-1WmXog0IFB6A82kK?usp=sharing 

Link to generated images from CEDAR forgery samples https://drive.google.com/drive/folders/1-A1XdNMj9hQOxaJxjlxDuvupWz1KOlBw?usp=sharing

Link to generated images from UTSig real samples https://drive.google.com/drive/folders/1BAJ5EZDOMh1yzPYLj77vz_Uv02l-5jHo?usp=sharing

Link to generated images from UTSig simple forgery https://drive.google.com/drive/folders/1aYl0Mvma0Z7FOZHmhUJfqTKVBnogt-m4?usp=sharing


The vae_single.py code contains model trainings to generate images for 1 image, and batch_vae_gen.py to run the generation for all data samples. 
The code is based on the CEDAR dataset. Users need to download the datasets and change the paths in the codes as commented there

The repository also includes a verification model based on VGG16. Please follow the instruction in the codes to do proper setups for running. 
