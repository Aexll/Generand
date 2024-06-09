
:: upgrading pip
echo Upgrading pip > log.txt
py -m pip install --upgrade pip >> log.txt


:: installing Pillow to Generate image
echo ' ' >> log.txt
echo Installing Pillow >> log.txt
py -m pip install Pillow >> log.txt


:: installing Numpy to do Matrix Math
echo ' ' >> log.txt
echo Installing Numpy >> log.txt
py -m pip install Numpy >> log.txt



:: installing open cv to transform images
echo ' ' >> log.txt
echo Installing OpenCV2 >> log.txt
py -m pip install opencv-python >> log.txt



:: installing pyimgui to have user interface
echo ' ' >> log.txt
echo Installing Pyimgui >> log.txt
py -m pip install imgui[full]



:: installing matplotlib to have user interface
echo ' ' >> log.txt
echo Installing Matplotlib >> log.txt
py -m pip install matplotlib


:: installing dearpygui to have user interface
echo ' ' >> log.txt
echo Installing dearpygui >> log.txt
py -m pip install dearpygui