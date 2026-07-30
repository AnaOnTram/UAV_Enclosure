# UAV Enclosure v0.11 — Reduced-Height Variant

## Height definition

- Nominal electronics stack height: 35 mm
- Vertical assembly tolerance / clearance: 2 mm
- Usable internal enclosure height: 37 mm
- Roof thickness: 3 mm
- Canopy exterior height from the mounting surface: 40 mm
- Maximum overall height including the raised LD06 mounting columns: 59.8 mm

The 2 mm allowance is intentionally added above the requested 35 mm rather than making the internal cavity exactly 35 mm. This provides clearance for board-height variation, cable routing, vibration, and manufacturing tolerances.

## Changes from v0.10

- Reduced the drafted canopy extrusion from 58 mm to 37 mm.
- Reduced the matching hollow electronics cavity depth from 58 mm to 37 mm.
- Preserved the 3 mm roof thickness.
- Preserved the large hollow center for the PX6, RF board, and cable routing.
- Preserved the symmetric left/right RF-board arrangement envelope.
- Preserved the outer mounting brim, R30 brim corners, and eight independent M3 mounting holes.
- Preserved the edge-mounted LD06 platform, rotated PiBracket-style locating columns, two 55.5 mm GPS antenna recesses, and the shared rounded rectangular cable slot.

## Validation

- Rebuild status: successful
- Solid bodies: 1
- Bounding box: 180.5 mm × 190.0 mm × 59.8 mm
- Solid volume: 179.337 cm³
- Surface area: 0.10675 m²
- Previous maximum height: 80.8 mm
- Height reduction: 21.0 mm (about 26%)
- Previous solid volume: 212.341 cm³
- Solid-volume reduction: about 15.5%

The SolidWorks model remains parametric: the canopy and cavity depths are named `Cockpit_Canopy_37H_Draft10deg` and `Symmetric_Electronics_Cavity_37H`.
