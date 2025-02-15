RESPONSES = {
    "WELCOME":{
        "default":[
            {
                "type":"plain",
                "content":"220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------"
            },
            {
                "type":"plain",
                "content":"220-You are user number _CURRENT_ of _ALLOWED_USERS_ allowed."
            },
            {
                "type":"plain",
                "content":"220-Local time is now _TIME_. Server port: _PORT_."
            },
            {
                "type":"plain",
                "content":"220-This is a private system - No anonymous login"
            },
            {
                "type":"plain",
                "content":"220 You will be disconnected after 15 minutes of inactivity."
            }
        ]
    },
    "USER":{
        "default":[
            {
                "type":"plain",
                "content":"331 User _USERNAME_ OK. Password required"
            }
        ]
    },
    "PASS":{
        "default":[
            {
                "type":"plain",
                "content":"230 OK. Current directory is _DIRECTORY_"
            }
        ]
    },
    "PWD":{
        "default":[
            {
                "type":"plain",
                "content":"257 \"_DIRECTORY_\" is your current location"
            }
        ]
    },
    "CWD":{
        "default":[
            {
                "type":"plain",
                "content":"250 OK. Current directory is _DIRECTORY_"
            }
        ]
    },
    "PASV":{
        "default":[
            {
                "type":"plain",
                "content":"227 Entering Passive Mode (_IP1_,_IP2_,_IP3_,_IP4_,_PORT1_,_PORT2_)"
            }
        ]
    },
    "TYPE":{
        "default":[
            {
                "type":"plain",
                "content":"200 TYPE is now _TYPE_"
            }
        ]
    },
    "LIST":{
        "default":[
            {
                "type":"plain",
                "content":"150 Accepted data connection"
            },
            {
                "type":"plain",
                "content":"226-Options: -a -l"
            },
            {
                "type":"plain",
                "content":"226 6 _TOTALMATCHES_ total"
            },
            {
                "type":"data",
                "content":"_DATA_"
            }
        ]
    },
    "QUIT":{
        "default":[
            {
                "type":"plain",
                "content":"221-Goodbye. You uploaded _UPLOADED_ and downloaded _DOWNLOADED_ kbytes."
            },
            {
                "type":"plain",
                "content":"221 Logout."
            }
        ]
    },
    "RETR":{
        "default":[
            {
                "type":"plain",
                "content":"150-Accepted data connection"
            },
            {
                "type":"plain",
                "content":"150 _BYTESTODOWNLOAD_ kbytes to download"
            },
            {
                "type":"plain",
                "content":"226-File successfully transferred"
            },
            {
                "type":"plain",
                "content":"226 _SECONDSTOTRANSFER_ seconds (measured here), _MBYTESPERSECOND_ Mbytes per second"
            }
        ]
    }
}