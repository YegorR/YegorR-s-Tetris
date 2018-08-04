import pygame
from constant import USER_EVENT
from threading import Thread
from time import sleep

import logging


class Timer(Thread):
    def __init__(self, event, period):
        Thread.__init__(self)
        self._event = event
        self._period = period
        self._active = False

    def run(self):
        logging.info("Таймер сообщения "+str(self._event)+" запущен.")
        self._active = True
        while self._active:
            sleep(self._period / 1000)
            if self._active:
                pygame.event.post(pygame.event.Event(USER_EVENT, {'user_type': self._event}))
        logging.info("Таймер сообщения " + str(self._event) + " выключен.")

    def destroy(self):
        self._active = False


class TimerMgr:
    def __init__(self):
        self._timers = dict()

    def set_timer(self, event, period):
        self._timers[event] = Timer(event, period)
        self._timers[event].start()

    def delete_timer(self, event):
        if event in self._timers.keys():
            self._timers[event].destroy()
            self._timers.pop(event)

    def delete_all_timers(self):
        for i in self._timers:
            self._timers[i].destroy()
