# image_to_ascii_art
A Python-based project to convert images into ASCII text art. <br />

Step 1: The input image is converted into an 8-bit grayscale format. <br />
Step 2: The image is divided into 250 columns of rectangular tiles. Each column has multiple tiles, and each tile has multiple pixels. <br />
Step 3: The average brightness of the pixels of each individual tile is calculated by the avg_brightness() function. <br />
Step 4: According to their respective brightnesses, each tile is assigned one of 70 ASCII characters. <br />
Step 5: The resultant text art is outputted to a text file.
