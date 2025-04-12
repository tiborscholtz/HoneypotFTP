import json
from math import floor
import selectors
import socket
import curses
import queue
import sys
import os
from typing import List
from configuration import configuration
from connection import Connection
from connectionlog import ConnectionLog
from filestructure import FileStructure
from screen import Screen
connections: List[Connection] = list()
connectionlogs : List[ConnectionLog] = list()
import threading
selector = selectors.DefaultSelector()
screen = Screen()
f = FileStructure(configuration.get_filesystem_depth(),configuration.get_file_ratio(),configuration.get_directory_ratio(),configuration.get_average_entity_per_directory())


def get_x_center(text,maxx):
    return floor((maxx / 2) - (len(text) / 2))

def curses_interface(stdscr):
    global screen
    sys.stdout = open(os.devnull, 'w')
    stdscr.nodelay(1)
    maxy, maxx = stdscr.getmaxyx()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    while True:
        screen.print_curses_options(stdscr,screen.get_current_page())
        if screen.is_current_page("c"):
            welcome_text = "Welcome to HoneypotFTP!"
            stdscr.addstr(1, get_x_center(welcome_text,maxx), welcome_text, curses.color_pair(16))
            if len(connections) > 0:
                connections_text = "There are "+str(len(connections))+" connections...."
                stdscr.addstr(4, get_x_center(connections_text,maxx),connections_text,curses.color_pair(3))
                col_widths = [30, 20,50,80]
                col_width_max = floor((maxx / 2) - (sum(col_widths) / 2))
                start_y, start_x = 10, col_width_max 
                headers = ["ID","IP address","Connected at","Current path"]
                data = []
                for i in range(len(connections)):
                    data.append([connections[i].get_id(),connections[i].get_ip_address(),connections[i].get_connected_at(),connections[i].get_current_path()])
                screen.print_table(stdscr,col_widths,headers,data,start_x,start_y)
                pass
            else:
                no_connection_text = "There are no connections...."
                stdscr.addstr(4, get_x_center(no_connection_text,maxx),no_connection_text,curses.color_pair(3) )
        if screen.is_current_page("s"):
            col_widths = [30, 20,70]
            col_width_max = floor((maxx / 2) - (sum(col_widths) / 2))
            start_y, start_x = 10, col_width_max
            config_data = configuration.get_object_format()
            screen.print_table(stdscr,col_widths,config_data["headers"],config_data["data"],start_x,start_y)
            pass
        if screen.is_current_page("l"):
            col_widths = [40, 40,70]
            col_width_max = floor((maxx / 2) - (sum(col_widths) / 2))
            start_y, start_x = 10, col_width_max
            config_data = configuration.get_object_format()
            columns = ["IP Address","Timestamp","Text"]
            data = []
            for i in range(len(connectionlogs)):
                data.append([connectionlogs[i].get_ip_address(),connectionlogs[i].get_timestamp(),connectionlogs[i].get_text()])
            screen.print_table(stdscr,col_widths,columns,data,start_x,start_y)
            pass
        key = stdscr.getch()  # Capture keypress
        if key == ord('q'):
            break  # Quit when 'q' is pressed
        if  key == ord('c'):
            screen.change_current_page("c")
            stdscr.clear()
            stdscr.refresh()
            pass
        if key == ord('s'):
            screen.change_current_page("s")
            stdscr.clear()
            stdscr.refresh()
            pass
        if key == ord('l'):
            screen.change_current_page("l")
            stdscr.clear()
            stdscr.refresh()
            pass
        if key != -1:
            stdscr.refresh()
        try:
            msg = configuration.get_message()
            sys.stdout = sys.__stdout__
            if "type" not in msg or "data" not in msg:
                continue
            if msg["type"] == "send_log":
                connectionlogs.append(msg["data"])
            stdscr.clear()
            stdscr.refresh()
        except queue.Empty:
            pass
    sys.stdout = sys.__stdout__


def accept_connection(server_sock):
    conn, addr = server_sock.accept()
    current_id = len(connections)
    connection = Connection(current_id,conn, addr[0], selector,configuration,configuration.get_logging(),f._structure)
    configuration.send_message(f"Update {current_id}")
    connections.append(connection)
    if not selector.get_map().get(conn.fileno()):  
        selector.register(conn, selectors.EVENT_READ, connection.handle_connection)

def start_server(host='127.0.0.1', port=configuration.get_command_port()):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(100)
    server_sock.setblocking(False)
    selector.register(server_sock, selectors.EVENT_READ, accept_connection)
    try:
        while True:
            events = selector.select()
            for key, _ in events:
                callback = key.data 
                callback(key.fileobj) 
    except KeyboardInterrupt:
        pass
    finally:
        server_sock.close()
        selector.close()

if __name__ == "__main__":
    threading.Thread(target=start_server,daemon=True).start()
    curses.wrapper(curses_interface)
    #start_server()
    pass
