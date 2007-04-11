import rope.base
import rope.refactor


class TaskHandle(object):

    def __init__(self, name='Task'):
        self.name = name
        self.stopped = False
        self.job_sets = []
        self.observers = []

    def is_stopped(self):
        return self.stopped

    def stop(self):
        self.stopped = True
        self._inform_observers()

    def create_job_set(self, name='JobSet', count=None):
        result = JobSet(self, name=name, count=count)
        self.job_sets.append(result)
        self._inform_observers()
        return result

    def get_job_sets(self):
        return self.job_sets

    def add_observer(self, observer):
        self.observers.append(observer)

    def _inform_observers(self):
        for observer in list(self.observers):
            observer()


class JobSet(object):

    def __init__(self, handle, name, count):
        self.handle = handle
        self.name = name
        self.count = count
        self.done = 0
        self.job_name = None

    def started_job(self, name):
        self.check_status()
        self.job_name = name
        self.handle._inform_observers()

    def finished_job(self):
        self.handle._inform_observers()
        self.job_name = None
        self.done += 1

    def check_status(self):
        if self.handle.is_stopped():
            raise rope.base.exceptions.InterruptedTaskError()

    def get_active_job_name(self):
        return self.job_name

    def get_percent_done(self):
        if self.count is not None:
            percent = self.done * 100 / self.count
            return min(percent, 100)

    def get_name(self):
        return self.name


class NullTaskHandle(object):

    def __init__(self):
        pass

    def is_stopped(self):
        return False

    def stop(self):
        pass

    def create_job_set(self, *args, **kwds):
        return NullJobSet()

    def get_job_sets(self):
        return []

    def add_observer(self, observer):
        pass



class NullJobSet(object):

    def started_job(self, name):
        pass

    def finished_job(self):
        pass

    def check_status(self):
        pass

    def get_active_job_name(self):
        pass

    def get_percent_done(self):
        pass

    def get_name(self):
        pass