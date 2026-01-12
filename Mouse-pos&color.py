import win32gui, win32api # pyright: ignore[reportMissingModuleSource]

def getColor(coords):
    return rgbTuple(win32gui.GetPixel(
        win32gui.GetDC(win32gui.GetActiveWindow()), coords[0], coords[1]))

def rgbTuple(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)


while True:
    input()
    print(f"{win32api.GetCursorPos()}, {getColor(win32api.GetCursorPos())}")