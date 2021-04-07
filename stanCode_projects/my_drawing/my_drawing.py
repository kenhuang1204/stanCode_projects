"""
File: my_drawing.py
Name: 黃科諺
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Meet Snorlax (卡比獸) of stanCode! He dreams of Python when he sleeps. Be like Snorlax.
    """
    window = GWindow(width=300, height=300)
    face_outer = GOval(120, 75, x=(window.width-120)/2, y=50)
    face_outer.filled = True
    face_outer.fill_color = 'darkcyan'
    face_outer.color = 'darkcyan'
    window.add(face_outer)
    face_inner = GOval(100, 65, x=(window.width-100)/2, y=60)
    face_inner.filled = True
    face_inner.fill_color = 'lightsalmon'
    face_inner.color = 'lightsalmon'
    window.add(face_inner)
    forehead = GPolygon()
    forehead.add_vertex((135, 60))
    forehead.add_vertex((165, 60))
    forehead.add_vertex((150, 68))
    forehead.filled = True
    forehead.fill_color = 'darkcyan'
    forehead.color = 'darkcyan'
    window.add(forehead)
    r_ear = GPolygon()
    r_ear.add_vertex((113, 35))
    r_ear.add_vertex((95, 75))
    r_ear.add_vertex((140, 50))
    r_ear.filled = True
    r_ear.fill_color = 'darkcyan'
    r_ear.color = 'darkcyan'
    window.add(r_ear)
    l_ear = GPolygon()
    l_ear.add_vertex((187, 35))
    l_ear.add_vertex((205, 75))
    l_ear.add_vertex((160, 50))
    l_ear.filled = True
    l_ear.fill_color = 'darkcyan'
    l_ear.color = 'darkcyan'
    window.add(l_ear)
    r_eye = GLine (120, 75, 140, 75)
    window.add(r_eye)
    l_eye = GLine(180, 75, 160, 75)
    window.add(l_eye)
    mouth = GLine(135, 85, 165, 85)
    window.add(mouth)
    r_tooth = GPolygon()
    r_tooth.add_vertex((135, 84))
    r_tooth.add_vertex((139, 84))
    r_tooth.add_vertex((137, 80))
    r_tooth.filled = True
    r_tooth.fill_color = 'white'
    r_tooth.color = 'white'
    window.add(r_tooth)
    l_tooth = GPolygon()
    l_tooth.add_vertex((165, 84))
    l_tooth.add_vertex((161, 84))
    l_tooth.add_vertex((163, 80))
    l_tooth.filled = True
    l_tooth.fill_color = 'white'
    l_tooth.color = 'white'
    window.add(l_tooth)
    r_arm = GOval(100, 45, x=25, y=98)
    r_arm.filled = True
    r_arm.fill_color = 'darkcyan'
    r_arm.color = 'darkcyan'
    window.add(r_arm)
    l_arm = GOval(100, 45, x=175, y=98)
    l_arm.filled = True
    l_arm.fill_color = 'darkcyan'
    l_arm.color = 'darkcyan'
    window.add(l_arm)
    body = GOval(200, 160, x=(window.width - 200) / 2, y=95)
    body.filled = True
    body.fill_color = 'darkcyan'
    body.color = 'darkcyan'
    window.add(body)
    belly = GOval(176, 120, x=(window.width - 176) / 2, y=95)
    belly.filled = True
    belly.fill_color = 'lightsalmon'
    window.add(belly)
    r_claw1 = GPolygon()
    r_claw1.add_vertex((38, 100))
    r_claw1.add_vertex((44, 102))
    r_claw1.add_vertex((40, 106))
    r_claw1.filled = True
    r_claw1.fill_color = 'white'
    window.add(r_claw1)
    r_claw2 = GPolygon()
    r_claw2.add_vertex((32, 102))
    r_claw2.add_vertex((38, 104))
    r_claw2.add_vertex((35, 108))
    r_claw2.filled = True
    r_claw2.fill_color = 'white'
    window.add(r_claw2)
    r_claw3 = GPolygon()
    r_claw3.add_vertex((28, 104))
    r_claw3.add_vertex((34, 106))
    r_claw3.add_vertex((31, 110))
    r_claw3.filled = True
    r_claw3.fill_color = 'white'
    window.add(r_claw3)
    r_claw4 = GPolygon()
    r_claw4.add_vertex((24, 109))
    r_claw4.add_vertex((30, 111))
    r_claw4.add_vertex((27, 115))
    r_claw4.filled = True
    r_claw4.fill_color = 'white'
    window.add(r_claw4)
    r_claw5 = GPolygon()
    r_claw5.add_vertex((19, 122))
    r_claw5.add_vertex((25, 121))
    r_claw5.add_vertex((28, 127))
    r_claw5.filled = True
    r_claw5.fill_color = 'white'
    window.add(r_claw5)
    l_claw1 = GPolygon()
    l_claw1.add_vertex((262, 100))
    l_claw1.add_vertex((256, 102))
    l_claw1.add_vertex((260, 106))
    l_claw1.filled = True
    l_claw1.fill_color = 'white'
    window.add(l_claw1)
    l_claw2 = GPolygon()
    l_claw2.add_vertex((268, 102))
    l_claw2.add_vertex((262, 104))
    l_claw2.add_vertex((265, 108))
    l_claw2.filled = True
    l_claw2.fill_color = 'white'
    window.add(l_claw2)
    l_claw3 = GPolygon()
    l_claw3.add_vertex((272, 104))
    l_claw3.add_vertex((266, 106))
    l_claw3.add_vertex((269, 110))
    l_claw3.filled = True
    l_claw3.fill_color = 'white'
    window.add(l_claw3)
    r_claw4 = GPolygon()
    r_claw4.add_vertex((276, 109))
    r_claw4.add_vertex((270, 111))
    r_claw4.add_vertex((273, 115))
    r_claw4.filled = True
    r_claw4.fill_color = 'white'
    window.add(r_claw4)
    r_claw5 = GPolygon()
    r_claw5.add_vertex((281, 122))
    r_claw5.add_vertex((275, 121))
    r_claw5.add_vertex((272, 127))
    r_claw5.filled = True
    r_claw5.fill_color = 'white'
    window.add(r_claw5)
    r_foot = GOval(65, 60, x=50, y=220)
    r_foot.filled = True
    r_foot.fill_color = 'lightsalmon'
    r_foot.color = 'lightsalmon'
    window.add(r_foot)
    r_palm = GOval(45, 40, x=65, y=235)
    r_palm.filled = True
    r_palm.fill_color = 'Chocolate'
    r_palm.color = 'Chocolate'
    window.add(r_palm)
    r_nail1 = GPolygon()
    r_nail1.add_vertex((80, 210))
    r_nail1.add_vertex((88, 223))
    r_nail1.add_vertex((78, 224))
    r_nail1.filled = True
    r_nail1.fill_color = 'white'
    window.add(r_nail1)
    r_nail2 = GPolygon()
    r_nail2.add_vertex((52, 220))
    r_nail2.add_vertex((65, 228))
    r_nail2.add_vertex((57, 235))
    r_nail2.filled = True
    r_nail2.fill_color = 'white'
    window.add(r_nail2)
    r_nail3 = GPolygon()
    r_nail3.add_vertex((43, 250))
    r_nail3.add_vertex((54, 248))
    r_nail3.add_vertex((52, 258))
    r_nail3.filled = True
    r_nail3.fill_color = 'white'
    window.add(r_nail3)
    l_foot = GOval(65, 60, x=185, y=220)
    l_foot.filled = True
    l_foot.fill_color = 'lightsalmon'
    l_foot.color = 'lightsalmon'
    window.add(l_foot)
    l_palm = GOval(45, 40, x=190, y=235)
    l_palm.filled = True
    l_palm.fill_color = 'Chocolate'
    l_palm.color = 'Chocolate'
    window.add(l_palm)
    l_nail1 = GPolygon()
    l_nail1.add_vertex((220, 210))
    l_nail1.add_vertex((212, 223))
    l_nail1.add_vertex((222, 224))
    l_nail1.filled = True
    l_nail1.fill_color = 'white'
    window.add(l_nail1)
    r_nail2 = GPolygon()
    r_nail2.add_vertex((248, 220))
    r_nail2.add_vertex((235, 228))
    r_nail2.add_vertex((243, 235))
    r_nail2.filled = True
    r_nail2.fill_color = 'white'
    window.add(r_nail2)
    r_nail3 = GPolygon()
    r_nail3.add_vertex((257, 250))
    r_nail3.add_vertex((246, 248))
    r_nail3.add_vertex((248, 258))
    r_nail3.filled = True
    r_nail3.fill_color = 'white'
    window.add(r_nail3)
    word = GLabel('stanCode', x=123, y=185)
    word.font = '-8-bold'
    window.add(word)
    bubble1 = GOval(10, 10, x=140, y=35)
    window.add(bubble1)
    bubble2 = GOval(15, 15, x=155, y=23)
    window.add(bubble2)
    bubble3 = GOval(20, 20, x=175, y=12)
    window.add(bubble3)
    bubble4 = GOval(95, 85, x=200, y=5)
    window.add(bubble4)
    word2 = GLabel('Python', x=207, y=50)
    word2.font = 'Courier-18'
    window.add(word2)
    word3 = GLabel('Python', x=220, y=80)
    word3.font = 'Courier-13'
    window.add(word3)
    word4 = GLabel('Python', x=242, y=60)
    word4.font = 'Courier-8'
    window.add(word4)










if __name__ == '__main__':
    main()
