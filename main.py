import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import cvzone
from cv2 import cv2
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class MyGrid(Widget):

    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def black_sunglass(self):
        overlay = cv2.imread('sunglass1.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 0.9), int(h * 0.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x + 12, y + 35])
            cv2.imshow("filter", frame)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")



    def beach_sunglass(self):
        overlay = cv2.imread('sunglass3.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 0.9), int(h * 0.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x + 12, y + 30])
            cv2.imshow("filter", frame)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")



    def tika(self):
        overlay = cv2.imread('tika.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 0.9), int(h * 0.6)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x + 12, y - 20])
            cv2.imshow("filter", frame)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")

    def convocation(self):
        overlay = cv2.imread('convocation.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 1.8), int(h * 1.5)))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x - 150, y - 170])
            cv2.imshow("filter", frame)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")



    def convocation_sunglass(self):
        overlay = cv2.imread('convocation.png', cv2.IMREAD_UNCHANGED)
        overlay1 = cv2.imread('sunglass1.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 1.8), int(h * 1.5)))
                overlay_resize1 = cv2.resize(overlay1, (int(w * 0.9), int(h * 0.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x - 150, y - 170])
                frame1 = cvzone.overlayPNG(frame, overlay_resize1, [x + 12, y + 35])
            cv2.imshow("filter", frame1)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")

    def sunglass_tika(self):
        overlay = cv2.imread('tika.png', cv2.IMREAD_UNCHANGED)
        overlay1 = cv2.imread('sunglass1.png', cv2.IMREAD_UNCHANGED)
        print(overlay.shape)
        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grayscale)
            for x, y, w, h in faces:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 0)
                overlay_resize = cv2.resize(overlay, (int(w * 0.9), int(h * 0.5)))
                overlay_resize1 = cv2.resize(overlay1, (int(w * 0.9), int(h * 0.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x + 15, y - 20])
                frame1 = cvzone.overlayPNG(frame, overlay_resize1, [x + 12, y + 35])
            cv2.imshow("filter", frame1)
            k = cv2.waitKey(33)
            if k == 27:
                break
        cv2.destroyWindow("filter")


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()