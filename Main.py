import drawer
import implementation
import interact_interface
import threading
import time

# driver code
if __name__=="__main__":

    interact_interface.Interact()
    obj=drawer.Drawer()
    ob=obj.please_draw()

    i=implementation.Implementation(obj)
    mark_lists=i.Start(obj)
    obj.draw_marks(mark_lists,ob)
    

    
