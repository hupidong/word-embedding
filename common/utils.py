import sys
import time

"""
******functions for parameter processing******
"""
def print_progress(task_name, percentage, style=0):
    """
    Print progress bar
    Args:
      task_name: The name of the current task
      percentage: Current progress
      style: Progress bar form
    """
    styles = ['#', '█']
    mark = styles[style] * percentage
    mark += ' ' * (100 - percentage)
    status = '%d%%' % percentage if percentage < 100 else 'Finished'
    sys.stdout.write('%+20s [%s] %s\r' % (task_name, mark, status))
    sys.stdout.flush()
    time.sleep(0.002)