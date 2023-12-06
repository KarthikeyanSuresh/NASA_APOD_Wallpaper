from PIL import Image

def resizeImage(input_path, output_path, basewidth, hsize):    
    img = Image.open(input_path)
    img = img.resize((basewidth, hsize))
    img.save(output_path)