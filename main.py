from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (310, 580)

sc = """
MDFloatLayout:
    md_bg_color: 1,1,1,1
    Carousel:
        id: carousel
        on_current_slide: app.current_slide(self.index)

        MDFloatLayout:
            Image:
                source: "Images/TC_Logo.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint: 1, .1


            MDFloatLayout:    
                Image:
                    source: "Images/Intro_T1.jpg"
                    pos_hint: {"center_x": .5, "center_y": .67}
                    size_hint: 1, .1

                MDFloatLayout:    
                    Image:
                        source: "Images/Splash-Screen/Splash_1.png"
                        pos_hint: {"center_x": .5, "center_y": .35}
                        size_hint: 1, .4

                    MDTextButton:
                        text: "Skip"
                        pos_hint: {"center_x": .88, "center_y": .95}
                        font_name: "Inter"
                        font_size: "13sp"
                        color: rgba(255,114,111,255)
                        on_release:
                            app.next()


        MDFloatLayout:
            Image:
                source: "Images/TC_Logo.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint: 1, .1    

            MDFloatLayout:    
                Image:
                    source: "Images/Intro - T1.png"
                    pos_hint: {"center_x": .5, "center_y": .67}
                    size_hint: 1, .1

                MDFloatLayout:    
                    Image:
                        source: "Images/Splash-Screen/Splash_2.png"
                        pos_hint: {"center_x": .5, "center_y": .35}
                        size_hint: 1, .4

                    MDTextButton:
                        text: "Skip"
                        pos_hint: {"center_x": .88, "center_y": .95}
                        font_name: "Inter"
                        font_size: "13sp"
                        color: rgba(255,114,111,255)
                        on_release:
                            app.next()


        MDFloatLayout:
            Image:
                source: "Images/TC_Logo.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint: 1, .1

            MDFloatLayout:    
                Image:
                    source: "Images/Intro - T2.png"
                    pos_hint: {"center_x": .5, "center_y": .67}
                    size_hint: 1, .1

                MDFloatLayout:    
                    Image:
                        source: "Images/Splash-Screen/Splash_3.png"
                        pos_hint: {"center_x": .5, "center_y": .35}
                        size_hint: 1, .4

                    MDTextButton:
                        text: "Skip"
                        pos_hint: {"center_x": .88, "center_y": .95}
                        font_name: "Inter"
                        font_size: "13sp"
                        color: rgba(255,114,111,255)
                        on_release:
                            app.next()


        MDFloatLayout:
            Image:
                source: "Images/TC_Logo.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint: 1, .1

            MDFloatLayout:    
                Image:
                    source: "Images/Intro - T3.png"
                    pos_hint: {"center_x": .5, "center_y": .67}
                    size_hint: 1, .1

                MDFloatLayout:    
                    Image:
                        source: "Images/Splash-Screen/Splash_4.png"
                        pos_hint: {"center_x": .5, "center_y": .40}
                        size_hint: 1, .4

                    Button:
                        text: "Create an Account"
                        background_color: 0,0,0,0
                        font_name: "Inter"
                        font_size: "15sp"
                        size_hint: .7, .075
                        pos_hint: {"center_x": .5, "center_y": .17}
                        canvas.before:
                            Color:
                                rgb: rgba(0,0,0,255)
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [15]

            MDTextButton:
                text: "Already have an account? Log - In"
                pos_hint: {"center_x": .5, "center_y": .1}
                font_name: "Inter"
                font_size: "13sp"
                color: rgba(255,114,111,255)
"""


class TourCeylon(MDApp):

    def build(self):
        return Builder.load_string(sc)

    def current_slide(self, index):
        pass

    def next(self):
        self.root.ids.carousel.load_next(mode="next")


if __name__ == "__main__":
    LabelBase.register(name="Inter", fn_regular="E:\PyCharm_Projects\SplashScren\FONTS\static\Inter-Regular.ttf")

    LabelBase.register(name="Inter", fn_regular="E:\PyCharm_Projects\SplashScren\FONTS\static\Inter-Bold.ttf")

TourCeylon().run()
