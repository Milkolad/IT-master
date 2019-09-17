import pandas as pd
import math

class Metro:
    def __init__(self, stations, changes):
        metro_df = pd.read_csv(stations)
        changes_df = pd.read_csv(changes)
        lines_list = metro_df['Line'].values.tolist()
        self.lines = []
        for line in lines_list:
            stations_list = (metro_df.loc[metro_df['Line'].str.strip() == line, ['Name', 'Line', 'Order']]).values.tolist()
            self.lines.append(Line(stations_list, [], line))

    def get_line(self, line_name):
        return [line for line in self.lines if line.name == line_name][0]

    def find_station(self, station_name):
        for line in self.lines:
            station = line.get_station()
            if station is not None:
                return station
        return None

    def get_length(self, start_name, end_name):
        start = self.find_station(start_name)
        end = self.find_station(end_name)
        if start is not None and end is not None:
            if start.line_name == end.line_name:
                return self.get_line(start.line_name).get_length(start_name, end_name)
            else:
                start_line = self.get_line(start.line_name)
                sub_end = start_line.get_change(end.line_name)
                sub_start = 
                return 999
        else:
            return -1


class Line:
    def __init__(self, stations, changes, name):
        self.stations = [Station(station, changes) for station in stations]
        self.name = name

    def get_station(self, station_name):
        return [station for station in self.stations if station.name == station_name][0] or None

    def get_length(self, start_name, end_name):
        start = [station for station in self.stations if station.name == start_name][0]
        end = [station for station in self.stations if station.name == end_name][0]
        return int(math.fabs(start.order - end.order))

    def get_change(self, line_name):
        return 0 #station

class Station:
    def __init__(self, station, changes):
        self.name = station[0]
        self.line_name = station[1]
        self.order = int(station[2])
        self.changes = []
        for change in changes:
            self.changes.append(Change(change))
    
    def change(self, from_line, to_line):
        if len(self.changes) > 0:
            chng = [change for change in self.changes if change.line_from == from_line and change.line_to == to_line][0]
            return chng.name_to
        else:
            return None

class Change:
    def __init__(self, change):
        self.line_from = change[0]
        self.line_to = change[1]
        self.name_from = change[2]
        self.name_to = change[3]