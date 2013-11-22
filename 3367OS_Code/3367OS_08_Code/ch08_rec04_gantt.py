from datetime import datetime
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.dates as mdates

import logging


class Gantt(object):
    '''
    Simple Gantt renderer.
    Uses *matplotlib* rendering capabilities.
    '''

    # Red Yellow Green diverging colormap
    # from http://colorbrewer2.org/
    RdYlGr = ['#d73027', '#f46d43', '#fdae61',
              '#fee08b', '#ffffbf', '#d9ef8b',
              '#a6d96a', '#66bd63', '#1a9850']

    POS_START = 1.0
    POS_STEP = 0.5

    def __init__(self, tasks):
        self._fig = plt.figure()
        self._ax = self._fig.add_axes([0.1, 0.1, .75, .5])

        self.tasks = tasks[::-1]

    def _format_date(self, date_string):
        '''
        Formats string representation of *date_string* into *matplotlib.dates*
        instance.
        '''
        try:
            date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        except ValueError as err:
            logging.error("String '{0}' can not be converted to datetime object: {1}"
                  .format(date_string, err))
            sys.exit(-1)
        mpl_date = mdates.date2num(date)
        return mpl_date

    def _plot_bars(self):
        '''
        Processes each task and adds *barh* to the current *self._ax* (*axes*).
        '''
        i = 0
        for task in self.tasks:
            start = self._format_date(task['start'])
            end = self._format_date(task['end'])
            bottom = (i * Gantt.POS_STEP) + Gantt.POS_START
            width = end - start
            self._ax.barh(bottom, width, left=start, height=0.3,
                          align='center', label=task['label'],
                          color = Gantt.RdYlGr[i])
            i += 1

    def _configure_yaxis(self):
        '''y axis'''
        task_labels = [t['label'] for t in self.tasks]
        pos = self._positions(len(task_labels))
        ylocs = self._ax.set_yticks(pos)
        ylabels = self._ax.set_yticklabels(task_labels)
        plt.setp(ylabels, size='medium')

    def _configure_xaxis(self):
        ''''x axis'''
        # make x axis date axis
        self._ax.xaxis_date()

        # format date to ticks on every 7 days
        rule = mdates.rrulewrapper(mdates.DAILY, interval=7)
        loc = mdates.RRuleLocator(rule)
        formatter = mdates.DateFormatter("%d %b")

        self._ax.xaxis.set_major_locator(loc)
        self._ax.xaxis.set_major_formatter(formatter)
        xlabels = self._ax.get_xticklabels()
        plt.setp(xlabels, rotation=30, fontsize=9)

    def _configure_figure(self):
        self._configure_xaxis()
        self._configure_yaxis()

        self._ax.grid(True, color='gray')
        self._set_legend()
        self._fig.autofmt_xdate()

    def _set_legend(self):
        '''
        Tweak font to be small and place *legend*
        in the upper right corner of the figure
        '''
        font = font_manager.FontProperties(size='small')
        self._ax.legend(loc='upper right', prop=font)

    def _positions(self, count):
        '''
        For given *count* number of positions, get array for the positions.
        '''
        end = count * Gantt.POS_STEP + Gantt.POS_START
        pos = np.arange(Gantt.POS_START, end, Gantt.POS_STEP)
        return pos

    def show(self):
        self._plot_bars()
        self._configure_figure()
        plt.show()


if __name__ == '__main__':
    TEST_DATA = (
                 { 'label': 'Research',       'start':'2013-10-01 12:00:00', 'end': '2013-10-02 18:00:00'},  # @IgnorePep8
                 { 'label': 'Compilation',    'start':'2013-10-02 09:00:00', 'end': '2013-10-02 12:00:00'},  # @IgnorePep8
                 { 'label': 'Meeting #1',     'start':'2013-10-03 12:00:00', 'end': '2013-10-03 18:00:00'},  # @IgnorePep8
                 { 'label': 'Design',         'start':'2013-10-04 09:00:00', 'end': '2013-10-10 13:00:00'},  # @IgnorePep8
                 { 'label': 'Meeting #2',     'start':'2013-10-11 09:00:00', 'end': '2013-10-11 13:00:00'},  # @IgnorePep8
                 { 'label': 'Implementation', 'start':'2013-10-12 09:00:00', 'end': '2013-10-22 13:00:00'},  # @IgnorePep8
                 { 'label': 'Demo',           'start':'2013-10-23 09:00:00', 'end': '2013-10-23 13:00:00'},  # @IgnorePep8
                )

    gantt = Gantt(TEST_DATA)
    gantt.show()
