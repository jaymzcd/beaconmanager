# Beacon Management for In-Store applications

## Store App (node.js)

Uses bluetooth to scan for beacon devices broadbasting and log them
as they appear along with RSSI strengths and proximity level. 

![](http://i.imgur.com/CnRHZyH.pngg)

## Beacon Management (Django)

A backend management application using Django provides a central point of
management and end points for applications to get data from. Pings from
store applications can update metadata as well as checkin times allowing the
monitoring of beacons and tracking of failures.

![](http://i.imgur.com/htL7jSD.png)
