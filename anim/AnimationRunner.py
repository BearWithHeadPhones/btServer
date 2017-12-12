import threading

class AnimationThread (threading.Thread):
   def __init__(self, animation):
       threading.Thread.__init__(self)
       self._stop_event = threading.Event()
       self.animation = animation

   def stop(self):
       self._stop_event.set()

   def stopped(self):
       return self._stop_event.is_set()

   def run(self):
       self.animation.run(self)

def dummy():
    return

class AnimationRunner :
    def __init__(self):
        self.currentAnimation = AnimationThread(OneTime(dummy))
        self.currentAnimation.start()

    def animate(self, animation):
        if self.currentAnimation and False == self.currentAnimation.stopped() :
            self.currentAnimation.stop()
            self.currentAnimation.join()
        self.currentAnimation = AnimationThread(animation)
        self.currentAnimation.start()


class Loop :
    def __init__(self, anim):
        self.anim = anim

    def run(self, animationThread):
        while False == animationThread.stopped():
            self.anim()


class OneTime :
    def __init__(self, anim):
        self.anim = anim

    def run(self, animationThread):
        self.anim()
        return










