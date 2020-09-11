def manhattanDistance(firstCoords, secondCoords):
    # Minus the second set of coords from the first. ABS makes sure the number is positive when printed (Absolute value)
    print(abs(firstCoords[0] - secondCoords[0]) +
          abs(firstCoords[1] - secondCoords[1]))


manhattanDistance([1, 2], [1, 3])
manhattanDistance([5, 2], [7, 3])
manhattanDistance([1, 2], [4, 4])
