import shutil
from vae_sig import *

cnt=1
temp=0
path_os = os.getcwd()
#dataset path
source_path=path_os+"/CEDAR/full_forg"
for images in os.listdir(source_path):
    #for each images in folder
        print(images + " generating...")
        img_path = source_path+i+'/'+images
        if os.path.exists(path_os+'/box'):
            shutil.rmtree(path_os+'/box')
        if os.path.exists(path_os+'/result_vae_hindi_real/generated_'+images[:-4] + '_1.png'):
            cnt+=1
            print(cnt,end=' ')
            continue
        #create folder box and folder img inside the box
        os.mkdir(path_os+'/box')
        os.mkdir(path_os+'/box/img')
        box_path=path_os+'/box/img'
        shutil.copy(img_path,box_path)
        kt=1
        #sometimes VAE will generate an error when generating, so simply re train the model
        while kt==1:
            try:
                kt=0
                generateimg(images)
            except:
                kt=1
        cnt+=1
        print(cnt,end=' ')
        shutil.rmtree(path_os+'/box')