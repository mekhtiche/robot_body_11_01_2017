#!/usr/bin/python
import time
import tkFileDialog
import tkMessageBox
import tkSimpleDialog
from Tkinter import *
# import robot.servo.Adafruit_PWM_Servo_Driver.PWM as PWM
# from servo.Adafruit_PWM_Servo_Driver import PWM
# import thread
import rospy
from robot_body.msg import servoSet
from robot_body.msg import servoCmd
import pypot
import json
import numpy as np
import setNewHand
# ===========================================================================
# Example Code
# ===========================================================================
#DEBUG = 1
#Lpwm = PWM(0x41, 4) # , debug = True  # for debuging the code and see what it send from the bus
#Rpwm = PWM(0x40, 4) # 42
#Lpwm.setPWMFreq(30)
#Rpwm.setPWMFreq(30)
#global srl
#srl = serial.Serial('/dev/ttyACM1', 19200)
#time.sleep(3)
global RservoPub, LservoPub, rservoPub, lservoPub

RservoPub = rospy.Publisher('servo/Rcmd', servoSet, queue_size=10)
LservoPub = rospy.Publisher('servo/Lcmd', servoSet, queue_size=10)
rservoPub = rospy.Publisher('servo/rcmd', servoCmd, queue_size=10)
lservoPub = rospy.Publisher('servo/lcmd', servoCmd, queue_size=10)
Rcmd = servoSet()
Lcmd = servoSet()
cmd  = servoCmd()





def __init__(master, movement, robot = None ):

    # Set frequency to 60 Hz
#    master = Tk()
    master.geometry('915x855')
    master.title('SETTING THE HAND')
    rospy.init_node('Fingers_set', anonymous=True)
    title = Frame(master)
    title.grid(row=0, column=0, columnspan=3, sticky=W+E+N+S)
    info = Label(title, justify=LEFT, text='play the recorded sign using the slider in the blue section and set the hand configuration using \n'
                             'the sliders below than click "Set Pos" to record it, when you done all the hand sets click on \n'
                             '"Build & Play" to build the movement than save it. \n '
                             'you can also use "Delete before" and "Delete After" to delete unnecessary frames.')
    info.pack()
    lefthand = Frame(master, bg = "red")
    lefthand.grid(row=1, column=0)
    righthand = Frame(master, bg = "green")
    righthand.grid(row=1, column=2)
    medButt = Frame(master,bg = "blue")
    medButt.grid(row=1, column=1)
    buttfram = Frame(master, bg="blue")
    buttfram.grid(row=2, column=0, columnspan=3, sticky=W+E+N+S)
    master.closing = False
    master.movement = movement
    motorsName = movement['actors_NAME']
    if robot is None:
        master.closing = True
        print 'loading robot'
        master.robot = pypot.robot.from_config(pypot.robot.config.robot_config, True, True, False,
                                               activemotors=motorsName)
        print 'robot loaded succefful'
    else:
        master.robot = robot

    for m in master.robot.motors:
        m.compliant = False
    for m in master.robot.Dead_motors:
        m.goal_position = 0

    with open('/home/odroid/catkin_ws/src/robot_body/recording/Poppy_torso.json', 'r') as f:
        config = json.load(f)
    Rcfg = config['Right_Setting']
    Lcfg = config['Left_Setting']


#//////////////////////////////////////////////////////////////////////////LEFT  ARM////////////////////////////////////////////////////////////////////////
    def LgetValue1(event):
            #print(master.Lwrist_V.get())
            cmd.motor = 1
            cmd.command = master.Lwrist_V.get()
            lservoPub.publish(cmd)

    master.Lwrist_V = Scale(lefthand, label = "wrist_V N:1", from_=Lcfg['1'][0], to =Lcfg['1'][1], orient = HORIZONTAL, length = 300, command = LgetValue1)
    master.Lwrist_V.set(200)
    master.Lwrist_V.pack()

    def LgetValue2(event):
            #print(master.Lwrist_H.get())
            cmd.motor = 2
            cmd.command = master.Lwrist_H.get()
            lservoPub.publish(cmd)

    master.Lwrist_H = Scale(lefthand, label = "wrist_H N:2", from_=Lcfg['2'][0], to =Lcfg['2'][1], orient = HORIZONTAL, length = 300, command = LgetValue2)
    master.Lwrist_H.set(200)
    master.Lwrist_H.pack()

    def LgetValue3(event):
            #print(master.Lthump_J.get())
            cmd.motor = 3
            cmd.command = master.Lthump_J.get()
            lservoPub.publish(cmd)

    master.Lthump_J = Scale(lefthand, label = "Thump_J N:3", from_=Lcfg['3'][0], to =Lcfg['3'][1], orient = HORIZONTAL, length = 300, command = LgetValue3)
    master.Lthump_J.set(202)
    master.Lthump_J.pack()

    def LgetValue4(event):
            #print(master.Lthump.get())
            cmd.motor = 4
            cmd.command = master.Lthump.get()
            lservoPub.publish(cmd)

    master.Lthump = Scale(lefthand, label = "Thump N:4", from_=Lcfg['4'][0], to =Lcfg['4'][1], orient = HORIZONTAL, length = 300, command = LgetValue4)
    master.Lthump.set(280)
    master.Lthump.pack()

    def LgetValue5(event):
            #print(master.LOpen.get())
            cmd.motor = 5
            cmd.command = master.LOpen.get()
            lservoPub.publish(cmd)

    master.LOpen = Scale(lefthand, label = "Open N:5", from_=Lcfg['5'][0], to =Lcfg['5'][1], orient = HORIZONTAL, length = 300, command = LgetValue5)
    master.LOpen.set(233)
    master.LOpen.pack()

    def LgetValue6(event):
            #print(master.Lindex.get())
            cmd.motor = 6
            cmd.command = master.Lindex.get()
            lservoPub.publish(cmd)

    master.Lindex = Scale(lefthand, label = "Index N:6", from_=Lcfg['6'][0], to =Lcfg['6'][1], orient = HORIZONTAL, length = 300, command = LgetValue6)
    master.Lindex.set(270)
    master.Lindex.pack()

    def LgetValue7(event):
            #print(master.Lmajor.get())
            cmd.motor = 7
            cmd.command = master.Lmajor.get()
            lservoPub.publish(cmd)

    master.Lmajor = Scale(lefthand, label = "Major N:7", from_=Lcfg['7'][0], to =Lcfg['7'][1], orient = HORIZONTAL, length = 300, command = LgetValue7)
    master.Lmajor.set(115)
    master.Lmajor.pack()

    def LgetValue8(event):
            #print(master.Lring.get())
            cmd.motor = 8
            cmd.command = master.Lring.get()
            lservoPub.publish(cmd)

    master.Lring = Scale(lefthand, label = "Ring N:8", from_=Lcfg['8'][0], to =Lcfg['8'][1], orient = HORIZONTAL, length = 300, command = LgetValue8)
    master.Lring.set(110)
    master.Lring.pack()

    def LgetValue9(event):
            #print(master.Lauri.get())
            cmd.motor = 9
            cmd.command = master.Lauri.get()
            lservoPub.publish(cmd)

    master.Lauri = Scale(lefthand, label = "Auriculaire N:9", from_=Lcfg['9'][0], to =Lcfg['9'][1], orient = HORIZONTAL, length = 300, command = LgetValue9)
    master.Lauri.set(110)
    master.Lauri.pack()
#//////////////////////////////////////////////////////////////////////////LEFT  ARM////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////////////////////RIGHT ARM////////////////////////////////////////////////////////////////////////
    def RgetValue1(event):
        # print(master.Rwrist_V.get())
        cmd.motor = 1
        cmd.command = master.Rwrist_V.get()
        rservoPub.publish(cmd)


    master.Rwrist_V = Scale(righthand, label="wrist_V N:1", from_=Rcfg['1'][0], to=Rcfg['1'][1], orient=HORIZONTAL, length=300,
                            command=RgetValue1)
    master.Rwrist_V.set(200)
    master.Rwrist_V.pack()


    def RgetValue2(event):
        # print(master.Rwrist_H.get())
        cmd.motor = 2
        cmd.command = master.Rwrist_H.get()
        rservoPub.publish(cmd)


    master.Rwrist_H = Scale(righthand, label="wrist_H N:2", from_=Rcfg['2'][0], to=Rcfg['2'][1], orient=HORIZONTAL, length=300,
                            command=RgetValue2)
    master.Rwrist_H.set(200)
    master.Rwrist_H.pack()


    def RgetValue3(event):
        # print(master.Rthump_J.get())
        cmd.motor = 3
        cmd.command = master.Rthump_J.get()
        rservoPub.publish(cmd)


    master.Rthump_J = Scale(righthand, label="Thump_J N:3", from_=Rcfg['3'][0], to=Rcfg['3'][1], orient=HORIZONTAL, length=300,
                            command=RgetValue3)
    master.Rthump_J.set(202)
    master.Rthump_J.pack()


    def RgetValue4(event):
        # print(master.Rthump.get())
        cmd.motor = 4
        cmd.command = master.Rthump.get()
        rservoPub.publish(cmd)


    master.Rthump = Scale(righthand, label="Thump N:4", from_=Rcfg['4'][0], to=Rcfg['4'][1], orient=HORIZONTAL, length=300, command=RgetValue4)
    master.Rthump.set(280)
    master.Rthump.pack()


    def RgetValue5(event):
        # print(master.ROpen.get())
        cmd.motor = 5
        cmd.command = master.ROpen.get()
        rservoPub.publish(cmd)


    master.ROpen = Scale(righthand, label="Open N:5", from_=Rcfg['5'][0], to=Rcfg['5'][1], orient=HORIZONTAL, length=300, command=RgetValue5)
    master.ROpen.set(233)
    master.ROpen.pack()


    def RgetValue6(event):
        # print(master.Rindex.get())
        cmd.motor = 6
        cmd.command = master.Rindex.get()
        rservoPub.publish(cmd)


    master.Rindex = Scale(righthand, label="Index N:6", from_=Rcfg['6'][0], to=Rcfg['6'][1], orient=HORIZONTAL, length=300, command=RgetValue6)
    master.Rindex.set(270)
    master.Rindex.pack()


    def RgetValue7(event):
        # print(master.Rmajor.get())
        cmd.motor = 7
        cmd.command = master.Rmajor.get()
        rservoPub.publish(cmd)


    master.Rmajor = Scale(righthand, label="Major N:7", from_=Rcfg['7'][0], to=Rcfg['7'][1], orient=HORIZONTAL, length=300, command=RgetValue7)
    master.Rmajor.set(115)
    master.Rmajor.pack()


    def RgetValue8(event):
        # print(master.Rring.get())
        cmd.motor = 8
        cmd.command = master.Rring.get()
        rservoPub.publish(cmd)


    master.Rring = Scale(righthand, label="Ring N:8", from_=Rcfg['8'][0], to=Rcfg['8'][1], orient=HORIZONTAL, length=300, command=RgetValue8)
    master.Rring.set(110)
    master.Rring.pack()


    def RgetValue9(event):
        # print(master.Rauri.get())
        cmd.motor = 9
        cmd.command = master.Rauri.get()
        rservoPub.publish(cmd)


    master.Rauri = Scale(righthand, label="Auriculaire N:9", from_=Rcfg['9'][0], to=Rcfg['9'][1], orient=HORIZONTAL, length=300,
                         command=RgetValue9)
    master.Rauri.set(110)
    master.Rauri.pack()
#//////////////////////////////////////////////////////////////////////////RIGHT ARM////////////////////////////////////////////////////////////////////////

    def callback(Lcommand=None, Rcommand=None):

        if Lcommand is not None:
            Lcmd = Lcommand
            LservoPub.publish(Lcmd)
        if Rcommand is not None:
            Rcmd = Rcommand
            RservoPub.publish(Rcmd)


    def setframe(event):
        master.frm = master.recSlider.get()
        id = 0
        for m in master.robot.Active_motors:
            m.goal_position = master.movement['position'][str(master.frm)]['Robot'][id]
            id += 1
        if master.Lrec.get() == 0:
            callback(master.movement['position'][str(master.frm)]['Left_hand'], None)

        if master.Rrec.get() == 0:
            callback(None, master.movement['position'][str(master.frm)]['Right_hand'])


    def DelBefor():

        if tkMessageBox.askyesno(title='Warning', message='Warning: Do you want to delete the sequanses Befor the the frame ' + str(master.frm) + '?'):
            mov = {} #master.movement['position']




            newfrm=0
            for frm in range(master.frm, master.movement['frame_number'], 1):
                mov[str(newfrm)] = master.movement['position'][str(frm)]
                newfrm +=1
            master.movement.pop('position')
            master.movement['position'] = mov
            #master.movement['position'] = master.movement['position'][str(0):str(master.frm)]
            master.movement['frame_number']=newfrm
            master.recSlider.config(to=master.movement['frame_number'] - 1)
            master.recSlider.set(0)
            save.config(state=NORMAL)

    def DelAfter():

        if tkMessageBox.askyesno(title='Warning', message='Warning: Do you want to delete the sequanses After the the frame '+ str(master.frm) + '?'):
            for frm in range(master.frm, master.movement['frame_number'], 1):
                master.movement['position'].pop(str(frm))

            master.movement['frame_number'] = master.frm
            master.recSlider.config(to=master.movement['frame_number'] - 1)
            save.config(state=NORMAL)

    def closecall():
        callback([0]*9, [0]*9)

        if master.closing:
            for m in master.robot.motors:
                m.compliant = True
            master.robot.close()
	else:
	    for m in master.robot.Active_motors:
                m.compliant = True

        master.destroy()

    def savecall():

        print 'saving movement'
        saveFile = tkFileDialog.asksaveasfilename()
        if not saveFile:
            return None
        with open(saveFile, "w") as record:
            json.dump(master.movement, record)
        print 'saved'

    def setcall():
        print 'seting'
        master.lefthandpos = [master.Lwrist_V.get(), master.Lwrist_H.get(), master.Lthump_J.get(), master.Lthump.get(), master.LOpen.get(),
               master.Lindex.get(), master.Lmajor.get(), master.Lring.get(), master.Lauri.get()]
        master.righthandpos = [master.Rwrist_V.get(), master.Rwrist_H.get(), master.Rthump_J.get(), master.Rthump.get(), master.ROpen.get(),
                              master.Rindex.get(), master.Rmajor.get(), master.Rring.get(), master.Rauri.get()]
        master.movement['position'][str(master.frm)]['Left_hand'] = master.lefthandpos
        master.movement['position'][str(master.frm)]['Right_hand'] = master.righthandpos
        if master.frm not in master.setted_frame:
            master.setted_frame.append(master.frm)
            list(set(master.setted_frame))  # sort the list
        if ~master.needToBuild:
            master.needToBuild = True

        clear.config(state=NORMAL)
        print 'done'

    def find_smth_win():
        winSize = master.setted_frame[len(master.setted_frame)-1] - master.setted_frame[0]
        for i in range(len(master.setted_frame)-1):
            winSize = min(master.setted_frame[i+1]-master.setted_frame[i], winSize)
        return winSize;

    def buildPlay():
        if master.needToBuild:
            print 'building'
            #if master.setted_frame[0] != 0:
             #   master.setted_frame.insert(0, 0)
                #master.movement['position'][str(0)]['Left_hand'] = [200] * 9
                #master.movement['position'][str(0)]['Right_hand'] = [200] * 9
            if master.setted_frame[len(master.setted_frame) - 1] != master.movement['frame_number']:
                master.setted_frame.append(master.movement['frame_number'])
            index = 1
            while index < len(master.setted_frame):
                start = master.setted_frame[index - 1]
                stop = master.setted_frame[index]
                #        if (not master.movement['position'][str(0)]['Left_hand'])|(not master.movement['position'][str(0)]['Right_hand']):
                #            master.movement['position'][str(0)]['Left_hand'] = [200]*9
                #            master.movement['position'][str(0)]['Right_hand'] = [200]*9

                for frame in range(start + 1, stop, 1):
                    master.movement['position'][str(frame)]['Left_hand'] = master.movement['position'][str(start)]['Left_hand']
                    master.movement['position'][str(frame)]['Right_hand'] = master.movement['position'][str(start)]['Right_hand']
                index += 1
            print 'Done Building'

            print 'Smoothing the motion'

            win = find_smth_win()/int(2) if master.autoSmth.get() == 1 else master.smooth.get()
            for frame in range(master.movement['frame_number']):
                master.movement['position'][str(frame)]['Left_hand'] = np.mean([master.movement['position'][str(frame + i)]['Left_hand'] for i in range(min(master.movement['frame_number'] - frame-1, win)+1)], 0)
                master.movement['position'][str(frame)]['Right_hand'] = np.mean([master.movement['position'][str(frame + i)]['Right_hand'] for i in range(min(master.movement['frame_number'] - frame-1, win)+1)], 0)
                master.movement['position'][str(frame)]['Left_hand'] = list(np.int_(master.movement['position'][str(frame)]['Left_hand']))
                master.movement['position'][str(frame)]['Right_hand'] = list(np.int_(master.movement['position'][str(frame)]['Right_hand']))
            print 'Done Smoothing'
            master.needToBuild = False
            save.config(state=NORMAL)

        for m in master.robot.motors:
            m.compliant = False

        time.sleep(0.5)
        print 'Playing'
        for frame in range(master.frm, master.movement['frame_number']):
            id = 0
            for m in master.robot.Active_motors:
                m.goal_position = master.movement['position'][str(frame)]['Robot'][id]
                id += 1
            callback(master.movement['position'][str(frame)]['Left_hand'], master.movement['position'][str(frame)]['Right_hand'])
            time.sleep(1/float(master.movement['freq']))
        master.recSlider.set(frame)
        print 'Done'

    def clearcall():

        master.setted_frame = []

        master.needToBuild = False









    def setauto():
        master.smooth.config(state=NORMAL) if master.autoSmth.get() == 0 else master.smooth.config(state=DISABLED)

    def saveL():
        lefthandpos = [master.Lwrist_V.get(), master.Lwrist_H.get(), master.Lthump_J.get(), master.Lthump.get(),
                              master.LOpen.get(), master.Lindex.get(), master.Lmajor.get(), master.Lring.get(), master.Lauri.get()]
        name = tkSimpleDialog.askstring('Left Hand set name', 'Please enter the name of the Left hand set')
        if name:
            handSetting["Left"][name] = lefthandpos
            L_handSets.insert(len(handSetting["Left"]), name)
        else:
            print "you Should enter the mane of the hand set"

        with open("/home/odroid/catkin_ws/src/robot/recording/handSetting.json", "w") as h:
            json.dump(handSetting, h)

    def saveR():
        righthandpos = [master.Rwrist_V.get(), master.Rwrist_H.get(), master.Rthump_J.get(), master.Rthump.get(),
                                master.ROpen.get(), master.Rindex.get(), master.Rmajor.get(), master.Rring.get(), master.Rauri.get()]
        name = tkSimpleDialog.askstring('Right Hand set name', 'Please enter the name of the Right hand set')
        if name:
            handSetting["Right"][name] = righthandpos
            R_handSets.insert(len(handSetting["Right"]), name)
        else:
            print "you Should enter the mane of the hand set"

        with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as h:
            json.dump(handSetting, h)

    def Lrel():
        callback([50] * 9, None)
        # srl.write(struct.pack('cBBBBBBBBB', "L", 50, 50, 50, 50, 50, 50, 50, 50, 50))

    def Rrel():
        callback(None, [50] * 9)
        # srl.write(struct.pack('cBBBBBBBBB', "R", 50, 50, 50, 50, 50, 50, 50, 50, 50))

    close = Button(buttfram, text='Close', width=10, command=closecall)
    close.grid(row=6, column=4, sticky=E)


    rel = Button(lefthand, text="Release",width = 10, command =  Lrel)
    rel.pack(side=LEFT)
    LSET = Button(lefthand, text=">>", width=10, command=saveL)
    LSET.pack(side=RIGHT)
    master.Lrec = IntVar(lefthand,value=0)
    recL = Checkbutton(lefthand, text='Record Mode', variable=master.Lrec)
    recL.pack()

    rer = Button(righthand, text="Release", width=10, command= Rrel)
    rer.pack(side=RIGHT)
    RSET = Button(righthand, text="<<", width=10, command=saveR)
    RSET.pack(side=LEFT)
    master.Rrec = IntVar(righthand, value=0)
    recR = Checkbutton(righthand, text='Record Mode', variable=master.Rrec)
    recR.pack()


    L_handSets = Listbox(medButt, height=10, width=15)
    L_handSets.grid(row=2, column=0, columnspan=2)
    R_handSets = Listbox(medButt, height=10, width=15)
    R_handSets.grid(row=2, column=2, columnspan=2)
    try:
        with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "r") as f:
            handSetting = json.load(f)

        for name, pos in handSetting["Left"].items():

            L_handSets.insert(END, str(name))
        for name, pos in handSetting["Right"].items():

            R_handSets.insert(END, str(name))
    except Exception, err:
        print err


    def setleft():
        if list(L_handSets.curselection()):
            left_values = handSetting["Left"][L_handSets.get(L_handSets.curselection())]
            callback(left_values)
            master.Lwrist_V.set(left_values[0])
            master.Lwrist_H.set(left_values[1])
            master.Lthump_J.set(left_values[2])
            master.Lthump.set(left_values[3])
            master.LOpen.set(left_values[4])
            master.Lindex.set(left_values[5])
            master.Lmajor.set(left_values[6])
            master.Lring.set(left_values[7])
            master.Lauri.set(left_values[8])
        else:
            print "No setting is selected"

    def setright():
        if list(R_handSets.curselection()):
            right_values = handSetting["Right"][R_handSets.get(R_handSets.curselection())]
            callback(None, right_values)
            master.Rwrist_V.set(right_values[0])
            master.Rwrist_H.set(right_values[1])
            master.Rthump_J.set(right_values[2])
            master.Rthump.set(right_values[3])
            master.ROpen.set(right_values[4])
            master.Rindex.set(right_values[5])
            master.Rmajor.set(right_values[6])
            master.Rring.set(right_values[7])
            master.Rauri.set(right_values[8])
        else:
            print "No setting is selected"

    def setNhand():
        setupFrame = Toplevel()
        setupFrame.grab_set()
        setupFrame.transient(master)
        setuphands = setNewHand.__init__(setupFrame, rservoPub, lservoPub)


    def refresh():

        with open('/home/odroid/catkin_ws/src/robot/recording/Poppy_torso.json', 'r') as f:
            config = json.load(f)
        Rcfg = config['Right_Setting']
        Lcfg = config['Left_Setting']
        master.Lwrist_V.config(from_=Lcfg['1'][0], to=Lcfg['1'][1])
        master.Lwrist_H.config(from_=Lcfg['2'][0], to=Lcfg['2'][1])
        master.Lthump_J.config(from_=Lcfg['3'][0], to=Lcfg['3'][1])
        master.Lthump.config(from_=Lcfg['4'][0], to=Lcfg['4'][1])
        master.LOpen.config(from_=Lcfg['5'][0], to=Lcfg['5'][1])
        master.Lindex.config(from_=Lcfg['6'][0], to=Lcfg['6'][1])
        master.Lmajor.config(from_=Lcfg['7'][0], to=Lcfg['7'][1])
        master.Lring.config(from_=Lcfg['8'][0], to=Lcfg['8'][1])
        master.Lauri.config(from_=Lcfg['9'][0], to=Lcfg['9'][1])

        master.Rwrist_V.config(from_=Rcfg['1'][0], to=Rcfg['1'][1])
        master.Rwrist_H.config(from_=Rcfg['2'][0], to=Rcfg['2'][1])
        master.Rthump_J.config(from_=Rcfg['3'][0], to=Rcfg['3'][1])
        master.Rthump.config(from_=Rcfg['4'][0], to=Rcfg['4'][1])
        master.ROpen.config(from_=Rcfg['5'][0], to=Rcfg['5'][1])
        master.Rindex.config(from_=Rcfg['6'][0], to=Rcfg['6'][1])
        master.Rmajor.config(from_=Rcfg['7'][0], to=Rcfg['7'][1])
        master.Rring.config(from_=Rcfg['8'][0], to=Rcfg['8'][1])
        master.Rauri.config(from_=Rcfg['9'][0], to=Rcfg['9'][1])

    def L_DEL():

        if list(L_handSets.curselection()):
            if tkMessageBox.askyesno(title='Warning', message='do you want to DELETE ' + L_handSets.get(L_handSets.curselection()) + ' ?'):
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json") as f:
                    handSetting = json.load(f)
                del handSetting["Left"][L_handSets.get(L_handSets.curselection())]
                L_handSets.delete(L_handSets.curselection())
                with open("/home/odroid/catkin_ws/src/robot/recording/handSetting.json", "w") as f:
                    json.dump(handSetting, f)
        else:
            print "No setting is selected"


    def R_DEL():

        if list(R_handSets.curselection()):
            if tkMessageBox.askyesno(title='Warning', message='do you want to DELETE ' + R_handSets.get(R_handSets.curselection()) + ' ?'):
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "r") as f:
                    handSetting = json.load(f)
                del handSetting["Right"][R_handSets.get(R_handSets.curselection())]
                R_handSets.delete(R_handSets.curselection())
                with open("/home/odroid/catkin_ws/src/robot_body/recording/handSetting.json", "w") as f:
                    json.dump(handSetting, f)
        else:
            print "No setting is selected"







    NewHandSetupFrame = Frame(medButt, bg="blue")
    NewHandSetupFrame.grid(row=0, column=0, columnspan=4, sticky=W + E + N + S)

    NewHandSetup = Button(NewHandSetupFrame,text = "Setup New Hand/s", width=13, command=setNhand)
    NewHandSetup.grid(row=0, column=0)
    Refresh = Button(NewHandSetupFrame, text = "Refresh", width = 13, command = refresh)
    Refresh.grid(row=0, column=2)

    leftSet = Button(medButt, text="<<", width=5, command=setleft)
    leftSet.grid(row=3, column=0, sticky=E)
    LDEL = Button(medButt, text="DEL", width=5, command=L_DEL)
    LDEL.grid(row=3, column=1, sticky=W)

    rightSet = Button(medButt, text=">>", width=5, command=setright)
    rightSet.grid(row=3, column=3, sticky=W)
    RDEL = Button(medButt, text="DEL", width=5, command=R_DEL)
    RDEL.grid(row=3, column=2, sticky=E)

    master.steps = StringVar(master, value=1)
    master.frm = 0
    master.recSlider = Scale(buttfram, from_=0, to=master.movement['frame_number']-1, orient=HORIZONTAL, length=910, command=setframe)
    master.recSlider.set(0)
    master.recSlider.grid(row=0, column=0, columnspan=5)
    del_befor = Button(buttfram, text='Delete Before', width=10, command=DelBefor)
    del_befor.grid(row=1, column=0)
    del_after = Button(buttfram, text='Delete After', width=10, command=DelAfter)
    del_after.grid(row=1, column=4)
    master.autoSmth = IntVar(master, value=1)
    master.autoSmooth = Checkbutton(buttfram, text='Auto Smoothing', variable=master.autoSmth, command=setauto)
    master.autoSmooth.grid(row=2, column=0)
    master.smooth = Scale(buttfram, label = "Smoothing:", from_=0, to=master.movement['frame_number']-1, takefocus=1, orient=HORIZONTAL, length=250)
    master.smooth.set(min(30, master.movement['frame_number'] - 1))
    master.smooth.grid(row=2, column=1, columnspan=2, sticky=W)
    master.smooth.config(state=DISABLED)
    setpos = Button(buttfram, text='Set Pos', width=10, command=setcall)
    setpos.grid(row=3, column=0)
    build = Button(buttfram, text='Build & play', width=10, command=buildPlay)
    build.grid(row=4, column=0)
    save = Button(buttfram, text='Save', width=10, command=savecall)
    save.grid(row=5, column=0)
    save.config(state=DISABLED)
    clear = Button(buttfram, text='Clear', width=10, command=clearcall)
    clear.grid(row=6, column=0)
    clear.config(state=DISABLED)

    msg = Label(buttfram, height=6, justify=LEFT, text='<----- Click here to record a hand set.\n\n'
                                                        '<----- Click here to build or play the recording. \n\n'
                                                        '<----- Click here to save.')
    msg.grid(row=3, column=1, rowspan=3, sticky=W)
    master.needToBuild = False
    master.setted_frame = []


    actors = ['abs_z', 'bust_y', 'bust_x', 'head_z', 'head_y', 'l_shoulder_y', 'l_shoulder_x', 'l_arm_z', 'l_elbow_y', 'l_forearm_z', 'r_shoulder_y', 'r_shoulder_x', 'r_arm_z', 'r_elbow_y']
    #print actors



    id = 0
    for m in master.robot.Active_motors:
        m.goal_position = master.movement['position'][str(master.frm)]['Robot'][id]
        id += 1
    #callback(master.movement['position'][str(master.frm)]['Left_hand'], master.movement['position'][str(master.frm)]['Right_hand'])




#mainloop()

