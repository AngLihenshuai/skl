import glob, sys, fitz, os

# To get better resolution
zoom_x = 4.0  # horizontal zoom
zoom_y = 4.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

path = 'example.pdf'
all_files = glob.glob(path)
n = sys.argv[1]
os.mkdir("p/" + n)
for filename in all_files:
    doc = fitz.open(filename)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        png_path = "p/" + n + "/" + "pdf-page-" + str(page.number) + ".png"
        pix.save(png_path)
        print('<img src="https://anglihenshuai.github.io/skl/' + png_path + '">')
os.remove("example.pdf")