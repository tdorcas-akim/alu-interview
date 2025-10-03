#!/usr/bin/python3
"""
0-rain
Calculates the total amount of rainwater retained between walls.
"""


def rain(walls):
        """
            Calculates how many square units of water will be retained after it rains.

                Args:
                        walls (list): A list of non-negative integers representing the
                                              heights of walls with unit width 1.

                                                  Returns:
                                                          int: Total amount of rainwater retained.
                                                              """
                                                                  if not walls or len(walls) < 3:
                                                                              # Cannot retain water with less than 3 walls or an empty list.
                                                                                      return 0

                                                                                      total_water = 0
                                                                                          left = 0
                                                                                              right = len(walls) - 1
                                                                                                  max_left = 0
                                                                                                      max_right = 0

                                                                                                          while left < right:
                                                                                                                      if walls[left] < walls[right]:
                                                                                                                                      # The retaining height is limited by the left side.
                                                                                                                                                  if walls[left] >= max_left:
                                                                                                                                                                      # Update the maximum left height
                                                                                                                                                                                      max_left = walls[left]
                                                                                                                                                                                                  else:
                                                                                                                                                                                                                      # Water retained at this position is max_left - current height
                                                                                                                                                                                                                                      total_water += max_left - walls[left]
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                              # Move the left pointer to the right
                                                                                                                                                                                                                                                                          left += 1
                                                                                                                                                                                                                                                                                  else:
                                                                                                                                                                                                                                                                                                  # The retaining height is limited by the right side.
                                                                                                                                                                                                                                                                                                              if walls[right] >= max_right:
                                                                                                                                                                                                                                                                                                                                  # Update the maximum right height
                                                                                                                                                                                                                                                                                                                                                  max_right = walls[right]
                                                                                                                                                                                                                                                                                                                                                              else:
                                                                                                                                                                                                                                                                                                                                                                                  # Water retained at this position is max_right - current height
                                                                                                                                                                                                                                                                                                                                                                                                  total_water += max_right - walls[right]
                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                          # Move the right pointer to the left
                                                                                                                                                                                                                                                                                                                                                                                                                                      right -= 1

                                                                                                                                                                                                                                                                                                                                                                                                                                          return total_water
