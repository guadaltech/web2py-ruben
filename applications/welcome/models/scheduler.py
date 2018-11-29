
import os
import time
from gluon.scheduler import Scheduler
db_dal = os.path.abspath(os.path.join(request.folder, '..', '..', 'dummy2.db'))
sched_dal = DAL('sqlite://%s' % db_dal, folder=os.path.dirname(db_dal))
sched = Scheduler(sched_dal, max_empty_runs=15, migrate=False, heartbeat=1)
def termination():
    sched.terminate()
    sched_dal.commit()
            
def demo1(*args,**vars):
    print('you passed args=%s and vars=%s' % (args, vars))
    return args[0]
import random
def demo7():
    time.sleep(random.randint(1,5))
    print(W2P_TASK, request.now)
    return W2P_TASK.id, W2P_TASK.uuid, W2P_TASK.run_id
