import os, sys, io
import M5
from M5 import *

from m5stack import * #UIFLOW1
from m5ui import * #UIFLOW1
from uiflow import * #UIFLOW1
from libs.m5_espnow import M5ESPNOW
import time





def send_cb(flag):
  global flag_cb,slave_mac,slave_data,run,cnt_succes,count_send,peer_mac,slave_ssid
  flag_cb = flag
  if flag_cb:
    cnt_succes = cnt_succes + 1
    label8.setText(str(cnt_succes))
  pass

def recv_cb(dummy):
  global flag_cb,slave_mac,slave_data,run,cnt_succes,count_send,peer_mac,slave_ssid
  slave_mac, slave_data = now.espnow_recv_str()
  label11.setText(str(slave_data))
  pass


def buttonA_wasPressed():
  global flag_cb, slave_mac, slave_data, run, cnt_succes, count_send, peer_mac, slave_ssid
  run = 1
  pass


def buttonC_wasPressed():
  global flag_cb, slave_mac, slave_data, run, cnt_succes, count_send, peer_mac, slave_ssid
  run = 0
  pass

def setup():

  M5.begin()
  Widgets.fillScreen(0x222222)

  flag_cb = None
  slave_mac = None
  slave_data = None
  run = None
  cnt_succes = None
  count_send = None
  peer_mac = None
  slave_ssid = None

  now = M5ESPNOW()

  title0 = M5Title(title="ESPNOW-MASTER", x=100, fgcolor=0xFFFFFF, bgcolor=0xff0000)
  label0 = M5TextBox(24, 75, "SLAVE MAC:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label1 = M5TextBox(125, 38, "label1", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label2 = M5TextBox(24, 109, "SEND COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label9 = M5TextBox(230, 219, "STOP", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label3 = M5TextBox(126, 75, "label3", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label10 = M5TextBox(24, 175, "REVC COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label4 = M5TextBox(25, 38, "SLAVE SSID:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label11 = M5TextBox(145, 175, "label11", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label5 = M5TextBox(146, 109, "label5", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label6 = M5TextBox(48, 219, "SEND", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label7 = M5TextBox(24, 144, "SUCCESS COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
  label8 = M5TextBox(174, 144, "label8", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

  peer_mac = None
  now.espnow_init(1, 1)
  count_send = 0
  cnt_succes = 0
  flag_cb = 0
  run = 0
  slave_ssid = 'M5_Slave'
  while peer_mac == None:
    peer_mac = now.espnow_scan(1, slave_ssid)
  

def loop():
  M5.update()
  label1.setText(str(slave_ssid))
  label3.setText(str(peer_mac))
  now.espnow_add_peer(peer_mac, 1, 0, False)
  now.espnow_send_cb(send_cb)
  now.espnow_recv_cb(recv_cb)
  while True:
    if run:
      count_send = count_send + 1
      now.espnow_send_data(1, str(count_send))
      label5.setText(str(count_send))
      wait_ms(1)
    wait_ms(2)


if __name__ == '__main__':
  try:
    setup()
    btnA.wasPressed(buttonA_wasPressed)
    btnC.wasPressed(buttonC_wasPressed)
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")














