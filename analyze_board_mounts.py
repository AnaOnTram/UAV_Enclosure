from __future__ import annotations

import struct
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


STL_PATH = Path(r"C:\Users\ANA\Documents\UAV\ZD850_UP.stl")
QUANTIZE_MM = 0.001


def read_binary_stl(path: Path) -> np.ndarray:
    with path.open("rb") as handle:
        handle.read(80)
        triangle_count = struct.unpack("<I", handle.read(4))[0]
        data = np.fromfile(
            handle,
            dtype=np.dtype(
                [
                    ("normal", "<f4", (3,)),
                    ("vertices", "<f4", (3, 3)),
                    ("attribute", "<u2"),
                ]
            ),
            count=triangle_count,
        )
    return data["vertices"].astype(np.float64)


def key(point: np.ndarray) -> tuple[int, int]:
    return tuple(np.rint(point[:2] / QUANTIZE_MM).astype(np.int64))


def point_from_key(point_key: tuple[int, int]) -> np.ndarray:
    return np.asarray(point_key, dtype=np.float64) * QUANTIZE_MM


def polygon_area(points: np.ndarray) -> float:
    x = points[:, 0]
    y = points[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


triangles = read_binary_stl(STL_PATH)
top_z = float(triangles[:, :, 2].max())
top_mask = np.all(np.isclose(triangles[:, :, 2], top_z, atol=1e-4), axis=1)
top_triangles = triangles[top_mask]

edge_counts: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
for triangle in top_triangles:
    for start_index, end_index in ((0, 1), (1, 2), (2, 0)):
        start = key(triangle[start_index])
        end = key(triangle[end_index])
        edge = tuple(sorted((start, end)))
        edge_counts[edge] += 1

boundary_edges = [edge for edge, count in edge_counts.items() if count == 1]
adjacency: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
for start, end in boundary_edges:
    adjacency[start].append(end)
    adjacency[end].append(start)

unused = set(boundary_edges)
loops: list[np.ndarray] = []
while unused:
    first_edge = next(iter(unused))
    start, current = first_edge
    previous = start
    path = [start, current]
    unused.remove(first_edge)
    while current != start:
        candidates = [
            neighbor
            for neighbor in adjacency[current]
            if neighbor != previous
            and tuple(sorted((current, neighbor))) in unused
        ]
        if not candidates:
            break
        next_point = candidates[0]
        unused.remove(tuple(sorted((current, next_point))))
        previous, current = current, next_point
        path.append(current)
    if len(path) >= 4 and path[-1] == path[0]:
        loops.append(np.asarray([point_from_key(item) for item in path[:-1]]))

records = []
for loop in loops:
    minimum = loop.min(axis=0)
    maximum = loop.max(axis=0)
    centroid = loop.mean(axis=0)
    records.append(
        {
            "area": polygon_area(loop),
            "centroid": centroid,
            "minimum": minimum,
            "maximum": maximum,
            "size": maximum - minimum,
            "vertices": len(loop),
        }
    )

records.sort(key=lambda record: record["area"], reverse=True)
print(f"top_z={top_z:.4f} mm")
print(f"top_triangles={len(top_triangles)} boundary_loops={len(records)}")
for index, record in enumerate(records):
    if index > 0 and record["area"] > 500:
        continue
    if index > 0 and record["area"] < 1:
        continue
    centroid = record["centroid"]
    size = record["size"]
    minimum = record["minimum"]
    maximum = record["maximum"]
    print(
        f"{index:03d} area={record['area']:.3f} "
        f"center=({centroid[0]:.3f},{centroid[1]:.3f}) "
        f"size=({size[0]:.3f},{size[1]:.3f}) "
        f"bbox=({minimum[0]:.3f},{minimum[1]:.3f})"
        f"..({maximum[0]:.3f},{maximum[1]:.3f}) "
        f"vertices={record['vertices']}"
    )
