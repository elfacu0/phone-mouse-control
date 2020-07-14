from flask import Flask
from flask import render_template
from flask import request
import pyautogui
from win32api import GetSystemMetrics
pyautogui.PAUSE = 0

app = Flask(__name__)

window_width = GetSystemMetrics(0)
window_height = GetSystemMetrics(1)
last_x = 0
last_y = 0
@app.route('/move_mouse')
def move_mouse():
    global last_x
    global last_y
    global window_height
    global window_width
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    is_drawing = request.args.get('isDrawing')
    if(last_x==0 or last_y==0):
        last_x = x
        last_y = y

    ## y is x because phone is supposed to be horizontal
    current_x = pyautogui.position()[0]+(y-last_y) 
    current_y = pyautogui.position()[1]+(last_x-x)
    if(current_x<window_width and current_y<window_height and current_x>0 and current_y>0):
        if(is_drawing == "false"):
            pyautogui.moveTo(current_x,current_y)
        else:
            pyautogui.drag((y-last_y), (last_x-x))

    last_x = x
    last_y = y

    return ("nothing")

@app.route('/reset_position')
def reset_position():
    global last_y
    global last_x
    last_x = 0
    last_y = 0
    return ("nothing")


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.15", port=80)
