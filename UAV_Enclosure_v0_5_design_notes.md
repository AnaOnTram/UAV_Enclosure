# UAV Enclosure v0.5

## Board interface

- External mounting brim: 180 x 190 x 3 mm
- Brim envelope including reinforced pads: 183 x 190 mm
- Eight M3 clearance holes: diameter 3.4 mm
- Reinforcement pads: diameter 10 mm, 2.5 mm above the brim
- Hole centers, measured from `ZD850_UP.stl`:
  - X = +/-86.5 mm, Y = +/-11 mm
  - X = +/-61.776 mm, Y = +/-85.000 mm

## Canopy and electronics bay

- Left/right-symmetric eight-sided cockpit-canopy planform
- Base planform: 150 x 160 mm maximum
- Inward aerodynamic draft: 10 degrees
- External corner radius: 10 mm
- Roof-edge radius: 6 mm
- Symmetric drafted cavity: 58 mm high
- The 120 x 80 mm central equipment region retains at least 50 mm clear height.
- The RF board can be arranged on either side of a centered Pixhawk 6X.

## LD06 interface

- Raised platform: 48 x 48 x 8 mm
- Two PiBracket-style fixing columns: diameter 4.3 x 11.8 mm
- Column center offsets from the LiDAR center:
  - X = -14.1 mm, Y = +14.1 mm
  - X = +14.1 mm, Y = -14.1 mm
- Blind pilot holes: diameter 1.5 mm x 11.3 mm deep

## Cable ports

- Two GPS cable ports: diameter 10 mm
- One UART cable port: diameter 8 mm
- All three ports are on the upper canopy surface behind the raised LiDAR platform.

## Validation

- SolidWorks rebuild after close/reopen: successful
- Solid body count: 1
- Overall bounding box: 183 x 190 x 80.8 mm
- Solid volume: 209.542 cm3
