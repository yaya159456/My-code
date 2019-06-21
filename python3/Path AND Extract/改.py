import os
filename = r'I:\长安新城及樱花园小学\波形文件_前加01-长安新城-'
for root, dir, file in os.walk(filename ):
    for i in file:
        name = i
        os.rename(os.path.join(root, name), os.path.join(root, "01-长安新城-" + name))